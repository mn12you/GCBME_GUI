import sys
import os
import time
from PyQt5 import uic
from PyQt5 import QtCore, QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow , QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox,QFileDialog
from PyQt5.QtCore import  QThread, pyqtSignal, QObject, QMutex, QWaitCondition
from sklearn.metrics import accuracy_score, confusion_matrix
import serial.tools.list_ports
from ctypes import *
from mecg20 import *
from aecg100 import *
from secg50 import *
# Transform for model result
Label_reader={'Normal':0,'AFib':1}
Label_transform={0:'Normal',1:'AFib'}
# AECG100 control parameter
ac = None
dc = None

# AECG100 load txt function
def load_raw_data_file(file_name):
    global ac, dc
    
    play_raw_data = PLAY_RAW_DATA()
    lineNumber = 0
    f = open(file_name)
    for x in f:
        if lineNumber == 0:
            play_raw_data.SampleRate = int(x)
        elif lineNumber == 1:
            play_raw_data.Size = int(x)
            ac = (c_double * play_raw_data.Size)()
            dc = (c_double * play_raw_data.Size)()
        elif lineNumber >= 4:
            ac[lineNumber-4] = float(x)
            dc[lineNumber-4] = 0

        lineNumber = lineNumber + 1

    f.close()

    play_raw_data.AC = addressof(ac)
    play_raw_data.DC = addressof(dc)
    play_raw_data.OutputSignalCallback =CFUNCTYPE(None, c_double, c_int, c_int)(0)
    return play_raw_data

# woker for sending ECG 
class Worker(QObject):
    finished = pyqtSignal()
    result = pyqtSignal(int,int,float)
    
    def __init__(self,device,data_path,ser,device_name):
        super().__init__()
        self.device=device
        self.data_path=data_path
        self.ser=ser
        self.device_name=device_name
        self._is_paused = False
        self._is_running = True
        self._mutex = QMutex()
        self._pause_condition = QWaitCondition()
    
    def run(self):
        # Simulate a long-running task

        if self.device.connect(-1, 5000) == False:
            print('Error: ECG device is not connected')
            self.device.free()
            sys.exit()
        print('device is connected... ' + self.device.get_serial_number())

        if not (os.path.exists(self.data_path)):
            print("請指定正確 data folder")
            return
        else:
            data_folder=self.data_path

        for dirpath, dirnames,files_in_directory in os.walk(data_folder):
            
            self._mutex.lock()
            if self._is_paused:
                self._pause_condition.wait(self._mutex)
            self._mutex.unlock()
            
            if not self._is_running:
                self.device.free()
                break

            for file in files_in_directory:
                file_path=os.path.join(dirpath,file)
                print(file_path)
                if  file_path.find("Afib")!=-1:
                    label_encode=1
                else:
                    label_encode=0
                send_str="k"
                self.ser.write(send_str.encode())

################################################# Start sending ECG ######################################################     
                print('output whaleteq-format data...')
                if self.device_name==0:
                    raw_data = load_raw_data_file(file_path)
                    self.device.enable_player_loop(c_bool(True))
                    self.device.play_raw_ecg(pointer(raw_data))
                elif self.device_name==1:
                    self.device.reset()
                    fileName = c_char_p(file_path.encode('utf-8'))
                    success = self.device.load_ecg_txt(fileName, 0)  # Load .txt file in whaleteq format
                    if success > 0:
                        self.device.set_output_function(OutputFunction.Output_ECG_File.value)
                    elif success == -1:
                        raise IOError("Open file failed")
                    elif success == -2:
                        raise IOError("Invalid sample rate in Line 1")
                    elif success == -3:
                        raise IOError("Invalid sample number in Line 2")
                    elif success == -4:
                        raise IOError("Invalid channel number in Line 3")
                    elif success == -5:
                        raise IOError("Invalid description in Line 4")
                    elif success == -6:
                        raise IOError("Raw data file is too large to fit the memory")
                    elif success == -7:
                        raise IOError("No such channel")
                    else:
                        sys.exit()
                else:
                    sys.stdout.flush()  
                    header = self.device.load_whaleteq_database(create_string_buffer(file_path.encode('ascii'))) 
                    sys.stdout.flush()               
                    if not header:
                        print('failed')
                        self.device.free()
                        sys.exit()             
                    self.device.output_waveform(0, None, None)   # Send ECG to simulator 
                start_time=time.time()
                while 1:
                 
                    if self.ser.inWaiting() > 0:
                        result = self.ser.readline()
                        decoded_data = result.decode('ascii').strip()     # Get OKEY and start to send ECG
                        end_time=time.time()
                        self.result.emit(Label_reader[decoded_data[1:]],label_encode,(end_time-start_time))
                        if self.device_name==0:
                            self.device.stop_output()
                        elif self.device_name==1:
                            self.device.set_output_function(OutputFunction.Output_Off.value)
                        break
        self.device.free()
        self.finished.emit()

    def pause(self):
        self._mutex.lock()
        self._is_paused = True
        self._mutex.unlock()

    def resume(self):
        self._mutex.lock()
        self._is_paused = False
        self._pause_condition.wakeAll()
        self._mutex.unlock()

    def stop(self):
        self._is_running = False
        if self._is_paused:
            self.resume()  # In case it's paused, resume and stop


# Combobox class to add up click update function
class ComboBox(QtWidgets.QComboBox):
    popupAboutToBeShown = QtCore.pyqtSignal()

    def showPopup(self):
        self.popupAboutToBeShown.emit()
        super(ComboBox, self).showPopup()

# the main window class for the GUI
class GCBME_app(QMainWindow):
    
    #initial function
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI.ui',self)
        
        self.device_name=0 #device flag AECG100:'0' ; SECG50:'1'
        self.ser = serial.Serial()# serial port
        self.AI_pred=[]# AI result
        self.label=[]#label result
        self.latency=[]#latency result
        self.pause_button_state=0 # button state PAUSE:'0' ; RESUME:'1'
        self.start_button_state=0 # button state START:'0' ; STOP:'1'

        # UI initiate 
        self.Serial_buttn.clicked.connect(self.connect_port)
        self.Serial_item.popupAboutToBeShown.connect(self.update_ports)
        self.data_buttn.clicked.connect(self.choose_dataset)        
        self.Start_buttn.clicked.connect(self.start_multi)
        self.pause_resume.clicked.connect(self.pause_resume_task)
        self.Export_result.clicked.connect(self.export)

    def update_ports(self):
        """Updates the list of available serial ports."""
        self.Serial_item.clear()  # Clear the combo box
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.Serial_item.addItem(port.device)  # Add port name to combo box

    def connect_port(self):
        """Create Serial connection according to selected port"""
        comport=self.Serial_item.currentText()
        if comport!="":
            baudrate=115200
            print(comport + ' @ ' + '%d' %baudrate)
            self.ser.port =comport
            self.ser.baudrate = baudrate
            # self.ser.bytesize = serial.EIGHTBITS #number of bits per bytes
            # self.ser.parity = serial.PARITY_NONE #set parity check
            # self.ser.stopbits = serial.STOPBITS_ONE #number of stop bits

            # self.ser.timeout = 0.3        #non-block read 0.5s
            # self.ser.writeTimeout = 0.5     #timeout for write 0.5s
            # self.ser.xonxoff = False    #disable software flow control
            # self.ser.rtscts = False     #disable hardware (RTS/CTS) flow control
            # self.ser.dsrdtr = False     #disable hardware (DSR/DTR) flow control
            try: 
                self.ser.open()
            except Exception as ex:
                print ("open serial port error " + str(ex))
                return 0
            if self.ser.isOpen():
                print('Serial open!')
                return 1
            if self.ser.isOpen() == False:
                print('Serial connect fail!')
                return 0
        else:
            print("Comport not select!")
            
    def choose_dataset(self):
        '''Dataset select through QFileDialog'''
        # Open the folder dialog and allow the user to select a folder
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        # If the user selects a folder, update the label with the folder path
        if folder_path:
            self.data_path.setText(folder_path)
        else:
            self.data_path.setText("No folder selected")
        
    def start_multi(self):
        '''Start send ECG work'''
        if self.start_button_state==0:
            self.Terminal_result.clear()
            self.Final_result.clear()
            self.start_button_state=1
            self.Start_buttn.setText("Stop")

            self.AI_pred=[]
            self.label=[]
            self.latency=[]

            if self.ECG_device_box.currentText()=="AECG100":
                self.device=AECG100()
                self.device_name=0
            else:
                self.device=SECG50()
                self.device_name=1

            # Create a QThread object
            self.thread = QThread()
            # Create a worker object
            self.worker = Worker(self.device,self.data_path.text(),self.ser,self.device_name)
            # Move the worker to the thread
            self.worker.moveToThread(self.thread)
            # Connect the thread's started signal to the worker's run method
            self.thread.started.connect(self.worker.run)
            # Connect the worker's finished signal to stop the thread
            self.worker.finished.connect(self.thread.quit)
            # Optionally, delete the worker and thread when done
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.worker.finished.connect(self.final_report)
            # Connect worker's progress signal to a handler method
            self.worker.result.connect(self.report_result)
            # Start the thread
            self.thread.start()
        else:
            self.start_button_state=0
            self.Start_buttn.setText("Start")
            self.worker.stop()




    def report_result(self,AI,label,latency):
        '''Receive label result signal and Save it in array'''
        latency=round(latency,4)
        self.label.append(label)
        self.AI_pred.append(AI)
        self.latency.append(latency)
        acc=round(100*accuracy_score(self.label, self.AI_pred),3)
        print(f'Label:{self.label}')
        print(f'AI pred:{self.AI_pred}')
        print(f'Latency :{self.latency}')
        result_sentece=f"################\nAI prediction: {Label_transform[AI]}\nLabel: {Label_transform[label]}\nLatency: {latency}\nAccuracy so far: {acc}\n################"
        self.Terminal_result.append(result_sentece)
    
    def final_report(self):
        acc=round(100*accuracy_score(self.label, self.AI_pred),3)
        cm=confusion_matrix(self.label, self.AI_pred)
        latency=round(sum(self.latency) / len(self.latency),3)
        col_width = 30
        confusion_matrix_str=""
        confusion_matrix_str += f"{'':<{col_width}}{'Predicted Normal':<{col_width}}{'Predicted Afib':<{col_width}}\n"
        confusion_matrix_str += f"{'Actual Normal':<{col_width}}{cm[0][0]:<{col_width}}{cm[0][1]:<{col_width}}\n"
        confusion_matrix_str += f"{'Actual Afib':<{col_width}}{cm[1][0]:<{col_width}}{cm[1][1]:<{col_width}}\n"
        result_sentence=f"##########\n The accuracy is: {acc}\n The latency is: {latency}\nConfusion matrix is:\n"
        self.Final_result.append(result_sentence)
        self.Final_result.append(confusion_matrix_str)
        print(confusion_matrix_str)

    def pause_resume_task(self):
        if self.pause_button_state==0:
            self.pause_button_state=1
            self.pause_resume.setText("Resume")
            self.worker.pause()
        else:
            self.pause_button_state=0
            self.pause_resume.setText("Pause")
            self.worker.resume()
    
    def export(self):
        string_to_save=self.Final_result.toPlainText()
        group=self.Group_name.toPlainText()
        with open("./Result/"+group+"_result.txt", "w") as text_file:
            text_file.write(string_to_save)
        
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GCBME_app()
    window.show()
    app.exec_()



##### old code for one thread #####
# def start_test(self):
#         self.button_pause=True
#         self.AI_pred=[]
#         self.label=[]
#         if self.ECG_device_box.currentText()=="AECG100":
#             self.device=AECG100()
#             self.device_name=0
#         else:
#             self.device=SECG50()
#             self.device_name=1

        
        
#         if self.device.connect(-1, 5000) == False:
#             print('Error: ECG device is not connected')
#             self.device.free()
#             sys.exit()
#         print('device is connected... ' + self.device.get_serial_number())

#         if not (os.path.exists(self.data_path.text())):
#             print("請指定正確 data folder")
#             return
#         else:
#             data_folder=self.data_path.text()

#         for dirpath, dirnames,files_in_directory in os.walk(data_folder):
#             QApplication.processEvents() 
#             for file in files_in_directory:
#                 file_path=os.path.join(dirpath,file)
#                 if dirpath.find("Afib"):
#                     self.label.append(1)
#                 else:
#                     self.label.append(1)
#                 send_str="k"
#                 self.ser.write(send_str.encode())

# ################################################# Start sending ECG ######################################################     
#                 print('output whaleteq-format data...')
#                 if self.device_name==0:
#                     raw_data = load_raw_data_file(file_path)
#                     self.device.enable_player_loop(c_bool(True))
#                     self.device.play_raw_ecg(pointer(raw_data))
#                 elif self.device_name==1:
#                     self.device.reset()
#                     fileName = c_char_p(file_path.encode('utf-8'))
#                     success = self.device.load_ecg_txt(fileName, 0)  # Load .txt file in whaleteq format
#                     if success > 0:
#                         self.device.set_output_function(OutputFunction.Output_ECG_File.value)
#                     elif success == -1:
#                         raise IOError("Open file failed")
#                     elif success == -2:
#                         raise IOError("Invalid sample rate in Line 1")
#                     elif success == -3:
#                         raise IOError("Invalid sample number in Line 2")
#                     elif success == -4:
#                         raise IOError("Invalid channel number in Line 3")
#                     elif success == -5:
#                         raise IOError("Invalid description in Line 4")
#                     elif success == -6:
#                         raise IOError("Raw data file is too large to fit the memory")
#                     elif success == -7:
#                         raise IOError("No such channel")
#                     else:
#                         sys.exit()
#                 else:
#                     sys.stdout.flush()  
#                     header = self.device.load_whaleteq_database(create_string_buffer(file_path.encode('ascii'))) 
#                     sys.stdout.flush()               
#                     if not header:
#                         print('failed')
#                         self.device.free()
#                         sys.exit()             
#                     self.device.output_waveform(0, None, None)   # Send ECG to simulator 
#                 while 1:
#                     QApplication.processEvents() 
#                     if self.ser.inWaiting() > 0:
#                         result = self.ser.readline()
#                         decoded_data = result.decode('ascii').strip()     # Get OKEY and start to send ECG
#                         self.AI_pred.append(Label_reader[decoded_data[1:]])
#                         self.Terminal_result.append(decoded_data[1:])
#                         QApplication.processEvents() 
#                         # print(decoded_data[1:] )
#                         # print(self.AI_pred)
#                         # print(self.label)
#                         if self.device_name==0:
#                             self.device.stop_output()
#                         elif self.device_name==1:
#                             self.device.set_output_function(OutputFunction.Output_Off.value)
#                         break    
