# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fatigue.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTime, QTimer, Qt
from pyqtgraph import PlotWidget, ViewBox, mkPen
from time import time
from datetime import timedelta
from winsound import MessageBeep
from csv import writer
from utilities import *

class Ui_Fatigue(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        super(Ui_Fatigue, self).__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)
    
    def setupUi(self, Fatigue):
        Fatigue.setObjectName("Fatigue")
        Fatigue.resize(1077, 739)
        Fatigue.setMinimumSize(QtCore.QSize(1050, 650))
        Fatigue.setMaximumSize(QtCore.QSize(16777215, 100000))
        self.gridLayout_2 = QtWidgets.QGridLayout(Fatigue)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(Fatigue)
        self.widget.setMinimumSize(QtCore.QSize(350, 449))
        self.widget.setMaximumSize(QtCore.QSize(350, 16777215))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title_label = QtWidgets.QLabel(self.widget)
        self.title_label.setMinimumSize(QtCore.QSize(0, 24))
        self.title_label.setMaximumSize(QtCore.QSize(16777215, 24))
        self.title_label.setObjectName("title_label")
        self.verticalLayout_2.addWidget(self.title_label)
        self.setting_label = QtWidgets.QLabel(self.widget)
        self.setting_label.setMinimumSize(QtCore.QSize(0, 24))
        self.setting_label.setMaximumSize(QtCore.QSize(16777215, 24))
        self.setting_label.setObjectName("setting_label")
        self.verticalLayout_2.addWidget(self.setting_label)
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.set_pulseWidth = QtWidgets.QDoubleSpinBox(self.frame)
        self.set_pulseWidth.setDecimals(1)
        self.set_pulseWidth.setMaximum(1000.0)
        self.set_pulseWidth.setProperty("value", 10.0)
        self.set_pulseWidth.setObjectName("set_pulseWidth")
        self.horizontalLayout_6.addWidget(self.set_pulseWidth)
        self.set_timeUnit = QtWidgets.QComboBox(self.frame)
        self.set_timeUnit.setMaximumSize(QtCore.QSize(41, 22))
        self.set_timeUnit.setObjectName("set_timeUnit")
        self.set_timeUnit.addItem("")
        self.set_timeUnit.addItem("")
        self.set_timeUnit.addItem("")
        self.horizontalLayout_6.addWidget(self.set_timeUnit)
        self.gridLayout.addLayout(self.horizontalLayout_6, 4, 2, 1, 1)
        self.nPulse_lable = QtWidgets.QLabel(self.frame)
        self.nPulse_lable.setObjectName("nPulse_lable")
        self.gridLayout.addWidget(self.nPulse_lable, 9, 1, 1, 1)
        self.set_pulseWidth_label = QtWidgets.QLabel(self.frame)
        self.set_pulseWidth_label.setObjectName("set_pulseWidth_label")
        self.gridLayout.addWidget(self.set_pulseWidth_label, 4, 1, 1, 1)
        self.read_voltage = QtWidgets.QDoubleSpinBox(self.frame)
        self.read_voltage.setDecimals(3)
        self.read_voltage.setMaximum(10.0)
        self.read_voltage.setSingleStep(0.1)
        self.read_voltage.setProperty("value", 0.1)
        self.read_voltage.setObjectName("read_voltage")
        self.gridLayout.addWidget(self.read_voltage, 7, 2, 1, 1)
        self.temperature = QtWidgets.QDoubleSpinBox(self.frame)
        self.temperature.setEnabled(False)
        self.temperature.setMaximum(600.0)
        self.temperature.setProperty("value", 300.0)
        self.temperature.setObjectName("temperature")
        self.gridLayout.addWidget(self.temperature, 12, 2, 1, 1)
        self.resetV_label = QtWidgets.QLabel(self.frame)
        self.resetV_label.setObjectName("resetV_label")
        self.gridLayout.addWidget(self.resetV_label, 5, 1, 1, 1)
        self.fname_label = QtWidgets.QLabel(self.frame)
        self.fname_label.setObjectName("fname_label")
        self.gridLayout.addWidget(self.fname_label, 1, 1, 1, 1)
        self.readV_label = QtWidgets.QLabel(self.frame)
        self.readV_label.setObjectName("readV_label")
        self.gridLayout.addWidget(self.readV_label, 7, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.resetV = QtWidgets.QDoubleSpinBox(self.frame)
        self.resetV.setDecimals(3)
        self.resetV.setMinimum(-5.0)
        self.resetV.setMaximum(5.0)
        self.resetV.setSingleStep(0.001)
        self.resetV.setProperty("value", 3.0)
        self.resetV.setObjectName("resetV")
        self.horizontalLayout_3.addWidget(self.resetV)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.reset_pulseWidth = QtWidgets.QDoubleSpinBox(self.frame)
        self.reset_pulseWidth.setDecimals(1)
        self.reset_pulseWidth.setMaximum(1000.0)
        self.reset_pulseWidth.setProperty("value", 50.0)
        self.reset_pulseWidth.setObjectName("reset_pulseWidth")
        self.horizontalLayout.addWidget(self.reset_pulseWidth)
        self.reset_timeUnit = QtWidgets.QComboBox(self.frame)
        self.reset_timeUnit.setMaximumSize(QtCore.QSize(41, 22))
        self.reset_timeUnit.setObjectName("reset_timeUnit")
        self.reset_timeUnit.addItem("")
        self.reset_timeUnit.addItem("")
        self.reset_timeUnit.addItem("")
        self.horizontalLayout.addWidget(self.reset_timeUnit)
        self.gridLayout.addLayout(self.horizontalLayout, 6, 2, 1, 1)
        self.setV_label = QtWidgets.QLabel(self.frame)
        self.setV_label.setObjectName("setV_label")
        self.gridLayout.addWidget(self.setV_label, 3, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.avg = QtWidgets.QSpinBox(self.frame)
        self.avg.setMaximumSize(QtCore.QSize(50, 20))
        self.avg.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.avg.setMinimum(1)
        self.avg.setMaximum(100)
        self.avg.setProperty("value", 5)
        self.avg.setObjectName("avg")
        self.horizontalLayout_4.addWidget(self.avg)
        self.avgread_label = QtWidgets.QLabel(self.frame)
        self.avgread_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.avgread_label.setObjectName("avgread_label")
        self.horizontalLayout_4.addWidget(self.avgread_label)
        self.gridLayout.addLayout(self.horizontalLayout_4, 8, 2, 1, 1)
        self.file_name = QtWidgets.QLineEdit(self.frame)
        self.file_name.setObjectName("file_name")
        self.gridLayout.addWidget(self.file_name, 1, 2, 1, 1)
        self.source = QtWidgets.QComboBox(self.frame)
        self.source.setEnabled(False)
        self.source.setAcceptDrops(False)
        self.source.setObjectName("source")
        self.source.addItem("")
        self.source.addItem("")
        self.gridLayout.addWidget(self.source, 2, 2, 1, 1)
        self.Ilimit_label = QtWidgets.QLabel(self.frame)
        self.Ilimit_label.setObjectName("Ilimit_label")
        self.gridLayout.addWidget(self.Ilimit_label, 10, 1, 1, 1)
        self.temp_check = QtWidgets.QCheckBox(self.frame)
        self.temp_check.setObjectName("temp_check")
        self.gridLayout.addWidget(self.temp_check, 12, 1, 1, 1)
        self.avg_label = QtWidgets.QLabel(self.frame)
        self.avg_label.setObjectName("avg_label")
        self.gridLayout.addWidget(self.avg_label, 8, 1, 1, 1)
        self.source_label = QtWidgets.QLabel(self.frame)
        self.source_label.setObjectName("source_label")
        self.gridLayout.addWidget(self.source_label, 2, 1, 1, 1)
        self.reset_pulseWidth_label = QtWidgets.QLabel(self.frame)
        self.reset_pulseWidth_label.setObjectName("reset_pulseWidth_label")
        self.gridLayout.addWidget(self.reset_pulseWidth_label, 6, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.setV = QtWidgets.QDoubleSpinBox(self.frame)
        self.setV.setDecimals(3)
        self.setV.setMinimum(-5.0)
        self.setV.setMaximum(5.0)
        self.setV.setSingleStep(0.1)
        self.setV.setProperty("value", -3.0)
        self.setV.setObjectName("setV")
        self.horizontalLayout_2.addWidget(self.setV)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 2, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.nPulses = connectedSpinBox(self.frame)
        self.nPulses.setMinimum(1)
        self.nPulses.setMaximum(9)
        self.nPulses.setProperty("value", 1)
        self.nPulses.setObjectName("nPulses")
        self.horizontalLayout_5.addWidget(self.nPulses)
        self.nPulse_unit = QtWidgets.QComboBox(self.frame)
        self.nPulse_unit.setObjectName("nPulse_unit")
        self.nPulse_unit.addItem("")
        self.nPulse_unit.addItem("")
        self.nPulse_unit.addItem("")
        self.nPulse_unit.addItem("")
        self.nPulse_unit.addItem("")
        self.nPulse_unit.addItem("")
        self.nPulse_unit.addItem("")
        self.nPulse_unit.addItem("")
        self.nPulse_unit.addItem("")
        self.horizontalLayout_5.addWidget(self.nPulse_unit)
        self.gridLayout.addLayout(self.horizontalLayout_5, 9, 2, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.iLimit = QtWidgets.QDoubleSpinBox(self.frame)
        self.iLimit.setDecimals(3)
        self.iLimit.setMinimum(-5.0)
        self.iLimit.setMaximum(5.0)
        self.iLimit.setSingleStep(0.001)
        self.iLimit.setProperty("value", 3.0)
        self.iLimit.setObjectName("iLimit")
        self.horizontalLayout_7.addWidget(self.iLimit)
        self.resistor = QtWidgets.QLabel(self.frame)
        self.resistor.setObjectName("resistor")
        self.horizontalLayout_7.addWidget(self.resistor)
        self.gridLayout.addLayout(self.horizontalLayout_7, 10, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        self.fatiguePlot = PlotWidget(Fatigue, viewBox=ViewBox(border=mkPen(color='k', width=2)))
        self.fatiguePlot.setBackground((255, 182, 193, 25))
        self.fatiguePlot.setMinimumSize(QtCore.QSize(411, 379))
        self.fatiguePlot.setObjectName("fatiguePlot")
        self.gridLayout_2.addWidget(self.fatiguePlot, 0, 1, 2, 1)
        self.widget1 = QtWidgets.QWidget(Fatigue)
        self.widget1.setMinimumSize(QtCore.QSize(350, 151))
        self.widget1.setMaximumSize(QtCore.QSize(350, 10000))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comment_checkBox = QtWidgets.QCheckBox(self.widget1)
        self.comment_checkBox.setObjectName("comment_checkBox")
        self.verticalLayout.addWidget(self.comment_checkBox)
        self.commentBox = QtWidgets.QTextEdit(self.widget1)
        self.commentBox.setEnabled(False)
        self.commentBox.setObjectName("commentBox")
        self.verticalLayout.addWidget(self.commentBox)
        self.timeTaken = QtWidgets.QLineEdit(self.widget1)
        self.timeTaken.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.timeTaken.setPalette(palette)
        self.timeTaken.setText("")
        self.timeTaken.setAlignment(QtCore.Qt.AlignCenter)
        self.timeTaken.setReadOnly(True)
        self.timeTaken.setObjectName("timeTaken")
        self.verticalLayout.addWidget(self.timeTaken)
        self.start_Button = QtWidgets.QPushButton(self.widget1)
        self.start_Button.setObjectName("start_Button")
        self.verticalLayout.addWidget(self.start_Button)
        self.abort_Button = QtWidgets.QPushButton(self.widget1)
        self.abort_Button.setObjectName("abort_Button")
        self.verticalLayout.addWidget(self.abort_Button)
        self.status = QtWidgets.QLineEdit(self.widget1)
        self.status.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.status.setPalette(palette)
        self.status.setText("")
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setReadOnly(True)
        self.status.setObjectName("status")
        self.verticalLayout.addWidget(self.status)
        self.gridLayout_2.addWidget(self.widget1, 1, 0, 1, 1)

        self.retranslateUi(Fatigue)
        self.set_timeUnit.setCurrentIndex(0)
        self.reset_timeUnit.setCurrentIndex(0)
        self.nPulse_unit.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Fatigue)
        Fatigue.setTabOrder(self.file_name, self.source)
        Fatigue.setTabOrder(self.source, self.setV)
        Fatigue.setTabOrder(self.setV, self.set_pulseWidth)
        Fatigue.setTabOrder(self.set_pulseWidth, self.set_timeUnit)
        Fatigue.setTabOrder(self.set_timeUnit, self.resetV)
        Fatigue.setTabOrder(self.resetV, self.reset_pulseWidth)
        Fatigue.setTabOrder(self.reset_pulseWidth, self.reset_timeUnit)
        Fatigue.setTabOrder(self.reset_timeUnit, self.read_voltage)
        Fatigue.setTabOrder(self.read_voltage, self.avg)
        Fatigue.setTabOrder(self.avg, self.nPulses)
        Fatigue.setTabOrder(self.nPulses, self.nPulse_unit)
        Fatigue.setTabOrder(self.nPulse_unit, self.iLimit)
        Fatigue.setTabOrder(self.iLimit, self.temp_check)
        Fatigue.setTabOrder(self.temp_check, self.temperature)
        Fatigue.setTabOrder(self.temperature, self.comment_checkBox)
        Fatigue.setTabOrder(self.comment_checkBox, self.commentBox)
        Fatigue.setTabOrder(self.commentBox, self.timeTaken)
        Fatigue.setTabOrder(self.timeTaken, self.start_Button)
        Fatigue.setTabOrder(self.start_Button, self.abort_Button)
        Fatigue.setTabOrder(self.abort_Button, self.status)

    def retranslateUi(self, Fatigue):
        _translate = QtCore.QCoreApplication.translate
        Fatigue.setWindowTitle(_translate("Fatigue", "Fatigue/Endurance"))
        self.title_label.setText(_translate("Fatigue", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#0000ff;\">Fatigue Test / Endurance Test</span></p></body></html>"))
        self.setting_label.setText(_translate("Fatigue", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#aa0000;\">Settings</span></p></body></html>"))
        self.set_timeUnit.setToolTip(_translate("Fatigue", "<html><head/><body><p>Select time unit. Time below 50 ms may not be reliable for Keithley 2450</p></body></html>"))
        self.set_timeUnit.setItemText(0, _translate("Fatigue", "µs"))
        self.set_timeUnit.setItemText(1, _translate("Fatigue", "ms"))
        self.set_timeUnit.setItemText(2, _translate("Fatigue", "s"))
        self.nPulse_lable.setText(_translate("Fatigue", "<html><head/><body><p><span style=\" font-size:10pt;\">Number of pulses</span></p></body></html>"))
        self.set_pulseWidth_label.setText(_translate("Fatigue", "<html><head/><body><p><span style=\" font-size:10pt;\">Set Pulse Width</span></p></body></html>"))
        self.temperature.setToolTip(_translate("Fatigue", "<html><head/><body><p>Temperature range will depend on the type of heater</p></body></html>"))
        self.resetV_label.setToolTip(_translate("Fatigue", "<html><head/><body><p>voltage for high resistance state</p></body></html>"))
        self.resetV_label.setText(_translate("Fatigue", "<html><head/><body><p><span style=\" font-size:10pt;\">Reset Voltage (V)</span></p></body></html>"))
        self.fname_label.setText(_translate("Fatigue", "<html><head/><body><p><span style=\" font-size:10pt;\">File Name</span></p></body></html>"))
        self.readV_label.setText(_translate("Fatigue", "<html><head/><body><p><span style=\" font-size:10pt;\">Read Voltage (V)</span></p></body></html>"))
        self.resetV.setToolTip(_translate("Fatigue", "<html><head/><body><p>HRS</p></body></html>"))
        self.reset_timeUnit.setToolTip(_translate("Fatigue", "<html><head/><body><p>Select time unit. Time below 50 ms may not be reliable for Keithley 2450</p></body></html>"))
        self.reset_timeUnit.setItemText(0, _translate("Fatigue", "µs"))
        self.reset_timeUnit.setItemText(1, _translate("Fatigue", "ms"))
        self.reset_timeUnit.setItemText(2, _translate("Fatigue", "s"))
        self.setV_label.setToolTip(_translate("Fatigue", "<html><head/><body><p>Voltage for low resistance state</p></body></html>"))
        self.setV_label.setText(_translate("Fatigue", "<html><head/><body><p><span style=\" font-size:10pt;\">Set Voltage (V)</span></p></body></html>"))
        self.avgread_label.setText(_translate("Fatigue", "<html><head/><body><p><span style=\" font-size:10pt;\">Readings</span></p></body></html>"))
        self.file_name.setText(_translate("Fatigue", "Sample_Fatigue"))
        self.source.setItemText(0, _translate("Fatigue", "Keysight B2902B"))
        self.source.setItemText(1, _translate("Fatigue", "Tektronix AFG1022"))
        self.Ilimit_label.setText(_translate("Fatigue", "<html><head/><body><p><span style=\" font-size:10pt;\">Current Limit (mA)</span></p></body></html>"))
        self.temp_check.setToolTip(_translate("Fatigue", "<html><head/><body><p>Use temperature only if temperature controller is attached</p></body></html>"))
        self.temp_check.setText(_translate("Fatigue", "Temperature (K)"))
        self.avg_label.setText(_translate("Fatigue", "<html><head/><body><p><span style=\" font-size:10pt;\">Average over</span></p></body></html>"))
        self.source_label.setText(_translate("Fatigue", "<html><head/><body><p><span style=\" font-size:10pt;\">Voltage Source</span></p></body></html>"))
        self.reset_pulseWidth_label.setText(_translate("Fatigue", "<html><head/><body><p><span style=\" font-size:10pt;\">Reset Pulse width</span></p></body></html>"))
        self.setV.setToolTip(_translate("Fatigue", "<html><head/><body><p>LRS</p></body></html>"))
        self.nPulse_unit.setItemText(0, _translate("Fatigue", "x10^2"))
        self.nPulse_unit.setItemText(1, _translate("Fatigue", "x10^3"))
        self.nPulse_unit.setItemText(2, _translate("Fatigue", "x10^4"))
        self.nPulse_unit.setItemText(3, _translate("Fatigue", "x10^5"))
        self.nPulse_unit.setItemText(4, _translate("Fatigue", "x10^6"))
        self.nPulse_unit.setItemText(5, _translate("Fatigue", "x10^7"))
        self.nPulse_unit.setItemText(6, _translate("Fatigue", "x10^8"))
        self.nPulse_unit.setItemText(7, _translate("Fatigue", "x10^9"))
        self.nPulse_unit.setItemText(8, _translate("Fatigue", "x10^10"))
        self.iLimit.setToolTip(_translate("Fatigue", "<html><head/><body><p>HRS</p></body></html>"))
        self.resistor.setText(_translate("Fatigue", "~ 1 kΩ"))
        self.comment_checkBox.setText(_translate("Fatigue", "Add Comments"))
        self.start_Button.setToolTip(_translate("Fatigue", "<html><head/><body><p>Click to start the experiment</p></body></html>"))
        self.start_Button.setText(_translate("Fatigue", "Start Measurement"))
        self.abort_Button.setToolTip(_translate("Fatigue", "<html><head/><body><p>Click to abort the experiment</p></body></html>"))
        self.abort_Button.setText(_translate("Fatigue", "Abort"))

class app_Fatigue(Ui_Fatigue):
    """The Switch app module."""
    
    def __init__(self, parent=None, smu = None, k2700 = None, afg1022 = None, sName="Sample_Fatigue", connection=1):
        super(app_Fatigue, self).__init__(parent)
        self.parent = parent
        self.smu = smu
        self.k2700 = k2700
        self.afg1022 = afg1022
        self.connection = connection
        disableScreen = False
        if self.afg1022 and self.smu:
            if self.afg1022.ID == 'Fake':
                self.source.removeItem(1) # Remove AFG source option
                if self.smu.ID == 'K2450':
                    disableScreen = True
            if self.smu.ID == 'Fake':
                disableScreen = True
        elif not self.smu:
            disableScreen = True
        elif not self.afg1022:
            self.source.removeItem(1) # Remove AFG source option
            if self.smu.ID == 'K2450':
                disableScreen = True
        if disableScreen:
            self.widget.setEnabled(False)
            self.status.setText("Required instruments not connected. Reconnect and try again.")
            self.widget1.setEnabled(False)
            self.fatiguePlot.setEnabled(False)                
        self.stopCall = False
        self.start_Button.clicked.connect(self.startFatigue)
        self.abort_Button.clicked.connect(self.abortFatigue)
        self.start_Button.setShortcut('ctrl+Return')
        self.abort_Button.setShortcut('ctrl+q')
        self.set_pulseWidth.setMinimum(0.1)
        self.reset_pulseWidth.setMinimum(0.1)
        self.initialize_plot()
        self.smu.nplc = 1
        self.smu.avg = 5
        self.smu.readV = 0.1
        self.filename = sName
        self.file_name.setText(self.filename)
        self.measurement_status = "Idle"
        self.file_name.setReadOnly(True)
        self.nPulses.setWrapping(True)
        self.iLimit.valueChanged.connect(self.update_resistor)
        self.setV.valueChanged.connect(self.update_resistor)
        self.resetV.valueChanged.connect(self.update_resistor)
        self.nPulses.editingFinished.connect(self.update_total_time)
        self.nPulse_unit.currentIndexChanged.connect(self.update_total_time)
        self.set_pulseWidth.valueChanged.connect(self.update_total_time)
        self.reset_pulseWidth.valueChanged.connect(self.update_total_time)
        self.set_timeUnit.currentIndexChanged.connect(self.update_total_time)
        self.reset_timeUnit.currentIndexChanged.connect(self.update_total_time)
        self.update_resistor()
        self.update_total_time()
        self.nPulses.hasWrapped.message.connect(lambda value: self.update_time_unit(value)) # not working, seems to be some version incompatibility problem
        self.ratio = 1.5
        self.params = {
            "Vset": 3,
            "setPwidth": 10,
            "set_timeUnit": 1,  # 0 = us, 1=ms, 2 = s
            "Vreset": -3,
            "resetPwidth": 10,
            "reset_timeUnit": 1,  # 0 = us, 1=ms, 2 = s
            "Rvoltage": 0.1,  # V
            "Average": 5,
            "nPulses": 1,
            "pulseUnit": 3,
            "ILimit": 1/1000,
            "temperature": 300,
            "temp_check": 0,
            "comments" : ""}
        self.parameters = list(self.params.values())[:-1]
        self.comment_checkBox.stateChanged.connect(self.updateCommentBox)
    
    def updateCommentBox(self):
        if self.comment_checkBox.isChecked():
            self.commentBox.setEnabled(True)
        else:
            self.commentBox.setEnabled(False)
    
    def update_resistor(self):
        limiting_current = self.iLimit.value()
        max_applied_voltage = max(abs(self.setV.value()),abs(self.resetV.value()))
        self.resistance = round(max_applied_voltage/limiting_current,2)
        self.resistor.setText("~ {} kΩ".format(self.resistance))
    
    def update_total_time(self):
        self.configurePulse()
        total_time = self.points[-1]*(self.setTimestep+self.resetTimestep)
        total_Qtime = QTime(0,0,0)
        total_Qtime = total_Qtime.addSecs(int(total_time))
        if total_time < 86399:
            self.timeTaken.setText("Total experiment time: {}".format(total_Qtime.toString("h:mm:ss")))
        else:
            days = int(total_time/86400)
            hours = int((total_time/86400 - days)*24)
            minutes = int(((total_time/86400 - days)*24 - hours)*60)
            if days == 1:
                daytext = "day"
            else:
                daytext = "days"
            if hours == 1:
                hourtext = "Hour"
            else:
                hourtext = "Hours"
            if minutes == 1:
                mintext = "Min"
            else:
                mintext = "Mins"
            self.timeTaken.setText("Total experiment time: {0} {3}, {1} {4}, {2} {5}.".format(days,hours,minutes,daytext,hourtext,mintext))
        
    def update_time_unit(self, factor):
        currentIndex = self.nPulse_unit.currentIndex()
        if factor == -1 and currentIndex > 0:
            self.nPulse_unit.setCurrentIndex(currentIndex+factor)
        elif factor == 1 and currentIndex < 8:
            self.nPulse_unit.setCurrentIndex(currentIndex+factor)
        elif factor == -1 and currentIndex == 0:
            self.nPulses.setValue(1)
        elif factor == 1 and currentIndex == 8:
            self.nPulses.setValue(9)
    
    def load_parameters(self):
        try:
            self.setV.setValue(self.parameters[0]),
            self.set_pulseWidth.setValue(self.parameters[1]),
            self.set_timeUnit.setCurrentIndex(self.parameters[2]),
            self.resetV.setValue(self.parameters[3]),
            self.reset_pulseWidth.setValue(self.parameters[4]),
            self.reset_timeUnit.setCurrentIndex(self.parameters[5]),
            self.read_voltage.setValue(self.parameters[6]),
            self.avg.setValue(self.parameters[7]),
            self.nPulses.setValue(self.parameters[8]),
            self.nPulse_unit.setCurrentIndex(self.parameters[9]),
            self.iLimit.setValue(self.parameters[10]*1000),
            self.temperature.setValue(self.parameters[11]),
            self.temp_check.setChecked(self.parameters[12])
        except Exception as e:
            print(f"Problem with loading fatigue parameters. {e}")
            print("Deleting parameter file from the folder may resolve the issue.")
    
    def configurePulse(self):
        """
        Configure the pulse parameters.

        Returns
        -------
        None.

        """
        maincomment = self.parent.commentBox.toPlainText()
        wholeComment = maincomment + '\n' + self.commentBox.toPlainText()
        formattedComment = ""
        for t in wholeComment.split('\n'):
            formattedComment += '## ' + t + '\n'
        self.params = {
            "Vset": self.setV.value(),
            "setPwidth": self.set_pulseWidth.value(),
            "set_timeUnit": self.set_timeUnit.currentIndex(),
            "Vreset": self.resetV.value(),
            "resetPwidth": self.reset_pulseWidth.value(),
            "reset_timeUnit": self.reset_timeUnit.currentIndex(),
            "Rvoltage": self.read_voltage.value(),
            "Average": self.avg.value(),
            "nPulses": self.nPulses.value(),
            "pulseUnit": self.nPulse_unit.currentIndex(),
            "ILimit": self.iLimit.value()/1000,
            "temperature": self.temperature.value(),
            "temp_check": int(self.temp_check.isChecked()),
            "comments" : formattedComment}
        self.parameters = list(self.params.values())[:-1]
        self.smu.avg = self.params["Average"]
        self.smu.readV = self.params["Rvoltage"]
        if self.params["set_timeUnit"] == 0:
            self.setTimestep = self.params["setPwidth"]*1e-6
        elif self.params["set_timeUnit"] == 1:
            self.setTimestep = self.params["setPwidth"]*1e-3
        elif self.params["set_timeUnit"] == 2:
            self.setTimestep = self.params["setPwidth"]
        if self.params["reset_timeUnit"] == 0:
            self.resetTimestep = self.params["resetPwidth"]*1e-6
        elif self.params["reset_timeUnit"] == 1:
            self.resetTimestep = self.params["resetPwidth"]*1e-3
        elif self.params["reset_timeUnit"] == 2:
            self.resetTimestep = self.params["resetPwidth"]
        if self.params["pulseUnit"] == 0:
            self.nPulse_order = 1e2
        elif self.params["pulseUnit"] == 1:
            self.nPulse_order = 1e3
        elif self.params["pulseUnit"] == 2:
            self.nPulse_order = 1e4
        elif self.params["pulseUnit"] == 3:
            self.nPulse_order = 1e5
        elif self.params["pulseUnit"] == 4:
            self.nPulse_order = 1e6
        elif self.params["pulseUnit"] == 5:
            self.nPulse_order = 1e7
        elif self.params["pulseUnit"] == 6:
            self.nPulse_order = 1e8
        elif self.params["pulseUnit"] == 7:
            self.nPulse_order = 1e9
        elif self.params["pulseUnit"] == 8:
            self.nPulse_order = 1e10
        self.points = linlogspace(self.nPulse_order*self.params["nPulses"])
        self.fpoints = getBinnedPoints(self.points)
        self.number_of_points = len(self.fpoints)
                
    def initialize_SMU_and_AFG(self):
        """
        Initialize the SMU.

        Returns
        -------
        None.

        """
        if self.setTimestep != self.resetTimestep:
            x = int(8000*self.setTimestep/(self.setTimestep+self.resetTimestep))
            self.afg1022.configure_user7(x)
            waitFor(2000) # wait for 2 seconds for new pulse to be written
        self.smu.apply_voltage(compliance_current=self.params["ILimit"])
        self.smu.set_wire_configuration(2) # two wire configuration
        self.smu.display_light(state ='ON', percent = 25)
        self.smu.set_read_back_on()
        self.smu.measure_current()
        self.smu.set_simple_loop(self.params["Average"])
        self.smu.source_voltage = self.params["Rvoltage"]
        connect_sample_with_AFG(self.k2700, self.connection)

    def pulseMeasure_AFG(self):
        """
        Apply n pulses from AFG and measure resistance from SMU.

        Returns
        -------
        current set, reset resistances.

        """
        self.afg1022.setNPulses(self.params['Vset'],
                                self.setTimestep,
                                self.params['Vreset'],
                                self.resetTimestep,
                                self.fpoints[self.i])
        self.afg1022.trgNwait()
        LRScurrent, HRScurrent = self.read_LRS_HRS_states()
        LRS, HRS = self.params['Rvoltage']/LRScurrent, self.params['Rvoltage']/HRScurrent
        self.ncycles.append(self.points[self.i])
        self.LRScurrents.append(LRScurrent)
        self.LRS.append(LRS)
        self.HRScurrents.append(HRScurrent)
        self.HRS.append(HRS)
               
        self.data_lineHRS.setData(self.ncycles, self.HRS)
        self.data_lineLRS.setData(self.ncycles, self.LRS)
        
        self.i = self.i + 1
        # if ratio between HRS & LRS is less than 1.5, then sample is considered to have failed.
        """
        if HRS/LRS < 1.5: # stop program if sample has stopped switching
            # sometimes, sample starts behaving in opposite manner after some cycles. 
            # Program will continue experiment, if that happens.
            if LRS/HRS < 1.5:
                print("HRS = {0}, LRS = {1}".format(HRS,LRS))
                self.stopCall = True
                title = "Sample Failed!"
                text = "Sample is not showing resistive switching anymore! Please change sample or measurement paramters."
                QMessageBox.critical(self,title,text)
        """
        if self.i >= self.number_of_points or self.stopCall:
            self.stop_program()
            return
        
        if self.connection == 1:
            self.k2700.close_Channels(AFG) # connect function generator for next set of cycles
        elif self.connection == 2:
            self.k2700.close_Channels(AFG+10)
        waitFor(20) # wait for 20msec to ensure switching is complete
        self.timer.singleShot(0, self.pulseMeasure_AFG)  # Measure next pulse    

    def startFatigue(self):
        """
        Begins the fatigue experiment.

        Returns
        -------
        None.

        """
        title = "Confirm resistance."
        text = "Is resistor of {} kΩ connected?".format(self.resistance)
        reply = QMessageBox.question(self, title,text,QMessageBox.Yes,QMessageBox.No)
        if reply == QMessageBox.No:
            return
        self.stopCall = False
        self.measurement_status = "Running"
        self.status.setText("Program Running..")
        self.i = 0
        self.configurePulse()
        self.initialize_SMU_and_AFG()
        self.smu.enable_source()
        startTime = time()
        LRScurrent,HRScurrent = self.read_LRS_HRS_states()
        endTime = time()
        self.readingTime = endTime - startTime
        self.totalTime = self.points[-1]*(self.setTimestep+self.resetTimestep) + self.readingTime*self.number_of_points
        self.timeTaken.setText("Total experiment time: {}".format(str(timedelta(seconds=int(self.totalTime)))))
        LRS, HRS = self.params['Rvoltage']/LRScurrent, self.params['Rvoltage']/HRScurrent
        
        self.ncycles = [1] # log plot cannot have 0 in its axis
        self.LRScurrents = [LRScurrent]
        self.LRS = [LRS]
        self.HRScurrents = [HRScurrent]
        self.HRS = [HRS]
        """
        if abs(HRS/LRS) < 1.5 and abs(LRS/HRS) < 1.5:
            self.stopCall = True
            print("HRS = {0}, LRS = {1}".format(HRS,LRS))
            title = "Sample Failed!"
            text = "Sample does not show resistive switching! Please change measurement parameters, or change sample."
            QMessageBox.critical(self,title,text)
            self.stop_program()
            return
        
        if HRS < LRS:
            self.params['Vset'] = self.params['Vreset']
            self.params['Vreset'] = self.setV.value()
            self.setV.setValue(self.params['Vset'])
            self.resetV.setValue(self.params['Vreset'])
            title = "Parameter change notice!"
            text = "Vset and Vreset has been interchanged as required."
            QMessageBox.warning(self,title,text)
        """
        pen1 = mkPen(color=(0, 0, 255), width=2)
        pen2 = mkPen(color=(255, 0, 0), width=2)
        self.data_lineLRS = self.fatiguePlot.plot(self.ncycles, self.LRS, pen=pen1, symbol='x', symbolPen='r')
        self.data_lineHRS = self.fatiguePlot.plot(self.ncycles, self.HRS, pen=pen2, symbol='o')
        del self.ncycles[0]
        del self.LRS[0]
        del self.HRS[0]
        self.timer = QTimer()
        self.start_Button.setEnabled(False)
        self.abort_Button.setEnabled(True)
        self.timer.singleShot(0, self.pulseMeasure_AFG)

    def read_LRS_HRS_states(self):
        # Assuming function generator is connected and SMU is disconnected
        
        # Get LRS
        self.afg1022.setSinglePulse(self.params['Vset'],self.setTimestep)
        self.afg1022.trgNwait()
        if self.connection == 1:
            self.k2700.open_Channels(AFG) # disconnect function generator
            self.k2700.close_Channels(SMU) # connect SMU
        elif self.connection == 2:
            self.k2700.open_Channels(AFG+10) # disconnect function generator
            self.k2700.close_Channels(SMU+10) # connect SMU
        waitFor(20) # wait for 20msec to ensure switching is complete
        # Measure Read resistance using smu
        LRScurrent = self.smu.readReRAM()
        
        # Get HRS        
        if self.connection == 1:
            self.k2700.open_Channels(SMU) # disconnect SMU
            self.k2700.close_Channels(AFG) # connect function generator
        elif self.connection == 2:
            self.k2700.open_Channels(SMU+10) # disconnect SMU
            self.k2700.close_Channels(AFG+10) # connect function generator
        waitFor(20) # wait for 20msec to ensure switching is complete
        self.afg1022.setSinglePulse(self.params['Vreset'],self.resetTimestep)
        self.afg1022.trgNwait()
        if self.connection == 1:
            self.k2700.open_Channels(AFG) # disconnect function generator
            self.k2700.close_Channels(SMU) # connect SMU
        elif self.connection == 2:
            self.k2700.open_Channels(AFG+10) # disconnect function generator
            self.k2700.close_Channels(SMU+10) # connect SMU
        waitFor(20) # wait for 20msec to ensure switching is complete
        # Measure Read resistance using smu
        HRScurrent = self.smu.readReRAM()
        if self.connection == 1:
            self.k2700.open_Channels(SMU) # disconnect SMU
            self.k2700.close_Channels(AFG) # connect function generator
        elif self.connection == 2:
            self.k2700.open_Channels(SMU+10) # disconnect SMU
            self.k2700.close_Channels(AFG+10) # connect function generator
        waitFor(20) # wait for 20msec to ensure switching is complete
        return LRScurrent, HRScurrent
        
    def stop_program(self):
        self.saveData()
        if self.stopCall:
            self.measurement_status = "Aborted"
            self.status.setText("Program Aborted. Partial data saved if available.")
        else:
            self.measurement_status = "Idle"
            self.status.setText("Measurement Finished. Data saved.")
        self.start_Button.setEnabled(True)
        self.abort_Button.setEnabled(False)
        self.smu.source_voltage = 0
        self.smu.disable_source()
        MessageBeep()
    
    def abortFatigue(self):
        self.status.setText("Aborting the program. Please wait..")
        self.abort_Button.setEnabled(False)
        self.stopCall = True
        
    def saveData(self):
        """
        Save the data to file.

        Returns
        -------
        None.

        """
        self.fullfilename = unique_filename(directory='.', prefix=self.filename, datetimeformat="", ext='dat')
        with open(self.fullfilename, "w", newline='') as f:
            if self.source.currentText() == 'Keysight B2902B':
                f.write("##Pulse voltage source: Keysight B2902B SMU.\n")
            elif self.source.currentText() == 'Tektronix AFG1022':
                f.write("##Pulse voltage source: Tektronix AFG1022 MultiFunction Generator.\n")
            f.write("##Resistance read using Keithley 2450 source-measure unit.\n")
            f.write(f"## Date & Time: {datetime.now().strftime('%m/%d/%Y; %H:%M:%S')}\n")
            f.write("##Set voltage = {0}, Reset Voltage = {1}.\n".format(self.params["Vset"],self.params["Vreset"]))
            f.write("##Set pulse width = {0}s, Reset pulse width = {1}s\n".format(self.setTimestep,self.resetTimestep))
            f.write("##Read voltage = {0}V, averaged over {1} readings\n".format(self.params["Rvoltage"],self.params["Average"]))
            f.write("##Limiting current = {}mA\n".format(self.iLimit.value()))
            f.write(self.params["comments"])
            f.write("#NCycles\t LRS current (A)\t HRS Current\t LRS resistance (Ω)\t HRS resistance (Ω)\n")
            write_data = writer(f, delimiter = '\t')
            write_data.writerows(zip(self.ncycles, self.LRScurrents, 
                                     self.HRScurrents,self.LRS,self.HRS))
            
    def initialize_plot(self):
        """
        Initialize the plot before starting the measurement.

        Returns
        -------
        None.

        """
        styles = {'color': 'r', 'font-size': '20px'}
        self.fatiguePlot.setLabel('left', 'Read Resistance (Ohms)', **styles)
        self.fatiguePlot.setLabel('bottom', 'N. cycles', **styles)
        self.fatiguePlot.getPlotItem().setLogMode(True, True)
        self.fatiguePlot.addLegend()
    
    def keyPressEvent(self, event):
        """Close application from escape key.

        results in QMessageBox dialog from closeEvent, good but how/why?
        """
        if event.key() == Qt.Key_Escape:
            self.close()
    
    def closeEvent(self, event):
        """
        Perform necessary operations just before exiting the program.

        Parameters
        ----------
        event : QCloseEvent

        Returns
        -------
        None.

        """
        reply = QMessageBox.Yes
        if self.measurement_status == "Running":
            quit_msg = "Measurement is in Progress. Are you sure you want to stop and exit?"
            reply = QMessageBox.question(self, 'Message', 
                     quit_msg, QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.stopCall = True
        if reply == QMessageBox.Yes:
            if __name__ != "__main__":
                self.parent.show()
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fatigue = QtWidgets.QWidget()
    smu, k2700, afg1022 = checkInstrument(test = True)
    ui = app_Fatigue(Fatigue, smu, k2700, afg1022)
    ui.show()
    app.exec_()
    app.quit()

