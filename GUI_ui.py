# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\WTMH\Static_project\GCBME_GUI\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(959, 529)
        MainWindow.setMinimumSize(QtCore.QSize(10, 10))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.Serial_item = ComboBox(self.groupBox)
        self.Serial_item.setObjectName("Serial_item")
        self.horizontalLayout.addWidget(self.Serial_item)
        self.Serial_buttn = QtWidgets.QPushButton(self.groupBox)
        self.Serial_buttn.setObjectName("Serial_buttn")
        self.horizontalLayout.addWidget(self.Serial_buttn)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.ECG_device_box = QtWidgets.QComboBox(self.groupBox)
        self.ECG_device_box.setObjectName("ECG_device_box")
        self.ECG_device_box.addItem("")
        self.ECG_device_box.addItem("")
        self.horizontalLayout.addWidget(self.ECG_device_box)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.data_path = QtWidgets.QLineEdit(self.groupBox)
        self.data_path.setObjectName("data_path")
        self.horizontalLayout.addWidget(self.data_path)
        self.data_buttn = QtWidgets.QPushButton(self.groupBox)
        self.data_buttn.setObjectName("data_buttn")
        self.horizontalLayout.addWidget(self.data_buttn)
        self.Start_buttn = QtWidgets.QPushButton(self.groupBox)
        self.Start_buttn.setObjectName("Start_buttn")
        self.horizontalLayout.addWidget(self.Start_buttn)
        self.pause_resume = QtWidgets.QPushButton(self.groupBox)
        self.pause_resume.setObjectName("pause_resume")
        self.horizontalLayout.addWidget(self.pause_resume)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.Terminal_result = QtWidgets.QTextEdit(self.groupBox_2)
        self.Terminal_result.setReadOnly(True)
        self.Terminal_result.setObjectName("Terminal_result")
        self.verticalLayout.addWidget(self.Terminal_result)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.Final_result = QtWidgets.QTextEdit(self.groupBox_2)
        self.Final_result.setReadOnly(True)
        self.Final_result.setObjectName("Final_result")
        self.verticalLayout_2.addWidget(self.Final_result)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.Group_name = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.Group_name.setObjectName("Group_name")
        self.verticalLayout_4.addWidget(self.Group_name)
        self.Export_result = QtWidgets.QPushButton(self.groupBox_3)
        self.Export_result.setObjectName("Export_result")
        self.verticalLayout_4.addWidget(self.Export_result)
        self.verticalLayout_4.setStretch(1, 7)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 5)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Data setting"))
        self.label.setText(_translate("MainWindow", "Comport"))
        self.Serial_buttn.setText(_translate("MainWindow", "Connect board"))
        self.label_6.setText(_translate("MainWindow", "ECG device"))
        self.ECG_device_box.setItemText(0, _translate("MainWindow", "AECG100"))
        self.ECG_device_box.setItemText(1, _translate("MainWindow", "SECG50"))
        self.label_2.setText(_translate("MainWindow", "Data folder"))
        self.data_buttn.setText(_translate("MainWindow", "Browse"))
        self.Start_buttn.setText(_translate("MainWindow", "Start"))
        self.pause_resume.setText(_translate("MainWindow", "Pause"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Result"))
        self.label_3.setText(_translate("MainWindow", "Terminal result"))
        self.label_4.setText(_translate("MainWindow", "Final Result"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Expot Result"))
        self.label_5.setText(_translate("MainWindow", "Group Name"))
        self.Export_result.setText(_translate("MainWindow", "Export"))
from API import ComboBox
