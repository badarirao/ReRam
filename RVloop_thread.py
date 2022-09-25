# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RVloop.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

# TODO: Add tooltips
# TODO: There is some problem when stopping the measurement in between (I think it is resolved)
#TODO: Implement plotting multiple RV cycles when threading is implemented.
# TODO: When Keysight B2902 is selected, use pulse stairs for this measurement
# TODO: option to start from minV or maxV, and specify it in metadata
from winsound import MessageBeep
from csv import writer
from numpy import linspace, around, concatenate, array
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
from pyqtgraph import PlotWidget, ViewBox, mkPen
from utilities import unique_filename, FakeAdapter, checkInstrument, SMU, AFG
from utilities import connect_sample_with_SMU, waitFor, datetime

class Ui_RVLoop(QtWidgets.QWidget):
    """The pyqt5 gui class for RV loop measurement."""

    def __init__(self, parent=None):
        super(Ui_RVLoop, self).__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)

    def setupUi(self, RVLoop):
        RVLoop.setObjectName("RVLoop")
        RVLoop.resize(1050, 646)
        RVLoop.setMinimumSize(QtCore.QSize(1050, 550))
        self.gridLayout_2 = QtWidgets.QGridLayout(RVLoop)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(RVLoop)
        self.groupBox.setMinimumSize(QtCore.QSize(222, 370))
        self.groupBox.setMaximumSize(QtCore.QSize(293, 400))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Program_label = QtWidgets.QLabel(self.groupBox)
        self.Program_label.setMinimumSize(QtCore.QSize(0, 24))
        self.Program_label.setMaximumSize(QtCore.QSize(16777215, 24))
        self.Program_label.setObjectName("Program_label")
        self.verticalLayout_2.addWidget(self.Program_label)
        self.setting_label = QtWidgets.QLabel(self.groupBox)
        self.setting_label.setMinimumSize(QtCore.QSize(0, 24))
        self.setting_label.setMaximumSize(QtCore.QSize(16777215, 24))
        self.setting_label.setObjectName("setting_label")
        self.verticalLayout_2.addWidget(self.setting_label)
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.scan_speed = QtWidgets.QComboBox(self.frame)
        self.scan_speed.setObjectName("scan_speed")
        self.scan_speed.addItem("")
        self.scan_speed.addItem("")
        self.scan_speed.addItem("")
        self.scan_speed.addItem("")
        self.scan_speed.addItem("")
        self.gridLayout.addWidget(self.scan_speed, 6, 1, 1, 1)
        self.maxV = QtWidgets.QDoubleSpinBox(self.frame)
        self.maxV.setDecimals(3)
        self.maxV.setMinimum(-9.0)
        self.maxV.setMaximum(10.0)
        self.maxV.setSingleStep(0.001)
        self.maxV.setProperty("value", 3.0)
        self.maxV.setObjectName("maxV")
        self.gridLayout.addWidget(self.maxV, 3, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pulse_width = QtWidgets.QDoubleSpinBox(self.frame)
        self.pulse_width.setDecimals(1)
        self.pulse_width.setProperty("value", 1.0)
        self.pulse_width.setObjectName("pulse_width")
        self.horizontalLayout.addWidget(self.pulse_width)
        self.time_unit = QtWidgets.QComboBox(self.frame)
        self.time_unit.setMaximumSize(QtCore.QSize(41, 22))
        self.time_unit.setObjectName("time_unit")
        self.time_unit.addItem("")
        self.time_unit.addItem("")
        self.time_unit.addItem("")
        self.horizontalLayout.addWidget(self.time_unit)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 1, 1, 1)
        self.minV = QtWidgets.QDoubleSpinBox(self.frame)
        self.minV.setDecimals(3)
        self.minV.setMinimum(-10.0)
        self.minV.setMaximum(9.0)
        self.minV.setSingleStep(0.001)
        self.minV.setProperty("value", -3.0)
        self.minV.setObjectName("minV")
        self.gridLayout.addWidget(self.minV, 2, 1, 1, 1)
        self.vstep = QtWidgets.QDoubleSpinBox(self.frame)
        self.vstep.setMaximum(5.0)
        self.vstep.setSingleStep(0.1)
        self.vstep.setProperty("value", 0.1)
        self.vstep.setObjectName("vstep")
        self.gridLayout.addWidget(self.vstep, 4, 1, 1, 1)
        self.vstep_label = QtWidgets.QLabel(self.frame)
        self.vstep_label.setObjectName("vstep_label")
        self.gridLayout.addWidget(self.vstep_label, 4, 0, 1, 1)
        self.Ilimit_label = QtWidgets.QLabel(self.frame)
        self.Ilimit_label.setObjectName("Ilimit_label")
        self.gridLayout.addWidget(self.Ilimit_label, 7, 0, 1, 1)
        self.temp_check = QtWidgets.QCheckBox(self.frame)
        self.temp_check.setObjectName("temp_check")
        self.gridLayout.addWidget(self.temp_check, 11, 0, 1, 1)
        self.minV_label = QtWidgets.QLabel(self.frame)
        self.minV_label.setObjectName("minV_label")
        self.gridLayout.addWidget(self.minV_label, 2, 0, 1, 1)
        self.maxV_label = QtWidgets.QLabel(self.frame)
        self.maxV_label.setObjectName("maxV_label")
        self.gridLayout.addWidget(self.maxV_label, 3, 0, 1, 1)
        self.read_voltage = QtWidgets.QDoubleSpinBox(self.frame)
        self.read_voltage.setProperty("value", 0.1)
        self.read_voltage.setObjectName("read_voltage")
        self.gridLayout.addWidget(self.read_voltage, 8, 1, 1, 1)
        self.temperature = QtWidgets.QDoubleSpinBox(self.frame)
        self.temperature.setEnabled(False)
        self.temperature.setMaximum(600.0)
        self.temperature.setProperty("value", 300.0)
        self.temperature.setObjectName("temperature")
        self.gridLayout.addWidget(self.temperature, 11, 1, 1, 1)
        self.ncycles_label = QtWidgets.QLabel(self.frame)
        self.ncycles_label.setObjectName("ncycles_label")
        self.gridLayout.addWidget(self.ncycles_label, 8, 0, 1, 1)
        self.Ilimit = QtWidgets.QDoubleSpinBox(self.frame)
        self.Ilimit.setDecimals(3)
        self.Ilimit.setMaximum(1.0)
        self.Ilimit.setSingleStep(0.001)
        self.Ilimit.setProperty("value", 0.5)
        self.Ilimit.setObjectName("Ilimit")
        self.gridLayout.addWidget(self.Ilimit, 7, 1, 1, 1)
        self.vpulse_lable = QtWidgets.QLabel(self.frame)
        self.vpulse_lable.setObjectName("vpulse_lable")
        self.gridLayout.addWidget(self.vpulse_lable, 5, 0, 1, 1)
        self.vsource_label = QtWidgets.QLabel(self.frame)
        self.vsource_label.setObjectName("vsource_label")
        self.gridLayout.addWidget(self.vsource_label, 1, 0, 1, 1)
        self.scan_speed_label = QtWidgets.QLabel(self.frame)
        self.scan_speed_label.setObjectName("scan_speed_label")
        self.gridLayout.addWidget(self.scan_speed_label, 6, 0, 1, 1)
        self.vsource = QtWidgets.QComboBox(self.frame)
        self.vsource.setObjectName("vsource")
        self.vsource.addItem("")
        self.vsource.addItem("")
        self.vsource.addItem("")
        self.gridLayout.addWidget(self.vsource, 1, 1, 1, 1)
        self.file_name = QtWidgets.QLineEdit(self.frame)
        self.file_name.setObjectName("file_name")
        self.gridLayout.addWidget(self.file_name, 0, 1, 1, 1)
        self.fname_label = QtWidgets.QLabel(self.frame)
        self.fname_label.setObjectName("fname_label")
        self.gridLayout.addWidget(self.fname_label, 0, 0, 1, 1)
        self.ncycles_label_2 = QtWidgets.QLabel(self.frame)
        self.ncycles_label_2.setObjectName("ncycles_label_2")
        self.gridLayout.addWidget(self.ncycles_label_2, 10, 0, 1, 1)
        self.numCycles = QtWidgets.QDoubleSpinBox(self.frame)
        self.numCycles.setDecimals(0)
        self.numCycles.setMaximum(500.0)
        self.numCycles.setProperty("value", 1.0)
        self.numCycles.setObjectName("numCycles")
        self.gridLayout.addWidget(self.numCycles, 10, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(RVLoop)
        self.widget.setMinimumSize(QtCore.QSize(221, 151))
        self.widget.setMaximumSize(QtCore.QSize(293, 10000))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comment_checkBox = QtWidgets.QCheckBox(self.widget)
        self.comment_checkBox.setObjectName("comment_checkBox")
        self.verticalLayout.addWidget(self.comment_checkBox)
        self.commentBox = QtWidgets.QTextEdit(self.widget)
        self.commentBox.setEnabled(False)
        self.commentBox.setObjectName("commentBox")
        self.verticalLayout.addWidget(self.commentBox)
        self.start_Button = QtWidgets.QPushButton(self.widget)
        self.start_Button.setObjectName("start_Button")
        self.verticalLayout.addWidget(self.start_Button)
        self.stop_Button = QtWidgets.QPushButton(self.widget)
        self.stop_Button.setObjectName("stop_Button")
        self.verticalLayout.addWidget(self.stop_Button)
        self.statusbar = QtWidgets.QLineEdit(self.widget)
        self.statusbar.setEnabled(False)
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
        self.statusbar.setPalette(palette)
        self.statusbar.setText("")
        self.statusbar.setAlignment(QtCore.Qt.AlignCenter)
        self.statusbar.setReadOnly(True)
        self.statusbar.setObjectName("statusbar")
        self.verticalLayout.addWidget(self.statusbar)
        self.gridLayout_2.addWidget(self.widget, 1, 0, 1, 1)
        self.graphWidget = PlotWidget(RVLoop, viewBox=ViewBox(border=mkPen(color='k', width=2)))
        self.graphWidget.setBackground((255, 182, 193, 25))
        self.graphWidget.setMinimumSize(QtCore.QSize(411, 379))
        self.graphWidget.setObjectName("graphWidget")
        self.gridLayout_2.addWidget(self.graphWidget, 0, 1, 2, 1)

        self.retranslateUi(RVLoop)
        self.scan_speed.setCurrentIndex(3)
        self.time_unit.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(RVLoop)
        RVLoop.setTabOrder(self.file_name, self.vsource)
        RVLoop.setTabOrder(self.vsource, self.minV)
        RVLoop.setTabOrder(self.minV, self.maxV)
        RVLoop.setTabOrder(self.maxV, self.vstep)
        RVLoop.setTabOrder(self.vstep, self.pulse_width)
        RVLoop.setTabOrder(self.pulse_width, self.time_unit)
        RVLoop.setTabOrder(self.time_unit, self.scan_speed)
        RVLoop.setTabOrder(self.scan_speed, self.Ilimit)
        RVLoop.setTabOrder(self.Ilimit, self.read_voltage)
        RVLoop.setTabOrder(self.read_voltage, self.numCycles)
        RVLoop.setTabOrder(self.numCycles, self.temp_check)
        RVLoop.setTabOrder(self.temp_check, self.temperature)
        RVLoop.setTabOrder(self.temperature, self.comment_checkBox)
        RVLoop.setTabOrder(self.comment_checkBox, self.commentBox)
        RVLoop.setTabOrder(self.commentBox, self.start_Button)
        RVLoop.setTabOrder(self.start_Button, self.stop_Button)
        RVLoop.setTabOrder(self.stop_Button, self.statusbar)

    def retranslateUi(self, RVLoop):
        _translate = QtCore.QCoreApplication.translate
        RVLoop.setWindowTitle(_translate("RVLoop", "RV Loop"))
        self.Program_label.setText(_translate("RVLoop", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; color:#0000ff;\">Write Voltage Vs Read Resistance</span></p></body></html>"))
        self.setting_label.setText(_translate("RVLoop", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#aa0000;\">Settings</span></p></body></html>"))
        self.scan_speed.setItemText(0, _translate("RVLoop", "Very Slow"))
        self.scan_speed.setItemText(1, _translate("RVLoop", "Slow"))
        self.scan_speed.setItemText(2, _translate("RVLoop", "Normal"))
        self.scan_speed.setItemText(3, _translate("RVLoop", "Fast"))
        self.scan_speed.setItemText(4, _translate("RVLoop", "Very Fast"))
        self.maxV.setToolTip(_translate("RVLoop", "<html><head/><body><p>Max 10 V</p></body></html>"))
        self.time_unit.setToolTip(_translate("RVLoop", "<html><head/><body><p>Select time unit</p></body></html>"))
        self.time_unit.setItemText(0, _translate("RVLoop", "us"))
        self.time_unit.setItemText(1, _translate("RVLoop", "ms"))
        self.time_unit.setItemText(2, _translate("RVLoop", "s"))
        self.minV.setToolTip(_translate("RVLoop", "<html><head/><body><p>Max -10 V</p></body></html>"))
        self.vstep_label.setText(_translate("RVLoop", "<html><head/><body><p><span style=\" font-size:10pt;\">Voltage Step (V)</span></p></body></html>"))
        self.Ilimit_label.setText(_translate("RVLoop", "<html><head/><body><p><span style=\" font-size:10pt;\">Current Limit (mA)</span></p></body></html>"))
        self.temp_check.setToolTip(_translate("RVLoop", "<html><head/><body><p>Use temperature only if temperature controller is attached</p></body></html>"))
        self.temp_check.setText(_translate("RVLoop", "Temperature (K)"))
        self.minV_label.setText(_translate("RVLoop", "<html><head/><body><p><span style=\" font-size:10pt;\">Minimum Voltage (V)</span></p></body></html>"))
        self.maxV_label.setText(_translate("RVLoop", "<html><head/><body><p><span style=\" font-size:10pt;\">Maximum Voltage (V)</span></p></body></html>"))
        self.temperature.setToolTip(_translate("RVLoop", "<html><head/><body><p>Temperature range will depend on the type of heater</p></body></html>"))
        self.ncycles_label.setText(_translate("RVLoop", "<html><head/><body><p><span style=\" font-size:10pt;\">Read Voltage (V)</span></p></body></html>"))
        self.Ilimit.setToolTip(_translate("RVLoop", "<html><head/><body><p>The compliance current, which protects the sample from full breakdown</p></body></html>"))
        self.vpulse_lable.setText(_translate("RVLoop", "<html><head/><body><p><span style=\" font-size:10pt;\">Voltage Pulse width</span></p></body></html>"))
        self.vsource_label.setText(_translate("RVLoop", "<html><head/><body><p><span style=\" font-size:10pt;\">Voltage Source</span></p></body></html>"))
        self.scan_speed_label.setText(_translate("RVLoop", "<html><head/><body><p><span style=\" font-size:10pt;\">Scan Speed</span></p></body></html>"))
        self.vsource.setItemText(0, _translate("RVLoop", "Keysight 2902B"))
        self.vsource.setItemText(1, _translate("RVLoop", "Keithley 2450"))
        self.vsource.setItemText(2, _translate("RVLoop", "Tektronix AFG1022"))
        self.file_name.setText(_translate("RVLoop", "Sample_RV"))
        self.fname_label.setText(_translate("RVLoop", "<html><head/><body><p><span style=\" font-size:10pt;\">File Name</span></p></body></html>"))
        self.ncycles_label_2.setText(_translate("RVLoop", "<html><head/><body><p><span style=\" font-size:10pt;\">Num. Cycles</span></p></body></html>"))
        self.comment_checkBox.setText(_translate("RVLoop", "Add Comments"))
        self.start_Button.setToolTip(_translate("RVLoop", "<html><head/><body><p>Click to start the experiment</p></body></html>"))
        self.start_Button.setText(_translate("RVLoop", "START"))
        self.stop_Button.setToolTip(_translate("RVLoop", "<html><head/><body><p>Click to abort the experiment</p></body></html>"))
        self.stop_Button.setText(_translate("RVLoop", "STOP"))

class app_RVLoop(Ui_RVLoop):
    """The RV-Loop app module."""

    def __init__(self, parent=None, smu=None, k2700 = None, afg1022 = None, sName="Sample_RV.dat", connection=1):
        super(app_RVLoop, self).__init__(parent)
        self.parent = parent
        self.smu = smu
        self.k2700 = k2700
        self.afg1022 = afg1022
        self.stop_flag = False
        if self.afg1022:
            if self.afg1022.ID == 'Fake':
                self.vsource.removeItem(2) # Remove AFG source option
        else:
            self.vsource.removeItem(2) # Remove AFG source option
        if self.smu:
            if self.smu.ID == 'Fake':
                self.groupBox.setEnabled(False)
                self.statusbar.setText("Sourcemeter not connected. Reconnect and try again.")
                self.widget.setEnabled(False)
                self.graphWidget.setEnabled(False)
            elif self.smu.ID == 'B2902B':
                self.vsource.removeItem(1) # Remove Keithley SMU source option
            elif self.smu.ID == 'K2450':
                self.vsource.removeItem(0) # Remove Keysight SMU source option
        else:
            self.groupBox.setEnabled(False)
            self.statusbar.setText("Sourcemeter not connected. Reconnect and try again.")
            self.widget.setEnabled(False)
            self.graphWidget.setEnabled(False)

        self.connection = connection
        self.stop_Button.setEnabled(False)
        self.stopCall = False
        self.start_Button.clicked.connect(self.start_rvloop)
        self.stop_Button.clicked.connect(self.stop_rvLoop)
        self.start_Button.setShortcut('ctrl+Return')
        self.stop_Button.setShortcut('ctrl+q')
        self.initialize_plot()
        self.update_limits()
        self.smu.nplc = 0.01
        self.smu.readV = 0.1
        self.avg_over_n_readings = 10
        self.smu.avg = self.avg_over_n_readings
        self.filename = sName
        self.file_name.setReadOnly(True)
        self.file_name.setText(self.filename)
        self.temp_check.setEnabled(False)
        self.numCycles.setEnabled(False)
        self.measurement_status = "Idle"
        self.vsource.currentIndexChanged.connect(self.update_limits)
        self.params = {
            "Vsource": 0,
            "Vmin": -3,
            "Vmax": 3,
            "Vstep": 0.1,
            "VPwidth": 10,
            "timeunit": 1,  # 0 = us, 1=ms, 2 = s
            "Speed": 3,
            "ILimit": 1/1000,
            "Rvoltage": 0.1,
            "Ncycles": 1,
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

    def load_parameters(self):
        try:
            self.vsource.setCurrentIndex(self.parameters[0])
        except Exception as e:
            print(e)
        try:
            self.minV.setValue(self.parameters[1])
            self.maxV.setValue(self.parameters[2])
            self.vstep.setValue(self.parameters[3])
            self.pulse_width.setValue(self.parameters[4])
            self.time_unit.setCurrentIndex(self.parameters[5])
            self.scan_speed.setCurrentIndex(self.parameters[6])
            self.Ilimit.setValue(self.parameters[7]*1000)
            self.read_voltage.setValue(self.parameters[8])
            self.numCycles.setValue(self.parameters[9])
            self.temperature.setValue(self.parameters[10])
            self.temp_check.setChecked(self.parameters[11])
        except Exception as e:
            print(f"Problem with loading RV parameters. {e}")
            print("Deleting parameter file from the folder may resolve the issue.")
    def update_limits(self):
        if self.vsource.currentIndex() == 0:
            self.minV.setMaximum(190)
            self.minV.setMinimum(-190)
            self.maxV.setMaximum(190)
            self.minV.setMinimum(-190)
            self.time_unit.model().item(0).setEnabled(False)
        else:
            self.minV.setMaximum(5)
            self.minV.setMinimum(-5)
            self.maxV.setMaximum(5)
            self.minV.setMinimum(-5)
            self.time_unit.model().item(0).setEnabled(True)
    
    def update_params(self):
        """
        Update the measurement parameters.
        
            Function gen: Vlimit: +-5V, npoints < 50
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
            "Vsource": self.vsource.currentIndex(),
            "Vmin": self.minV.value(),
            "Vmax": self.maxV.value(),
            "Vstep": self.vstep.value(),
            "VPwidth": self.pulse_width.value(),
            "timeunit": self.time_unit.currentIndex(),
            "Speed": self.scan_speed.currentIndex(),
            "ILimit": self.Ilimit.value()/1000,
            "Rvoltage": self.read_voltage.value(),
            "Ncycles": self.numCycles.value(),
            "temperature": self.temperature.value(),
            "temp_check": int(self.temp_check.isChecked()),
            "comments" : formattedComment}
        self.parameters = list(self.params.values())[:-1]
        self.smu.readV = self.params["Rvoltage"]

    def plot_realtime_data(self,Data):
        """
        Plot the ith RV loop into the graph.

        Parameters
        ----------
        data : list
            R values for every applied Voltage
            i : int Loop number

        Returns
        -------
        None.

        """
        data = Data[0]
        self.currentCycle = Data[1]
        volts, resistances = hsplit(data, 2)
        volts = volts.flatten()
        resistances = abs(resistances.flatten())
        pen1 = mkPen(intColor(3 * i, values=3), width=2)
        if self.currentCycle == self.previousCycle:
            self.data_line.setData(volts, resistances)
        else:
            self.data_line = self.graphWidget.plot(volts, resistances, name=f"Cycle {self.currentCycle}",
                                                   pen=pen1)
        self.previousCycle = self.currentCycle

    def start_rvloop(self):
        """
        Begin the measurement.

        Returns
        -------
        None.

        """
        self.previousCycle = 0
        self.fullfilename = unique_filename(directory='.', prefix=self.filename, ext='dat', datetimeformat="")
        self.statusbar.setText("Measurement Running..")
        self.measurement_status = "Running"
        self.stop_flag = False
        self.graphWidget.clear()
        self.stopCall = False
        self.stop_Button.setEnabled(True)
        self.vsource.setEnabled(False)
        self.minV.setEnabled(False)
        self.maxV.setEnabled(False)
        self.vstep.setEnabled(False)
        self.pulse_width.setEnabled(False)
        self.time_unit.setEnabled(False)
        self.scan_speed.setEnabled(False)
        self.Ilimit.setEnabled(False)
        self.numCycles.setEnabled(False)
        self.read_voltage.setEnabled(False)
        self.start_Button.setEnabled(False)
        self.update_params()
        self.startThread()
        self.initialize_SMU()
        self.configure_sweep()
        self.smu.enable_source()
        self.plot_realtime_data()

    def startThread(self):
        self.thread = QThread()
        self.worker = Worker(self.params, self.smu, self.k2700, self.fullfilename, self.connection)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.start_RV)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.data.connect(self.plot_realtime_data)
        self.thread.finished.connect(self.finishAction)
        self.thread.finished.connect(self.finishAction)
        self.thread.start()

    def stop_rvloop(self):
        """
        Trigger to stop the IV measurement.

        Returns
        -------
        None.

        """
        self.statusbar.setText("Measurement Aborted!")
        self.measurement_status = "Aborted"
        self.stop_flag = True
        self.worker.stopcall.emit()

    def initialize_plot(self):
        """
        Initialize the plot to display IV loop.

        Returns
        -------
        None.

        """
        styles = {'color': 'r', 'font-size': '20px'}
        self.graphWidget.setLabel('left', 'Resistance (Ohms)', **styles)
        self.graphWidget.setLabel('bottom', 'Voltage (V)', **styles)
        self.graphWidget.addLegend()

    def stop_rvLoop(self):
        self.statusbar.setText("Measurement Aborted!")
        self.measurement_status = "Aborted"
        self.stop_flag = True
        self.worker.stopcall.emit()
        
    def finishAction(self):
        """
        Trigger to stop the RV measurement.

        Returns
        -------
        None.

        """
        if not self.stop_flag:
            self.measurement_status = "Idle"
            self.statusbar.setText("Measurement Finished.")
            self.stop_flag = True
        self.stop_Button.setEnabled(False)
        self.start_Button.setEnabled(True)
        self.vsource.setEnabled(True)
        self.minV.setEnabled(True)
        self.maxV.setEnabled(True)
        self.vstep.setEnabled(True)
        self.pulse_width.setEnabled(True)
        self.time_unit.setEnabled(True)
        self.scan_speed.setEnabled(True)
        self.Ilimit.setEnabled(True)
        self.numCycles.setEnabled(True)
        self.read_voltage.setEnabled(True)
        MessageBeep()

    def keyPressEvent(self, event):
        """Close application from escape key.

        results in QMessageBox dialog from closeEvent
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
            reply = QMessageBox.question(self, 'Message', quit_msg, QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.stopCall = True
        if reply == QMessageBox.Yes:
            if __name__ != "__main__":
                self.parent.show()
            event.accept()
        else:
            event.ignore()


class Worker(QObject):
    finished = pyqtSignal()
    data = pyqtSignal(list)
    stopcall = pyqtSignal()

    def __init__(self, params, smu=None, k2700=None, fullfilename="sample.dat", connection=1):
        super(Worker, self).__init__()
        self.stopCall = False
        self.params = params
        self.smu = smu
        if self.smu.ID == 'B2902B':
            # TODO: implement average_over_n_readings for B2902B SMU
            self.smu.avg = 1 # currently only 1 reading will be taken for read resistance per point
        self.k2700 = k2700
        self.connection = connection
        self.fullfilename = fullfilename
        self.stopcall.connect(self.stopcalled)
        self.smu.nplc = 1
        self.status = 1
        self.npoints = int(
            (self.params["Vmax"] - self.params["Vmin"]) / (self.params["Vstep"])) * 2 + 1
        if self.params["VPwidth"] == 0:
            self.params["VPwidth"] = 1
            self.params["timeunit"] = 0
        if self.params["timeunit"] == 0:
            self.pulse_width = self.params["VPwidth"]*1e-6
        elif self.params["timeunit"] == 1:
            self.pulse_width = self.params["VPwidth"]*1e-3
        elif self.params["timeunit"] == 2:
            self.pulse_width = self.params["VPwidth"]

    def initialize_SMU(self):
        """
        Initialize the SMU.

        Returns
        -------
        None.

        """
        if self.smu is None:
            self.smu = FakeAdapter()
        self.smu.reset()
        if self.params["Speed"] == 0:
            nplc = 5
            self.speed = "Very Slow"
        elif self.params["Speed"] == 1:
            nplc = 2
            self.speed = "Slow"
        elif self.params["Speed"] == 2:
            nplc = 1
            self.speed = "Normal"
        elif self.params["Speed"] == 3:
            nplc = 0.1
            self.speed = "Fast"
        elif self.params["Speed"] == 4:
            nplc = 0.01
            self.speed = "Very Fast"
        self.smu.apply_voltage(compliance_current=self.params["ILimit"])
        self.smu.measure_current()
        self.smu.auto_range_sense()
        self.smu.set_wire_configuration(self.smu.wire_config)  # two wire configuration
        self.smu.set_read_back_on()
        self.smu.set_zero_correct_on()
        self.smu.display_light('OFF')

    def configure_sweep(self):
        """
        Configure the sweep conditions based on given parameters.

        Returns
        -------
        None.

        """
        if self.params["Vsource"] == 0:
            # For SMU
            with open(self.fullfilename, "w", newline='') as f:
                if self.smu.ID == 'K2450':
                    f.write("##Pulse voltage source: Keithley 2450 source-measure unit.\n")
                    f.write("##Resistance read using Keithley 2450 source-measure unit.\n")
                elif self.smu.ID = 'B2902B':
                    f.write(f"##Pulse voltage source: Keysight B2902B source-measure unit (channel-{self.smu.ch}).\n")
                    f.write(f"##Resistance read using Keysight B2902B source-measure unit (channel-{self.smu.ch}).\n")
                f.write(f"## Date & Time: {datetime.now().strftime('%m/%d/%Y; %H:%M:%S')}\n")
                f.write("##Min voltage = {0}, Max Voltage = {1}.\n".format(self.params["Vmin"], self.params["Vmax"]))
                f.write(f"##Pulse width = {self.timestep}s, Num. cycles = {self.params['Ncycles']}\n")
                f.write(f"##Read voltage = {self.params['Rvoltage']}V, "
                        f"averaged over {self.smu.avg} readings\n")
                f.write("##Limiting current = {}mA\n".format(self.params["ILimit"] * 1000))
                f.write(self.params["comments"])
                if self.smu.ID == 'K2450':
                    f.write(f"#Set Voltage(V)\tActual Volts applied(V)\tSet Current(A)\t"
                            f"Read Current at {self.params['Rvoltage']}V\t"
                            f"Read Resistance at {self.params['Rvoltage']}V (Ω)\n")
                elif self.smu.ID == 'B2450':
                    f.write(f"#Set Voltage(V)\tActual Volts applied(V)\tSet Current(A)\t"
                            f"Read Current at {self.params['Rvoltage']}V\t"
                            f"Read Resistance at {self.params['Rvoltage']}V (Ω)\t"
                            f"Time Stamp (s)\n")
        else:
            # For AGF
            with open(self.fullfilename, "w", newline='') as f:
                f.write("##Pulse voltage source: Tektronix AFG1022 MultiFunction Generator.\n")
                if self.smu.ID == 'K2450':
                    f.write("##Resistance read using Keithley 2450 source-measure unit.\n")
                elif self.smu.ID == 'B2902B':
                    f.write("##Resistance read using Keysight B2902B source-measure unit.\n")
                f.write(f"##Date & Time: {datetime.now().strftime('%m/%d/%Y; %H:%M:%S')}\n")
                f.write(f"##Min voltage = {self.params['Vmin']}, Max Voltage = {self.params['Vmax']}.\n")
                f.write(f"##Pulse width = {self.timestep}s, Num. cycles = {self.params['Ncycles']}\n")
                f.write(f"##Read voltage = {self.params['Rvoltage']}V, "
                        f"averaged over {self.smu.avg} readings\n")
                f.write("##Limiting current = {}mA\n".format(self.params["Ilimit"] * 1000))
                f.write(self.params["comments"])
                f.write(f"#Set Voltage(V)\tRead Current at {self.params['Rvoltage']}V\t"
                        f"Read Resistance at {self.params['Rvoltage']}V (Ω)\n")

        l1 = linspace(self.params["Vmax"], self.params["Vmin"], int(
            self.npoints / 2), endpoint=False)
        l2 = linspace(self.params["Vmin"], self.params["Vmax"], int(
            self.npoints / 2) + 1, endpoint=True)
        self.points = around(concatenate((l1, l2)), 4)
        self.points[self.points == 0] = 0.0001
        if self.smu.ID == 'B2902B':
            voltages = ",".join(self.points.astype('str'))
            self.smu.configure_pulse_sweep(voltages,
                                           baseV=self.params["Rvoltage"],
                                           pulse_width=self.pulse_width)

    def measure_RV_B2902b(self):
        self.smu.clear_buffer((self.smu.avg+1)*self.npoints)
        self.smu.start_buffer()
        number_of_data_per_point = 4
        while self.smu.get_trigger_state() == 'RUNNING':
            sleep(0.2)
            data = smu.ask(":TRAC:Data?")
            data2 = reshape(array(data.split(','), dtype=float), (-1, number_of_data_per_point))
            writeData = data2[::self.smu.avg+1].copy()
            if self.smu.avg == 1:
                readData = data2[1::2].copy()
            else:
                readData = data2[np.mod(np.arange(data2.shape[0]), self.smu.avg+1) != 0]
                readData = reshape(readData,(-1,self.smu.avg,number_of_data_per_point))
                readData = mean(readData,axis=1)
            volts = writeData[:, 3]
            read_currents = readData[:, 1]
            resistances = self.params["Rvoltage"] / read_currents
            self.data.emit(volts,resistances)
        volts = writeData[:, 3]
        read_currents = readData[:, 1]
        resistances = self.params["Rvoltage"] / read_currents
        self.data.emit(volts, resistances)
        actual_setVolts = writeData[:,0]
        set_currents = writeData[:,1]
        time_stamp = writeData[:,2]
        data = np.array((volts, actual_setVolts, set_currents, read_currents, resistances,time_stamp))
        return data

    def measure_RV_K2450(self):
        """
        Initiate the measurement of one data point.

        Returns
        -------
        None.

        """
        i = 0
        while i < self.npoints or not self.stopCall:
            self.smu.setNPLC(0.01)
            self.smu.set_simple_loop(delayTime=self.timestep)
            self.smu.source_voltage = self.points[i]
            self.smu.start_buffer()
            self.wait_till_done(1)
            setData = self.smu.get_trace_data(1, 1)
            setData = array(setData.split(','), dtype=float)
            v, c = setData[0], setData[1]
            self.actual_setVolts.append(v)
            self.set_currents.append(c)
            self.smu.setNPLC()
            self.smu.set_simple_loop(count=self.smu.avg)
            self.smu.source_voltage = self.params["Rvoltage"]
            self.smu.start_buffer()
            self.wait_till_done()
            self.read_currents.append(self.smu.get_average_trace_data())
            if self.read_currents[i] == 0:
                self.read_currents[i] = 1e-20
            self.volts.append(self.points[i])
            self.resistances.append(
                self.params["Rvoltage"]/self.read_currents[i])
            self.data.emit([self.volts, self.resistances],self.cycleNum)
            i = i + 1
        data = np.array((self.volts,self.actual_setVolts,self.set_currents,self.read_currents,self.resistances))
        return data

    def measure_RV_AFG(self):
        """
        Initiate the measurement of one data point.

        Returns
        -------
        None.

        """
        i = 0
        while i < self.npoints or not self.stopCall:
            self.afg1022.setSinglePulse(self.points[i],self.timestep)
            self.afg1022.trgNwait()
            #self.set_currents.append(c)
            if self.connection == 1:
                self.k2700.open_Channels(AFG) # disconnect function generator
                self.k2700.close_Channels(SMU) # connect SMU
            elif self.connection == 2:
                self.k2700.open_Channels(AFG+10) # disconnect function generator
                self.k2700.close_Channels(SMU+10) # connect SMU
            sleep(0.2) # wait for 200msec to ensure switching is complete
            self.smu.start_buffer()
            self.wait_till_done()
            self.read_currents.append(self.smu.get_average_trace_data())
            if self.read_currents[i] == 0:
                self.read_currents[i] = 1e-11
            self.volts.append(self.points[i])
            self.resistances.append(
                self.params["Rvoltage"]/self.read_currents[i])
            self.data.emit([self.volts, self.resistances],self.cycleNum)
            i = i + 1
        data = np.array((self.volts, self.read_currents, self.resistances))
        return data

    def start_RV(self):
        self.initialize_SMU()
        self.configure_sweep()
        self.smu.enable_source()
        self.cycleNum = 0
        if self.params["Vsource"] == 0:
            connect_sample_with_SMU(self.k2700, self.connection)
        else:
            if self.connection == 1:
                self.k2700.open_Channels(SMU)  # Disconnect SMU
                self.k2700.open_Channels(AFG + 10)  # connect AFG
                self.k2700.close_Channels(AFG)  # connect AFG
            elif self.connection == 2:
                self.k2700.open_Channels(SMU + 10)  # Disconnect SMU
                self.k2700.open_Channels(AFG)  # connect AFG
                self.k2700.close_Channels(AFG + 10)  # connect AFG
            sleep(0.2)  # wait for 200msec to ensure switching is complete
        while self.cycleNum < self.params["ncycles"] and not self.stopCall:
            self.volts = []
            self.actual_setVolts = []
            self.set_currents = []
            self.read_currents = []
            self.resistances = []
            if self.params["Vsource"] == 0:
                if self.smu.ID == 'K2450':
                    data = self.measure_RV_K2450()
                elif self.smu.ID == 'B2902B':
                    data = self.measure_RV_B2902b()
            else:
                #TODO: check if this works with B2902B
                self.smu.setNPLC()
                self.smu.set_simple_loop(self.smu.avg)
                self.smu.source_voltage = self.params["Rvoltage"]
                data = self.measure_RV_AFG()
            self.cycleNum = self.cycleNum + 1
        with open(self.fullfilename, "a") as f:
            f.write(f"#Cycle {self.cycleNum + 1}\n")
            savetxt(f, data.T, delimiter='\t')
            f.write("\n\n")

    def wait_till_done(self):
        """
        Wait until the measurement is completed.

        Infinite loop runs until the 'state' is not 'RUNNING'

        Returns
        -------
        int
            1: if the measurement has successfully finished
            0: if there is some error
        """
        while True:  # wait for measurement to complete
            sleep(0.1) # wait for 100 ms
            state = self.smu.get_trigger_state()
            if state == 'IDLE':
                return 1
            elif state not in ('RUNNING', 'BUILDING'):
                return 0

    def stop_program(self):
        if self.stopCall:
            self.smu.abort()
        self.smu.source_voltage = 0
        self.smu.disable_source()
        self.finished.emit()

    def stopcalled(self):
        self.stopCall = True


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RVLoop = QtWidgets.QWidget()
    smu, k2700, afg1022 = checkInstrument(test = True)
    ui = app_RVLoop(RVLoop, smu, k2700, afg1022)
    ui.show()
    app.exec_()
    app.quit()