# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'retention.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
# 
# WARNING! All changes made in this file will be lost!

# TODO: Add tooltips
# TODO: Verify pulse application with SMU

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTime, QTimer
from time import time
from pyqtgraph import PlotWidget, ViewBox, mkPen
from os.path import exists as fileExists
from winsound import MessageBeep
from csv import writer
from utilities import linlogspace, SMU, AFG, waitFor
from utilities import connect_sample_with_AFG, unique_filename, checkInstrument
from utilities import MyTimeEdit, connect_sample_with_SMU, connect_sample_with_AFG, getBinnedPoints

class Ui_Retention(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        super(Ui_Retention, self).__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)
    
    def setupUi(self, Retention):
        Retention.setObjectName("Retention")
        Retention.resize(1050, 616)
        Retention.setMinimumSize(QtCore.QSize(1050, 550))
        self.gridLayout_2 = QtWidgets.QGridLayout(Retention)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Retention)
        self.groupBox.setMinimumSize(QtCore.QSize(222, 211))
        self.groupBox.setMaximumSize(QtCore.QSize(293, 600))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Program_label = QtWidgets.QLabel(self.groupBox)
        self.Program_label.setMinimumSize(QtCore.QSize(0, 24))
        self.Program_label.setObjectName("Program_label")
        self.verticalLayout_2.addWidget(self.Program_label)
        self.setting_label = QtWidgets.QLabel(self.groupBox)
        self.setting_label.setMinimumSize(QtCore.QSize(0, 24))
        self.setting_label.setObjectName("setting_label")
        self.verticalLayout_2.addWidget(self.setting_label)
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.setPwidth = QtWidgets.QDoubleSpinBox(self.frame)
        self.setPwidth.setDecimals(1)
        self.setPwidth.setProperty("value", 1.0)
        self.setPwidth.setObjectName("setPwidth")
        self.horizontalLayout.addWidget(self.setPwidth)
        self.setTimeUnit = QtWidgets.QComboBox(self.frame)
        self.setTimeUnit.setMaximumSize(QtCore.QSize(41, 22))
        self.setTimeUnit.setObjectName("setTimeUnit")
        self.setTimeUnit.addItem("")
        self.setTimeUnit.addItem("")
        self.setTimeUnit.addItem("")
        self.horizontalLayout.addWidget(self.setTimeUnit)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.avg = QtWidgets.QSpinBox(self.frame)
        self.avg.setWrapping(True)
        self.avg.setAlignment(QtCore.Qt.AlignCenter)
        self.avg.setMinimum(1)
        self.avg.setMaximum(100)
        self.avg.setProperty("value", 5)
        self.avg.setObjectName("avg")
        self.horizontalLayout_3.addWidget(self.avg)
        self.points_label = QtWidgets.QLabel(self.frame)
        self.points_label.setObjectName("points_label")
        self.horizontalLayout_3.addWidget(self.points_label)
        self.gridLayout.addLayout(self.horizontalLayout_3, 13, 1, 1, 1)
        self.readVoltage_label = QtWidgets.QLabel(self.frame)
        self.readVoltage_label.setObjectName("readVoltage_label")
        self.gridLayout.addWidget(self.readVoltage_label, 12, 0, 1, 1)
        self.read_voltage = QtWidgets.QDoubleSpinBox(self.frame)
        self.read_voltage.setProperty("value", 0.1)
        self.read_voltage.setObjectName("read_voltage")
        self.gridLayout.addWidget(self.read_voltage, 12, 1, 1, 1)
        self.temperature = QtWidgets.QDoubleSpinBox(self.frame)
        self.temperature.setEnabled(False)
        self.temperature.setMaximum(600.0)
        self.temperature.setProperty("value", 300.0)
        self.temperature.setObjectName("temperature")
        self.gridLayout.addWidget(self.temperature, 14, 1, 1, 1)
        self.Ilimit_label = QtWidgets.QLabel(self.frame)
        self.Ilimit_label.setObjectName("Ilimit_label")
        self.gridLayout.addWidget(self.Ilimit_label, 10, 0, 1, 1)
        self.temp_check = QtWidgets.QCheckBox(self.frame)
        self.temp_check.setObjectName("temp_check")
        self.gridLayout.addWidget(self.temp_check, 14, 0, 1, 1)
        self.resetV_label = QtWidgets.QLabel(self.frame)
        self.resetV_label.setObjectName("resetV_label")
        self.gridLayout.addWidget(self.resetV_label, 4, 0, 1, 1)
        self.setV_label = QtWidgets.QLabel(self.frame)
        self.setV_label.setObjectName("setV_label")
        self.gridLayout.addWidget(self.setV_label, 2, 0, 1, 1)
        self.vsource = QtWidgets.QComboBox(self.frame)
        self.vsource.setObjectName("vsource")
        self.vsource.addItem("")
        self.vsource.addItem("")
        self.gridLayout.addWidget(self.vsource, 1, 1, 1, 1)
        self.file_name = QtWidgets.QLineEdit(self.frame)
        self.file_name.setObjectName("file_name")
        self.gridLayout.addWidget(self.file_name, 0, 1, 1, 1)
        self.source_label = QtWidgets.QLabel(self.frame)
        self.source_label.setObjectName("source_label")
        self.gridLayout.addWidget(self.source_label, 1, 0, 1, 1)
        self.fname_label = QtWidgets.QLabel(self.frame)
        self.fname_label.setObjectName("fname_label")
        self.gridLayout.addWidget(self.fname_label, 0, 0, 1, 1)
        self.average_label = QtWidgets.QLabel(self.frame)
        self.average_label.setObjectName("average_label")
        self.gridLayout.addWidget(self.average_label, 13, 0, 1, 1)
        self.setPwidth_label = QtWidgets.QLabel(self.frame)
        self.setPwidth_label.setObjectName("setPwidth_label")
        self.gridLayout.addWidget(self.setPwidth_label, 3, 0, 1, 1)
        self.resetPwidth_label = QtWidgets.QLabel(self.frame)
        self.resetPwidth_label.setObjectName("resetPwidth_label")
        self.gridLayout.addWidget(self.resetPwidth_label, 7, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.resetPwidth = QtWidgets.QDoubleSpinBox(self.frame)
        self.resetPwidth.setWrapping(False)
        self.resetPwidth.setDecimals(1)
        self.resetPwidth.setProperty("value", 1.0)
        self.resetPwidth.setObjectName("resetPwidth")
        self.horizontalLayout_2.addWidget(self.resetPwidth)
        self.resetTimeUnit = QtWidgets.QComboBox(self.frame)
        self.resetTimeUnit.setMaximumSize(QtCore.QSize(41, 22))
        self.resetTimeUnit.setObjectName("resetTimeUnit")
        self.resetTimeUnit.addItem("")
        self.resetTimeUnit.addItem("")
        self.resetTimeUnit.addItem("")
        self.horizontalLayout_2.addWidget(self.resetTimeUnit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 1, 1, 1)
        self.time_label = QtWidgets.QLabel(self.frame)
        self.time_label.setObjectName("time_label")
        self.gridLayout.addWidget(self.time_label, 11, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.setV = QtWidgets.QDoubleSpinBox(self.frame)
        self.setV.setMinimumSize(QtCore.QSize(115, 0))
        self.setV.setDecimals(3)
        self.setV.setMinimum(-5.0)
        self.setV.setMaximum(5.0)
        self.setV.setSingleStep(0.001)
        self.setV.setProperty("value", -3.0)
        self.setV.setObjectName("setV")
        self.horizontalLayout_4.addWidget(self.setV)
        self.setVcheck = QtWidgets.QCheckBox(self.frame)
        self.setVcheck.setText("")
        self.setVcheck.setChecked(True)
        self.setVcheck.setObjectName("setVcheck")
        self.horizontalLayout_4.addWidget(self.setVcheck)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.resetV = QtWidgets.QDoubleSpinBox(self.frame)
        self.resetV.setMinimumSize(QtCore.QSize(115, 0))
        self.resetV.setDecimals(3)
        self.resetV.setMinimum(-9.0)
        self.resetV.setMaximum(10.0)
        self.resetV.setSingleStep(0.001)
        self.resetV.setProperty("value", 3.0)
        self.resetV.setObjectName("resetV")
        self.horizontalLayout_5.addWidget(self.resetV)
        self.resetVcheck = QtWidgets.QCheckBox(self.frame)
        self.resetVcheck.setText("")
        self.resetVcheck.setChecked(True)
        self.resetVcheck.setObjectName("resetVcheck")
        self.horizontalLayout_5.addWidget(self.resetVcheck)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.time_hr = QtWidgets.QTimeEdit(self.frame)
        self.time_hr.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.time_hr.setMaximumTime(QtCore.QTime(23, 59, 59))
        self.time_hr.setMinimumTime(QtCore.QTime(0, 0, 1))
        self.time_hr.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.time_hr.setTime(QtCore.QTime(2, 46, 40))
        self.time_hr.setObjectName("time_hr")
        self.horizontalLayout_6.addWidget(self.time_hr)
        self.time_sec = QtWidgets.QSpinBox(self.frame)
        self.time_sec.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.time_sec.setMinimum(1)
        self.time_sec.setMaximum(86399)
        self.time_sec.setProperty("value", 10000)
        self.time_sec.setObjectName("time_sec")
        self.horizontalLayout_6.addWidget(self.time_sec)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout_6, 11, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.iLimit = QtWidgets.QDoubleSpinBox(self.frame)
        self.iLimit.setMinimumSize(QtCore.QSize(0, 0))
        self.iLimit.setDecimals(3)
        self.iLimit.setMinimum(0.001)
        self.iLimit.setMaximum(500.0)
        self.iLimit.setSingleStep(0.1)
        self.iLimit.setProperty("value", 1.0)
        self.iLimit.setObjectName("iLimit")
        self.horizontalLayout_7.addWidget(self.iLimit)
        self.resistor = QtWidgets.QLabel(self.frame)
        self.resistor.setObjectName("resistor")
        self.horizontalLayout_7.addWidget(self.resistor)
        self.gridLayout.addLayout(self.horizontalLayout_7, 10, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(Retention)
        self.widget.setMinimumSize(QtCore.QSize(221, 151))
        self.widget.setMaximumSize(QtCore.QSize(293, 154))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.timeTaken = QtWidgets.QLineEdit(self.widget)
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
        self.start_Button = QtWidgets.QPushButton(self.widget)
        self.start_Button.setObjectName("start_Button")
        self.verticalLayout.addWidget(self.start_Button)
        self.skip_Button = QtWidgets.QPushButton(self.widget)
        self.skip_Button.setObjectName("skip_Button")
        self.verticalLayout.addWidget(self.skip_Button)
        self.abort_Button = QtWidgets.QPushButton(self.widget)
        self.abort_Button.setObjectName("abort_Button")
        self.verticalLayout.addWidget(self.abort_Button)
        self.status = QtWidgets.QLineEdit(self.widget)
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
        self.gridLayout_2.addWidget(self.widget, 1, 0, 1, 1)
        self.retentionPlot = PlotWidget(Retention, viewBox=ViewBox(border=mkPen(color='k', width=2)))
        self.retentionPlot.setBackground((255, 182, 193, 25))
        self.retentionPlot.setMinimumSize(QtCore.QSize(411, 379))
        self.retentionPlot.setObjectName("retentionPlot")
        self.gridLayout_2.addWidget(self.retentionPlot, 0, 1, 2, 1)

        self.retranslateUi(Retention)
        self.setTimeUnit.setCurrentIndex(0)
        self.vsource.setCurrentIndex(1)
        self.resetTimeUnit.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Retention)

    def retranslateUi(self, Retention):
        _translate = QtCore.QCoreApplication.translate
        Retention.setWindowTitle(_translate("Retention", "Form"))
        self.Program_label.setText(_translate("Retention", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; color:#0000ff;\">Retention Test</span></p></body></html>"))
        self.setting_label.setText(_translate("Retention", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#aa0000;\">Settings</span></p></body></html>"))
        self.setTimeUnit.setToolTip(_translate("Retention", "<html><head/><body><p>Select time unit</p></body></html>"))
        self.setTimeUnit.setItemText(0, _translate("Retention", "µs"))
        self.setTimeUnit.setItemText(1, _translate("Retention", "ms"))
        self.setTimeUnit.setItemText(2, _translate("Retention", "s"))
        self.points_label.setText(_translate("Retention", "Points"))
        self.readVoltage_label.setText(_translate("Retention", "<html><head/><body><p><span style=\" font-size:10pt;\">Read Voltage (V)</span></p></body></html>"))
        self.temperature.setToolTip(_translate("Retention", "<html><head/><body><p>Temperature range will depend on the type of heater</p></body></html>"))
        self.Ilimit_label.setText(_translate("Retention", "<html><head/><body><p><span style=\" font-size:10pt;\">Current Limit (mA)</span></p></body></html>"))
        self.temp_check.setToolTip(_translate("Retention", "<html><head/><body><p>Use temperature only if temperature controller is attached</p></body></html>"))
        self.temp_check.setText(_translate("Retention", "Temperature (K)"))
        self.resetV_label.setText(_translate("Retention", "<html><head/><body><p><span style=\" font-size:10pt;\">Reset Voltage (V)</span></p></body></html>"))
        self.setV_label.setText(_translate("Retention", "<html><head/><body><p><span style=\" font-size:10pt;\">Set Voltage (V)</span></p></body></html>"))
        self.vsource.setItemText(0, _translate("Retention", "Keithley 2450"))
        self.vsource.setItemText(1, _translate("Retention", "Tektronix AFG1022"))
        self.file_name.setText(_translate("Retention", "sample.dat"))
        self.source_label.setText(_translate("Retention", "<html><head/><body><p><span style=\" font-size:10pt;\">Pulse Source</span></p></body></html>"))
        self.fname_label.setText(_translate("Retention", "<html><head/><body><p><span style=\" font-size:10pt;\">File Name</span></p></body></html>"))
        self.average_label.setText(_translate("Retention", "<html><head/><body><p><span style=\" font-size:10pt;\">Average over</span></p></body></html>"))
        self.setPwidth_label.setText(_translate("Retention", "<html><head/><body><p><span style=\" font-size:10pt;\">Set Pulse width</span></p></body></html>"))
        self.resetPwidth_label.setText(_translate("Retention", "<html><head/><body><p><span style=\" font-size:10pt;\">Reset Pulse width</span></p></body></html>"))
        self.resetTimeUnit.setToolTip(_translate("Retention", "<html><head/><body><p>Select time unit</p></body></html>"))
        self.resetTimeUnit.setItemText(0, _translate("Retention", "µs"))
        self.resetTimeUnit.setItemText(1, _translate("Retention", "ms"))
        self.resetTimeUnit.setItemText(2, _translate("Retention", "s"))
        self.time_label.setText(_translate("Retention", "<html><head/><body><p><span style=\" font-size:10pt;\">Measurement Time</span></p></body></html>"))
        self.setV.setToolTip(_translate("Retention", "<html><head/><body><p>Max -10 V</p></body></html>"))
        self.resetV.setToolTip(_translate("Retention", "<html><head/><body><p>Max 10 V</p></body></html>"))
        self.time_hr.setToolTip(_translate("Retention", "<html><head/><body><p>hour:minute:second</p><p>Maximum 1 day</p></body></html>"))
        self.time_hr.setDisplayFormat(_translate("Retention", "h:mm:ss"))
        self.time_sec.setToolTip(_translate("Retention", "<html><head/><body><p>Total time in seconds</p><p>maximum: 86399</p></body></html>"))
        self.label_2.setText(_translate("Retention", "s"))
        self.iLimit.setToolTip(_translate("Retention", "<html><head/><body><p>If source is SMU, no need to connect resistor. If function generator is used, connect a resistor of specified value. </p></body></html>"))
        self.resistor.setText(_translate("Retention", "~ 1  kΩ"))
        self.start_Button.setToolTip(_translate("Retention", "<html><head/><body><p>Click to start the experiment</p></body></html>"))
        self.start_Button.setText(_translate("Retention", "START"))
        self.skip_Button.setText(_translate("Retention", "Skip to Next"))
        self.abort_Button.setToolTip(_translate("Retention", "<html><head/><body><p>Click to abort the experiment</p></body></html>"))
        self.abort_Button.setText(_translate("Retention", "Abort"))

class app_Retention(Ui_Retention):
    """The Switch app module."""

    def __init__(self, parent=None, k2450 = None, k2700 = None, afg1022 = None, sName="Sample_Retention.dat"):
        super(app_Retention, self).__init__(parent)
        self.parent = parent
        self.k2450 = k2450
        self.k2700 = k2700
        self.afg1022 = afg1022
        self.stopCall = False
        self.skip = False
        self.resistor.setToolTip("Connect a resistor of this value in series to input from function generator.")
        self.time_hr.setWrapping(True)
        self.time_hr.setCurrentSection(QtWidgets.QTimeEdit.MinuteSection)
        self.skip_Button.setEnabled(False)
        self.abort_Button.setEnabled(False)
        self.start_Button.clicked.connect(self.startRetention)
        self.skip_Button.clicked.connect(self.skip_to_next)
        self.abort_Button.clicked.connect(self.abortRetention)
        self.vsource.currentIndexChanged.connect(self.update_limits)
        self.time_sec.valueChanged.connect(self.connect_sec_to_hr)
        self.time_hr.timeChanged.connect(self.connect_hr_to_sec)
        self.time_hr.editingFinished.connect(self.update_total_time)
        self.time_sec.editingFinished.connect(self.update_total_time)
        self.setVcheck.stateChanged.connect(self.update_total_time)
        self.resetVcheck.stateChanged.connect(self.update_total_time)
        self.iLimit.valueChanged.connect(self.update_resistor)
        self.setV.valueChanged.connect(self.update_resistor)
        self.resetV.valueChanged.connect(self.update_resistor)
        self.update_resistor()
        self.initialize_plot()
        self.update_limits()
        self.k2450.nplc = 1
        self.k2450.avg = 5
        self.k2450.readV = 0.1
        self.measurement_status = "Idle"
        self.filename = sName
        self.file_name.setText(self.filename)
        self.file_name.setReadOnly(True)
        self.update_total_time()
        self.params = {
            "Vset": 3,
            "setPwidth": 1,
            "set_timeUnit": 1,  # 0 = us, 1=ms, 2 = s
            "Vreset": -3,
            "resetPwidth": 1,
            "reset_timeUnit": 1,  # 0 = us, 1=ms, 2 = s
            "ILimit": 0.001,
            "Measure_time": 10000,
            "Rvoltage": 0.1,  # V
            "Average": 5,
            "temperature": 300}

    def skip_to_next(self):
        self.skip = True
    
    def update_resistor(self):
        limiting_current = self.iLimit.value()
        max_applied_voltage = max(abs(self.setV.value()),abs(self.resetV.value()))
        self.resistance = round(max_applied_voltage/limiting_current,2)
        self.resistor.setText("~ {} kΩ".format(self.resistance))
    
    def update_total_time(self):
        self.measure_counts = 0
        if self.setVcheck.isChecked():
            self.measure_counts = self.measure_counts + 1
        if self.resetVcheck.isChecked():
            self.measure_counts = self.measure_counts + 1
        total_time = self.measure_counts * self.time_sec.value()
        total_Qtime = QTime(0,0,0)
        total_Qtime = total_Qtime.addSecs(total_time)
        self.timeTaken.setText("Total experiment time = {}".format(total_Qtime.toString("h:mm:ss")))
    
    def update_limits(self):
        if self.vsource.currentIndex() == 0:
            self.setV.setMaximum(190)
            self.resetV.setMaximum(190)
            self.setV.setMinimum(-190)
            self.resetV.setMinimum(-190)
            if self.setTimeUnit.currentIndex() == 0:
                self.setTimeUnit.setCurrentIndex(1)
            self.setTimeUnit.model().item(0).setEnabled(False)
            if self.resetTimeUnit.currentIndex() == 0:
                self.resetTimeUnit.setCurrentIndex(1)
            self.resetTimeUnit.model().item(0).setEnabled(False)
        else:
            self.setV.setMaximum(5)
            self.resetV.setMaximum(5)
            self.setV.setMinimum(-5)
            self.resetV.setMinimum(-5)
            self.setTimeUnit.model().item(0).setEnabled(True)
            self.resetTimeUnit.model().item(0).setEnabled(True)
    
    def connect_sec_to_hr(self):
        seconds = int(self.time_sec.value())
        time = QTime(0,0,0)
        time = time.addSecs(seconds)
        self.time_hr.setTime(time)
        
    def connect_hr_to_sec(self):
        time = self.time_hr.time()
        self.time_sec.setValue(time.hour()*3600+time.minute()*60+time.second())
        
    def configurePulse(self):
        """
        Configure the pulse parameters.

        Returns
        -------
        None.

        """
        self.params = {
            "Vset": self.setV.value(),
            "setPwidth": self.setPwidth.value(),
            "set_timeUnit": self.setTimeUnit.currentIndex(),
            "Vreset": self.resetV.value(),
            "resetPwidth": self.resetPwidth.value(),
            "reset_timeUnit": self.resetTimeUnit.currentIndex(),
            "ILimit": self.iLimit.value()/1000,
            "Measure_time": self.time_sec.value(),
            "Rvoltage": self.read_voltage.value(),
            "Average": self.avg.value(),
            "temperature": self.temperature.value()}
        self.k2450.avg = self.params["Average"]
        self.readV = self.params["Rvoltage"]
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
        self.timePoints = linlogspace(self.time_sec.value(),start=0,points_per_order=18)
        self.binnedPoints = getBinnedPoints(self.timePoints)
        self.number_of_points = len(self.binnedPoints)
        # set compliance current
        if self.vsource.currentIndex() == 0:
            self.k2450.write("source:voltage:ilimit {0}".format(self.params["ILimit"]))
        
    def initialize_SMU_and_AFG(self):
        """
        Initialize the SMU.

        Returns
        TODO: Feed the whole retention program into SMU, and receive buffer every n seconds.
        TODO: Ensure read voltage is always applied to sample during measurement
        TODO: Implement continuous measurement? Use threading to plot
        -------
        None.

        """
        self.k2450.apply_voltage(compliance_current=self.params["ILimit"])
        self.k2450.measure_current(nplc=self.k2450.nplc)
        self.k2450.write("SENS:curr:rsen OFF")  # two wire configuration
        self.k2450.write(":DISPlay:LIGHT:STATe ON25")
        self.k2450.write("sour:volt:read:back 1")
        self.k2450.write("SENSe:CURRent:NPLCycles {0}".format(self.k2450.nplc))
        self.k2450.write("TRIG:LOAD 'SimpleLoop', {0}, 0".format(self.params["Average"]))
        self.k2450.source_voltage = self.params["Rvoltage"]

    def do_one_retention(self):
        """
        Apply 1 pulse from AFG or SMU, and measure resistance from SMU.

        Returns
        -------
        None.

        """
        if self.vsource.currentIndex() == 0:
            connect_sample_with_SMU(self.k2700)
            self.k2450.apply_switch_pulse(*self.pulses_to_apply[self.i])
        elif self.vsource.currentIndex() == 1:
            connect_sample_with_AFG(self.k2700)
            self.afg1022.setSinglePulse(*self.pulses_to_apply[self.i])
            self.afg1022.trgNwait()
            connect_sample_with_SMU(self.k2700)
        
        self.k2450.write("TRIG:LOAD 'SimpleLoop', {}, 0".format(self.params["Average"]))
        self.k2450.source_voltage = self.k2450.readV
        
        if self.pulses_to_apply[self.i][0] == self.params["Vset"]:
            self.ntimesSet = []
            self.startTime = time()
            self.j = 0
            self.read_LRS_dataPoints()
        elif self.pulses_to_apply[self.i][0] == self.params["Vreset"] and not self.stopCall:
            self.ntimesReset = []
            self.startTime = time()
            self.j = 0
            self.read_HRS_dataPoints()

    def read_LRS_dataPoints(self):
        readCurrent = self.k2450.readReRAM()
        endTime = round((time() - self.startTime),3)
        self.ntimesSet.append(endTime)
        self.LRScurrents.append(readCurrent)
        self.LRS.append(abs(self.params["Rvoltage"]/readCurrent))
        self.data_lineLRS.setData(self.ntimesSet,self.LRS)
        self.j = self.j+1
        if self.j >= self.number_of_points or self.stopCall or self.skip:
            self.skip = False
            self.skip_Button.setEnabled(False)
            self.i = self.i+1
            if self.i >= len(self.pulses_to_apply) or self.stopCall:
                self.stop_program()
                return
            self.timer.singleShot(0,self.do_one_retention)
            return
        if self.j > 9:
            pauseTime = (self.timePoints[self.j]-endTime)*1000
        else:
            pauseTime = self.binnedPoints[self.j]*1000
        self.timer.singleShot(pauseTime, QtCore.Qt.PreciseTimer, self.read_LRS_dataPoints)
    
    def read_HRS_dataPoints(self):
        readCurrent = self.k2450.readReRAM()
        endTime = time() - self.startTime
        self.ntimesReset.append(round(endTime,3))
        self.HRScurrents.append(readCurrent)
        self.HRS.append(abs(self.params["Rvoltage"]/readCurrent))
        self.data_lineHRS.setData(self.ntimesReset,self.HRS)
        self.j = self.j+1
        if self.j >= self.number_of_points or self.stopCall or self.skip:
            self.skip = False
            self.skip_Button.setEnabled(False)
            self.i = self.i+1
            if self.i >= len(self.pulses_to_apply) or self.stopCall:
                self.stop_program()
                return
            self.timer.singleShot(0,self.do_one_retention)
            return
        if self.j > 9:
            pauseTime = (self.timePoints[self.j]-endTime)*1000
        else:
            pauseTime = self.binnedPoints[self.j]*1000
        self.timer.singleShot(pauseTime, QtCore.Qt.PreciseTimer, self.read_HRS_dataPoints)
        
    def startRetention(self):
        """
        Begins the retention experiment.

        Returns
        -------
        None.

        """
        self.measurement_status = "Running"
        if not self.setVcheck.isChecked() and not self.resetVcheck.isChecked():
            self.stopCall = True
            title = "No resistance state selected"
            text = "Please check atleast one of the set/reset states to carry out retention measurement."
            self.status.setText("Select atleast 1 resistive state.")
            QMessageBox.critical(self,title,text)
            self.measurement_status = "Idle"
            return
        if self.vsource.currentIndex() == 1:
            title = "Confirm resistance."
            text = "Is resistor of {} kΩ connected?".format(self.resistance)
            reply = QMessageBox.question(self, title,text,QMessageBox.Yes,QMessageBox.No)
            if reply == QMessageBox.No:
                self.stopCall = True
                self.measurement_status = "Idle"
                return
            LRSCurrent, HRSCurrent = self.read_LRS_HRS_states()
        else:
            vset = vreset = 0
            setpulse = resetpulse = 0.1
            if self.setVcheck.isChecked():
                vset = self.params["Vset"]
                setpulse = self.setTimestep
            if self.resetVcheck.isChecked():
                vreset = self.params["Vreset"]
                resetpulse = self.resetTimestep
            LRSCurrent, HRSCurrent = self.k2450.read_resistance_states([(vset,setpulse),(vreset,resetpulse)])
        self.stopCall = False
        self.skip = False
        self.status.setText("Program Running..")
        self.i = 0
        self.configurePulse()
        self.initialize_SMU_and_AFG()
        self.retentionPlot.clear()
        ntimes = [0.01]
        self.pulses_to_apply = []
        
        if self.setVcheck.isChecked():
            self.LRScurrents = [LRSCurrent]
            self.LRS = [abs(self.params["Rvoltage"]/LRSCurrent)]
            pen1 = mkPen(color=(0, 0, 255), width=2)
            self.data_lineLRS = self.retentionPlot.plot(ntimes, self.LRS, pen=pen1, symbol='x', symbolPen='r')
            del self.LRScurrents[0]
            del self.LRS[0]
            self.pulses_to_apply.append([self.params["Vset"],self.setTimestep])
        if self.resetVcheck.isChecked():
            self.HRScurrents = [HRSCurrent]
            self.HRS = [abs(self.params["Rvoltage"]/HRSCurrent)]
            pen2 = mkPen(color=(255, 0, 0), width=2)
            self.data_lineHRS = self.retentionPlot.plot(ntimes, self.HRS, pen=pen2, symbol='o')
            del self.HRScurrents[0]
            del self.HRS[0]
            self.pulses_to_apply.append([self.params["Vreset"],self.resetTimestep])
        del ntimes[0]
        self.start_Button.setEnabled(False)
        self.abort_Button.setEnabled(True)
        if self.measure_counts == 2:
            self.skip_Button.setEnabled(True)
        self.k2450.enable_source()
        self.timer = QTimer()
        print(self.number_of_points)
        self.timer.singleShot(0, self.do_one_retention)

    def read_LRS_HRS_states(self):
        # Assuming function generator is connected and SMU is disconnected
        LRScurrent = 1e-12
        HRScurrent = 1e-12
        if self.setVcheck.isChecked():
            # Get LRS
            self.k2700.open_Channels(SMU) # disconnect SMU
            self.k2700.close_Channels(AFG) # connect function generator
            waitFor(20) # wait for 20msec to ensure switching is complete
            self.afg1022.setSinglePulse(self.params['Vset'],self.setTimestep)
            self.afg1022.trgNwait()
            self.k2700.open_Channels(AFG) # disconnect function generator
            self.k2700.close_Channels(SMU) # connect SMU
            waitFor(20) # wait for 20msec to ensure switching is complete
            # Measure Read resistance using K2450
            LRScurrent = self.k2450.readReRAM()
        if self.resetVcheck.isChecked():
            # Get HRS        
            self.k2700.open_Channels(SMU) # disconnect SMU
            self.k2700.close_Channels(AFG) # connect function generator
            waitFor(20) # wait for 20msec to ensure switching is complete
            self.afg1022.setSinglePulse(self.params['Vreset'],self.resetTimestep)
            self.afg1022.trgNwait()
            self.k2700.open_Channels(AFG) # disconnect function generator
            self.k2700.close_Channels(SMU) # connect SMU
            waitFor(20) # wait for 20msec to ensure switching is complete
            # Measure Read resistance using K2450
            HRScurrent = self.k2450.readReRAM()
        self.k2700.open_Channels(SMU) # disconnect SMU
        self.k2700.close_Channels(AFG) # connect function generator
        waitFor(20) # wait for 20msec to ensure switching is complete
        return LRScurrent, HRScurrent
        
    def stop_program(self):
        self.measurement_status = "Stopped"
        self.saveData()
        if self.stopCall:
            self.status.setText("Program Aborted.")
        else:
            self.status.setText("Measurement Finished.")
        self.start_Button.setEnabled(True)
        self.abort_Button.setEnabled(False)
        self.k2450.source_voltage = 0
        self.k2450.disable_source()
        MessageBeep()
    
    def abortRetention(self):
        self.measurement_status = "Aborted"
        self.status.setText("Aborting the program. Please wait..")
        self.stopCall = True
        
    def saveData(self):
        """
        Save the data to file.

        Returns
        -------
        None.

        """
        if self.measure_counts != 0:
            self.status.setText(self.status.text() + " Data saved.")
            self.fullfilename = unique_filename(directory='.', prefix=self.filename, datetimeformat="", ext='dat')
            with open(self.fullfilename, "w", newline='') as f:
                if self.vsource.currentIndex() == 0:
                    f.write("#Pulse voltage source: Keithley 2450 SMU.\n")
                else:
                    f.write("#Pulse voltage source: Tektronix AFG1022 Function Generator.\n")
                f.write("#Pulse limiting current = {}mA\n".format(self.iLimit.value()))
                f.write("#Resistance read using Keithley 2450 SMU.\n")
                f.write("#Read voltage = {0}V, averaged over {1} readings\n".format(self.params["Rvoltage"],self.params["Average"]))
                write_data = writer(f)
                if self.setVcheck.checkState() and self.resetVcheck.checkState():
                    f.write("#Set voltage = {0}, Reset Voltage = {1}.\n".format(self.params["Vset"],self.params["Vreset"]))
                    f.write("#Set pulse width = {0}s, Reset pulse width = {1}s\n".format(self.setTimestep,self.resetTimestep))
                    f.write("Set Time (s), LRS current (A), LRS resistance (Ω), Reset Time (s), HRS Current (A), HRS resistance (Ω)\n")
                    write_data.writerows(zip(self.ntimesSet, self.LRScurrents,self.LRS, 
                                         self.ntimesReset,self.HRScurrents,self.HRS))
                elif self.setVcheck.checkState():
                    f.write("#Set voltage = {} \n".format(self.params["Vset"]))
                    f.write("#Set pulse width = {}s \n".format(self.setTimestep))
                    f.write("Time (s), LRS current (A), LRS resistance (Ω)\n")
                    write_data.writerows(zip(self.ntimesSet, self.LRScurrents, self.LRS))
                elif self.resetVcheck.checkState():
                    f.write("#Reset Voltage = {}.\n".format(self.params["Vreset"]))
                    f.write("#Reset pulse width = {}s\n".format(self.resetTimestep))
                    f.write("Time (s), HRS current (A), HRS resistance (Ω)\n")
                    write_data.writerows(zip(self.ntimesReset, self.HRScurrents, self.HRS))
            
    def initialize_plot(self):
        """
        Initialize the plot before starting the measurement.

        Returns
        -------
        None.

        """
        styles = {'color': 'r', 'font-size': '20px'}
        self.retentionPlot.setLabel('left', 'Read Resistance (Ohms)', **styles)
        self.retentionPlot.setLabel('bottom', 'Time (s)', **styles)
        self.retentionPlot.getPlotItem().setLogMode(True, True)
        self.retentionPlot.addLegend(offset=(180,170))
    
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
                self.stop_program()
        if reply == QMessageBox.Yes:
            if __name__ != "__main__":
                self.parent.show()
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Retention = QtWidgets.QWidget()
    k2450, k2700, afg1022 = checkInstrument(test = True)
    ui = app_Retention(Retention, k2450, k2700, afg1022)
    ui.show()
    app.exec_()
    app.quit()