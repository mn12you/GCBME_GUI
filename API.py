import sys
import os
import time
from PyQt5 import uic
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow , QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox,QFileDialog
from PyQt5.QtCore import  QThread, pyqtSignal, QObject
import serial.tools.list_ports
from ctypes import *
from mecg20 import *
from aecg100 import *
from secg50 import *
Label_reader={'Normal':0,'AFib':1}

ac = None
dc = None
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

class Worker(QObject):
    finished = pyqtSignal()
    label=pyqtSignal(int)
    result = pyqtSignal(str)
    AI_pred=pyqtSignal(int)
    
    def __init__(self,device,data_path,ser,device_name):
        super().__init__()
        self.device=device
        self.data_path=data_path
        self.ser=ser
        self.device_name=device_name
    
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
            QApplication.processEvents() 
            for file in files_in_directory:
                file_path=os.path.join(dirpath,file)
                if dirpath.find("Afib"):
                    self.label.emit(0)
                else:
                    self.label.emit(1)
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
                while 1:
                 
                    if self.ser.inWaiting() > 0:
                        result = self.ser.readline()
                        decoded_data = result.decode('ascii').strip()     # Get OKEY and start to send ECG
                        self.AI_pred.emit(Label_reader[decoded_data[1:]])
                        self.result.emit(decoded_data[1:])
                        if self.device_name==0:
                            self.device.stop_output()
                        elif self.device_name==1:
                            self.device.set_output_function(OutputFunction.Output_Off.value)
                        break

class ComboBox(QtWidgets.QComboBox):
    popupAboutToBeShown = QtCore.pyqtSignal()

    def showPopup(self):
        self.popupAboutToBeShown.emit()
        super(ComboBox, self).showPopup()

class GCBME_app(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI.ui',self)

        # self.device = MECG20()
        self.device_name=0
        self.ser = serial.Serial()
        self.button_pause=True
        self.AI_pred=[]
        self.label=[]

        self.Serial_buttn.clicked.connect(self.connect_port)
        self.Serial_item.popupAboutToBeShown.connect(self.update_ports)
        self.data_buttn.clicked.connect(self.choose_dataset)        
        self.Pause_buttn.clicked.connect(self.pause_it)
        self.Start_buttn.clicked.connect(self.start_multi)



    def update_ports(self):
        """Updates the list of available serial ports."""
        self.Serial_item.clear()  # Clear the combo box
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.Serial_item.addItem(port.device)  # Add port name to combo box
    
    def pause_it(self):
        self.button_pause=False
    def connect_port(self):
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
        # Open the folder dialog and allow the user to select a folder
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")

        # If the user selects a folder, update the label with the folder path
        if folder_path:
            self.data_path.setText(folder_path)
        else:
            self.data_path.setText("No folder selected")
        
    def start_multi(self):
        self.AI_pred=[]
        self.label=[]
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
        # Connect worker's progress signal to a handler method
        self.worker.result.connect(self.report_result)
        self.worker.AI_pred.connect(self.AI_result)
        self.worker.label.connect(self.label_result)
        # Start the thread
        self.thread.start()

    def report_result(self,decoded_data):
        self.Terminal_result.append(decoded_data)
    def AI_result(self,result):
        self.AI_pred.append(result)
        print(f'AI pred:{self.AI_pred}')
    def label_result(self,result):
        self.label.append(result)
        print(f'Label:{self.label}')
        

#     def start_test(self):
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GCBME_app()
    window.show()
    sys.exit(app.exec_())
