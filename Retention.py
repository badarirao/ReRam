# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'retention.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, ViewBox, mkPen
from os.path import exists as fileExists
from winsound import MessageBeep
from csv import writer
from utilities import linlogspace, SMU, AFG, waitFor
from utilities import connect_sample_with_AFG, unique_filename, checkInstrument

class Ui_Retention(object):
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
        self.setV.setMinimum(-10.0)
        self.setV.setMaximum(9.0)
        self.setV.setSingleStep(0.001)
        self.setV.setProperty("value", -3.0)
        self.setV.setObjectName("setV")
        self.horizontalLayout_4.addWidget(self.setV)
        self.setVcheck = QtWidgets.QCheckBox(self.frame)
        self.setVcheck.setText("")
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
        self.resetVcheck.setObjectName("resetVcheck")
        self.horizontalLayout_5.addWidget(self.resetVcheck)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 1, 1, 1)
        self.iLimit = QtWidgets.QComboBox(self.frame)
        self.iLimit.setObjectName("iLimit")
        self.iLimit.addItem("")
        self.iLimit.addItem("")
        self.iLimit.addItem("")
        self.gridLayout.addWidget(self.iLimit, 10, 1, 1, 1)
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
        self.retentionPlot.setMinimumSize(QtCore.QSize(411, 379))
        self.retentionPlot.setObjectName("retentionPlot")
        self.gridLayout_2.addWidget(self.retentionPlot, 0, 1, 2, 1)

        self.retranslateUi(Retention)
        self.setTimeUnit.setCurrentIndex(0)
        self.vsource.setCurrentIndex(1)
        self.resetTimeUnit.setCurrentIndex(0)
        self.iLimit.setCurrentIndex(0)
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
        self.iLimit.setItemText(0, _translate("Retention", "1 mA"))
        self.iLimit.setItemText(1, _translate("Retention", "0.5 mA"))
        self.iLimit.setItemText(2, _translate("Retention", "0.1 mA"))
        self.time_hr.setToolTip(_translate("Retention", "<html><head/><body><p>hour:minute:second</p><p>Maximum 1 day</p></body></html>"))
        self.time_hr.setDisplayFormat(_translate("Retention", "h:mm:ss"))
        self.time_sec.setToolTip(_translate("Retention", "<html><head/><body><p>Total time in seconds</p><p>maximum: 86399</p></body></html>"))
        self.label_2.setText(_translate("Retention", "s"))
        self.start_Button.setToolTip(_translate("Retention", "<html><head/><body><p>Click to start the experiment</p></body></html>"))
        self.start_Button.setText(_translate("Retention", "START"))
        self.skip_Button.setText(_translate("Retention", "Skip to Next"))
        self.abort_Button.setToolTip(_translate("Retention", "<html><head/><body><p>Click to abort the experiment</p></body></html>"))
        self.abort_Button.setText(_translate("Retention", "Abort"))

class app_Retention(Ui_Retention):
    """The Switch app module."""

    def __init__(self, parent=None, k2450 = None, k2700 = None, afg1022 = None, sName="Sample_Retention.dat"):
        super(app_Retention, self).__init__(parent)
        self.k2450 = k2450
        self.k2700 = k2700
        self.afg1022 = afg1022
        self.stopCall = False
        self.start_Button.clicked.connect(self.startRetention)
        self.skip_Button.clicked.connect(self.skip_to_next)
        self.abort_Button.clicked.connect(self.abortRetention)
        self.initialize_plot()
        self.nplc = 1
        self.filename = sName
        self.file_name.setText(self.filename)
        self.file_name.setReadOnly(True)
        self.params = {
            "Vset": -3,
            "setPwidth": 10,
            "set_timeUnit": 0,  # 0 = us, 1=ms, 2 = s
            "Vreset": 3,
            "resetPwidth": 10,
            "reset_timeUnit": 0,  # 0 = us, 1=ms, 2 = s
            "ILimit": 0,
            "Measure_time": 10000,
            "Rvoltage": 0.1,  # V
            "Average": 5,
            "temperature": 300}

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
            "ILimit": self.iLimit.currentIndex(),
            "Measure_time": self.time_sec.value(),
            "Rvoltage": self.read_voltage.value(),
            "Average": self.avg.value(),
            "temperature": self.temperature.value()}
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
        if self.params["ILimit"] == 0:
            self.iLimitAmp = 0.001
        elif self.params["ILimit"] == 1:
            self.iLimitAmp = 0.0005
        elif self.params["ILimit"] == 2:
            self.iLimitAmp = 0.0001
        self.points = linlogspace(self.nPulse_order*self.params["nPUlses"])
        self.number_of_points = len(self.fpoints)
        # set compliance current
        self.k2450.write("source:voltage:ilimit {0}".format(self.params["ILimit"]))
        
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
        self.k2450.apply_voltage(compliance_current=self.iLimitAmp)
        self.k2450.measure_current(nplc=self.nplc)
        self.k2450.write("SENS:curr:rsen OFF")  # two wire configuration
        self.k2450.write(":DISPlay:LIGHT:STATe ON25")
        self.k2450.write("sour:volt:read:back 1")
        self.k2450.write("SENSe:CURRent:NPLCycles {0}".format(self.nplc))
        self.k2450.write("TRIG:LOAD 'SimpleLoop', {0}, 0".format(self.params["Average"]))
        self.k2450.source_voltage = self.params["Rvoltage"]
        connect_sample_with_AFG(self.k2700)

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
        HRScurrent, LRScurrent = self.read_LRS_HRS_states()
        self.ncycles.append(self.fpoints[self.i])
        self.LRScurrents.append(LRScurrent)
        self.LRS.append(self.params['Vset']/LRScurrent)
        self.HRScurrents.append(HRScurrent)
        self.HRS.append(self.params['Vreset']/HRScurrent)
               
        self.data_lineHRS.setData(self.ncycles, self.HRS)
        self.data_lineLRS.setData(self.ncycles, self.LRS)
        
        self.i = self.i + 1
        if self.i >= self.number_of_points or self.stopCall:
            self.stop_program()
            return
        
        self.k2700.close_Channels(AFG) # connect function generator for next set of cycles
        waitFor(20) # wait for 20msec to ensure switching is complete
        self.timer.singleShot(0, self.pulseMeasure_AFG)  # Measure next pulse    

    def startRetention(self):
        """
        Begins the switching experiment.

        Note: set not to measure the actual applied voltage, as it saves time
        TODO: If both set and reset pulses are disabled, then take no action

        Returns
        -------
        None.

        """
        self.stopCall = False
        self.status.setText("Program Running..")
        self.i = 0
        self.initialize_SMU_and_AFG()
        LRScurrent,HRScurrent = self.read_LRS_HRS_states()
        self.ncycles = [0]
        self.LRScurrents = [LRScurrent]
        self.LRS = [self.params['Vset']/LRScurrent]
        self.HRScurrents = [HRScurrent]
        self.HRS = [self.params['Vreset']/HRScurrent]
        pen1 = mkPen(color=(0, 0, 255), width=2)
        pen2 = mkPen(color=(255, 0, 0), width=2)
        self.data_lineLRS = self.retentionPlot.plot(self.ncycles, self.LRS, pen=pen2, symbol='x', symbolPen='r')
        self.data_lineHRS = self.retentionPlot.plot(self.ncycles, self.HRS, pen=pen1, symbol='o')
        self.timer = QtCore.QTimer()
        self.start_Button.setEnabled(False)
        self.abort_Button.setEnabled(True)
        self.configurePulse()
        self.k2450.enable_source()
        self.timer.singleShot(0, self.pulseMeasure_AFG)

    def read_LRS_HRS_states(self):
        # Assuming function generator is connected and SMU is disconnected
        
        # Get LRS
        self.afg1022.setSinglePulse(self.params['Vset'],self.setTimestep)
        self.afg1022.trgNwait()
        self.k2700.open_Channels(AFG) # disconnect function generator
        self.k2700.close_Channels(SMU) # connect SMU
        waitFor(20) # wait for 20msec to ensure switching is complete
        # Measure Read resistance using K2450
        HRScurrent = self.k2450.readReRAM()
        
        # Get HRS        
        self.k2700.open_Channels(SMU) # disconnect SMU
        self.k2700.close_Channels(AFG) # connect function generator
        waitFor(20) # wait for 20msec to ensure switching is complete
        self.afg1022.setSinglePulse(self.params['Vreset'],self.resetTimestep)
        afg1022.trgNwait()
        self.k2700.open_Channels(AFG) # disconnect function generator
        self.k2700.close_Channels(SMU) # connect SMU
        waitFor(20) # wait for 20msec to ensure switching is complete
        # Measure Read resistance using K2450
        LRScurrent = self.k2450.readReRAM()
        self.k2700.open_Channels(SMU) # disconnect SMU
        self.k2700.close_Channels(AFG) # connect function generator
        waitFor(20) # wait for 20msec to ensure switching is complete
        return LRScurrent, HRScurrent
        
    def stop_program(self):
        self.saveData()
        if self.stopCall:
            self.status.setText("Program Aborted. Partial data saved.")
        else:
            self.status.setText("Measurement Finished. Data saved.")
        self.start_Button.setEnabled(True)
        self.abort_Button.setEnabled(False)
        self.k2450.source_voltage = 0
        self.k2450.disable_source()
        MessageBeep()
    
    def abortRetention(self):
        self.status.setText("Aborting the program. Please wait..")
        self.stopCall = True
        
    def saveData(self):
        """
        Save the data to file.

        Returns
        -------
        None.

        """
        self.fullfilename = unique_filename(directory='.', prefix=self.filename, datetimeformat="", ext='csv')
        with open(self.fullfilename, "w", newline='') as f:
            f.write("#Pulse voltage source: Tektronix AFG1022 MultiFunction Generator.\n")
            f.write("#Resistance read using Keithley 2450 source-measure unit.\n")
            f.write("#Set voltage = {0}, Reset Voltage = {1}.\n".format(self.params["Vset"],self.params["Vreset"]))
            f.write("#Set pulse width = {0}s, Reset pulse width = {1}s\n".format(self.setTimestep,self.resetTimestep))
            f.write("#Read voltage = {0}V, averaged over {1} readings\n".format(self.params["Rvoltage"],self.params["Average"]))
            f.write("#Limiting current = {}mA\n\n".format(self.iLimitAmp*1000))
            f.write("NCycles, LRS current (A), HRS Current, LRS resistance (Ω), HRS resistance (Ω)\n")
            write_data = writer(f)
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
        self.retentionPlot.setLabel('left', 'Read Resistance (Ohms)', **styles)
        self.retentionPlot.setLabel('bottom', 'N. cycles', **styles)
        self.retentionPlot.addLegend(offset=(180,170))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Retention = QtWidgets.QWidget()
    k2450, k2700, afg1022 = checkInstrument(test = True)
    ui = app_Retention(Retention, k2450, k2700, afg1022)
    ui.show()
    sys.exit(app.exec_())