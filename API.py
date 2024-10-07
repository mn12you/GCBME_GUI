import sys
import time
from PyQt5 import uic
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow , QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox,QFileDialog
import serial.tools.list_ports
from mecg20 import *



class ComboBox(QtWidgets.QComboBox):
    popupAboutToBeShown = QtCore.pyqtSignal()

    def showPopup(self):
        self.popupAboutToBeShown.emit()
        super(ComboBox, self).showPopup()

class GCBME_app(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('GUI.ui',self)

        self.device = MECG20()
        self.ser = serial.Serial()
        self.button_pause=True
        self.AI_pred=[]
        self.label=[]

        self.Serial_buttn.clicked.connect(self.connect_port)
        self.Serial_item.popupAboutToBeShown.connect(self.update_ports)
        self.data_buttn.clicked.connect(self.choose_dataset)        
        self.Pause_buttn.clicked.connect(self.pause_it)
        self.Start_buttn.clicked.connect(self.start_test)



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
            baudrate=23400
            print(comport + ' @ ' + '%d' %baudrate)
            self.ser.port =comport
            self.ser.baudrate = baudrate
            self.ser.bytesize = serial.EIGHTBITS #number of bits per bytes
            self.ser.parity = serial.PARITY_NONE #set parity check
            self.ser.stopbits = serial.STOPBITS_ONE #number of stop bits

            self.ser.timeout = 0.3        #non-block read 0.5s
            self.ser.writeTimeout = 0.5     #timeout for write 0.5s
            self.ser.xonxoff = False    #disable software flow control
            self.ser.rtscts = False     #disable hardware (RTS/CTS) flow control
            self.ser.dsrdtr = False     #disable hardware (DSR/DTR) flow control
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
        

    def start_test(self):
        self.button_pause=True
        if self.device.connect(-1, 5000) == False:
            print('Error: ECG device is not connected')
            self.device.free()
            sys.exit()
        print('device is connected... ' + self.device.get_serial_number())
        send_str="okay"
        self.ser.write(send_str.encode())
        while 1:
                                if ser.inWaiting() > 0:
                                    result = ser.readline()   # Get OKEY and start to send ECG
                                    print(result)
                                    break     

            if(self.button_pause):
                print("still_in")
                QApplication.processEvents() 
            else:
                break

        # print('Stop')                                  
        # device.stop_output()
        # device.free() 
        # print('Start')                      
        # if device.connect(-1, 5000) == False:
        #     print('Error: ECG device is not connected')
        #     device.free()
        #     sys.exit()
        # print('device is connected... ' + device.get_serial_number())
        

        # ser.write(send_str.encode())
        # ################################################# Preparing data ###################################################### 
        # # file_path = 'C:/Users/Iris/Desktop/Nano_ADC_EXE/data-wrong/test.txt'
        # print('output whaleteq-format data...')
        # sys.stdout.flush()  
        # header = device.load_whaleteq_database(create_string_buffer(file_path.encode('ascii'))) 
        # sys.stdout.flush()  
        # ############################################### Stop  when click STOP ###################################################  
        # if self.stopCount%2 < 1:      # Stop loop when click STOP button      
        #     print('Stop')   
        #     device.free_ecg_header(header)        
        #     device.stop_output()
        #     device.free()  
        #     break
        
        # if not header:
        #     print('failed')
        #     device.free()
        #     sys.exit()
        # ################################################# Start sending ECG ######################################################                  
        # while 1:
        #     if ser.inWaiting() > 0:
        #         result = ser.readline()   # Get OKEY and start to send ECG
        #         print(result)
        #         break                        
        # device.output_waveform(0, None, None)   # Send ECG to simulator
        pass

# class SerialApp(QWidget):
#     def __init__(self):
#         super().__init__()
        
#         # Main layout
#         self.layout = QVBoxLayout()
        
#         # Label to display selected port
#         self.label = QLabel("Select a Serial Port:", self)
#         self.layout.addWidget(self.label)
        
#         # ComboBox to list serial ports
#         self.combo = QComboBox(self)
#         self.layout.addWidget(self.combo)
        
#         # Button to refresh the list of available serial ports
#         self.refresh_button = QPushButton("Refresh Ports", self)
#         self.refresh_button.clicked.connect(self.update_ports)
#         self.layout.addWidget(self.refresh_button)
        
#         # Button to connect to the selected serial port
#         self.connect_button = QPushButton("Connect", self)
#         self.connect_button.clicked.connect(self.connect_serial)
#         self.layout.addWidget(self.connect_button)
        
#         # Set layout and window title
#         self.setLayout(self.layout)
#         self.setWindowTitle('Serial Port Selector')

#         # Populate initial ports list
#         self.update_ports()

#     def update_ports(self):
#         """Updates the list of available serial ports."""
#         self.combo.clear()  # Clear the combo box
#         ports = serial.tools.list_ports.comports()
#         for port in ports:
#             self.combo.addItem(port.device)  # Add port name to combo box
    
#     def connect_serial(self):
#         """Handles the serial connection when the user selects a port."""
#         selected_port = self.combo.currentText()
#         if selected_port:
#             self.label.setText(f"Connecting to {selected_port}...")
#             # Add your serial connection logic here
#             try:
#                 self.serial_conn = serial.Serial(selected_port, 9600)  # Default baudrate
#                 self.label.setText(f"Connected to {selected_port}")
#             except Exception as e:
#                 self.label.setText(f"Failed to connect: {str(e)}")
#         else:
#             self.label.setText("No serial port selected!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GCBME_app()
    window.show()
    sys.exit(app.exec_())
