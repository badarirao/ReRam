"""
The Switch module of the ReRam project.

    Contains the GUI for switching experiment,
    associated functions to set parameters, make measurement, and save the data
    You can apply customized pulses, and observe how resistance changes
    
    TODO: Check if enough time is provided after switching
    TODO: Ensure only new data is saved into the file.
    TODO: Add tooltips

"""

from csv import writer
from os.path import exists as fileExists
from winsound import MessageBeep
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPalette, QColor, QBrush
from PyQt5.QtCore import Qt
from pyqtgraph import GraphicsLayoutWidget, ViewBox, mkPen
from utilities import unique_filename, FakeAdapter, checkInstrument, AFG, SMU
from utilities import connect_sample_with_SMU, connect_sample_with_AFG
from utilities import waitFor

class Ui_Switch(QtWidgets.QWidget):
    """The pyqt5 gui class for switching experiment."""

    def __init__(self, parent=None):
        super(Ui_Switch, self).__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)

    def setupUi(self, Switch):
        """
        Draw and initialize the measurement screen.

        Code generated by QT Designer.

        Parameters
        ----------
        RVLoop : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        Switch.setObjectName("Switch")
        Switch.resize(1050, 650)
        Switch.setMinimumSize(QtCore.QSize(1050, 650))
        self.gridLayout_2 = QtWidgets.QGridLayout(Switch)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(Switch)
        self.widget.setMinimumSize(QtCore.QSize(350, 0))
        self.widget.setMaximumSize(QtCore.QSize(350, 16777215))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title_label = QtWidgets.QLabel(self.widget)
        self.title_label.setMinimumSize(QtCore.QSize(0, 24))
        self.title_label.setMaximumSize(QtCore.QSize(16777215, 100))
        self.title_label.setObjectName("title_label")
        self.verticalLayout_2.addWidget(self.title_label)
        self.setting_label = QtWidgets.QLabel(self.widget)
        self.setting_label.setMinimumSize(QtCore.QSize(0, 24))
        self.setting_label.setMaximumSize(QtCore.QSize(16777215, 100))
        self.setting_label.setObjectName("setting_label")
        self.verticalLayout_2.addWidget(self.setting_label)
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.avg = QtWidgets.QSpinBox(self.frame)
        self.avg.setMaximumSize(QtCore.QSize(50, 20))
        self.avg.setAlignment(QtCore.Qt.AlignRight |
                              QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.avg.setMinimum(1)
        self.avg.setMaximum(1000)
        self.avg.setProperty("value", 5)
        self.avg.setObjectName("avg")
        self.horizontalLayout_4.addWidget(self.avg)
        self.avgread_label = QtWidgets.QLabel(self.frame)
        self.avgread_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.avgread_label.setObjectName("avgread_label")
        self.horizontalLayout_4.addWidget(self.avgread_label)
        self.gridLayout.addLayout(self.horizontalLayout_4, 8, 2, 1, 1)
        self.reset_pulseWidth_label = QtWidgets.QLabel(self.frame)
        self.reset_pulseWidth_label.setObjectName("reset_pulseWidth_label")
        self.gridLayout.addWidget(self.reset_pulseWidth_label, 6, 1, 1, 1)
        self.Ilimit = QtWidgets.QDoubleSpinBox(self.frame)
        self.Ilimit.setDecimals(3)
        self.Ilimit.setMaximum(500.0)
        self.Ilimit.setSingleStep(0.001)
        self.Ilimit.setProperty("value", 1.0)
        self.Ilimit.setObjectName("Ilimit")
        self.gridLayout.addWidget(self.Ilimit, 10, 2, 1, 1)
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
        self.read_voltage = QtWidgets.QDoubleSpinBox(self.frame)
        self.read_voltage.setDecimals(3)
        self.read_voltage.setMaximum(10.0)
        self.read_voltage.setMinimum(-10.0)
        self.read_voltage.setSingleStep(0.1)
        self.read_voltage.setProperty("value", 0.1)
        self.read_voltage.setObjectName("read_voltage")
        self.gridLayout.addWidget(self.read_voltage, 7, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.Ilimit_label = QtWidgets.QLabel(self.frame)
        self.Ilimit_label.setObjectName("Ilimit_label")
        self.gridLayout.addWidget(self.Ilimit_label, 10, 1, 1, 1)
        self.temp_check = QtWidgets.QCheckBox(self.frame)
        self.temp_check.setObjectName("temp_check")
        self.gridLayout.addWidget(self.temp_check, 12, 1, 1, 1)
        self.ncycles_label = QtWidgets.QLabel(self.frame)
        self.ncycles_label.setObjectName("ncycles_label")
        self.gridLayout.addWidget(self.ncycles_label, 7, 1, 1, 1)
        self.temperature = QtWidgets.QDoubleSpinBox(self.frame)
        self.temperature.setEnabled(False)
        self.temperature.setMaximum(600.0)
        self.temperature.setProperty("value", 300.0)
        self.temperature.setObjectName("temperature")
        self.gridLayout.addWidget(self.temperature, 12, 2, 1, 1)
        self.maxV_label = QtWidgets.QLabel(self.frame)
        self.maxV_label.setObjectName("maxV_label")
        self.gridLayout.addWidget(self.maxV_label, 5, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.maxV = QtWidgets.QDoubleSpinBox(self.frame)
        self.maxV.setDecimals(3)
        self.maxV.setMinimum(-49.0)
        self.maxV.setMaximum(50.0)
        self.maxV.setSingleStep(0.001)
        self.maxV.setProperty("value", -3.0)
        self.maxV.setObjectName("maxV")
        self.horizontalLayout_3.addWidget(self.maxV)
        self.maxV_check = QtWidgets.QCheckBox(self.frame)
        self.maxV_check.setMaximumSize(QtCore.QSize(20, 16777215))
        self.maxV_check.setText("")
        self.maxV_check.setChecked(True)
        self.maxV_check.setObjectName("maxV_check")
        self.horizontalLayout_3.addWidget(self.maxV_check)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 2, 1, 1)
        self.avg_label = QtWidgets.QLabel(self.frame)
        self.avg_label.setObjectName("avg_label")
        self.gridLayout.addWidget(self.avg_label, 8, 1, 1, 1)
        self.minV_label = QtWidgets.QLabel(self.frame)
        self.minV_label.setObjectName("minV_label")
        self.gridLayout.addWidget(self.minV_label, 3, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.minV = QtWidgets.QDoubleSpinBox(self.frame)
        self.minV.setDecimals(3)
        self.minV.setMinimum(-50.0)
        self.minV.setMaximum(49.0)
        self.minV.setSingleStep(0.1)
        self.minV.setProperty("value", 3.0)
        self.minV.setObjectName("minV")
        self.horizontalLayout_2.addWidget(self.minV)
        self.minV_check = QtWidgets.QCheckBox(self.frame)
        self.minV_check.setMaximumSize(QtCore.QSize(20, 16777215))
        self.minV_check.setText("")
        self.minV_check.setChecked(True)
        self.minV_check.setObjectName("minV_check")
        self.horizontalLayout_2.addWidget(self.minV_check)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 2, 1, 1)
        self.fname_label = QtWidgets.QLabel(self.frame)
        self.fname_label.setObjectName("fname_label")
        self.gridLayout.addWidget(self.fname_label, 1, 1, 1, 1)
        self.file_name = QtWidgets.QLineEdit(self.frame)
        self.file_name.setObjectName("file_name")
        self.gridLayout.addWidget(self.file_name, 1, 2, 1, 1)
        self.source = QtWidgets.QComboBox(self.frame)
        self.source.setObjectName("source")
        self.source.addItem("")
        self.source.addItem("")
        self.gridLayout.addWidget(self.source, 2, 2, 1, 1)
        self.set_pulseWidth_label = QtWidgets.QLabel(self.frame)
        self.set_pulseWidth_label.setObjectName("set_pulseWidth_label")
        self.gridLayout.addWidget(self.set_pulseWidth_label, 4, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.set_pulseWidth = QtWidgets.QDoubleSpinBox(self.frame)
        self.set_pulseWidth.setDecimals(1)
        self.set_pulseWidth.setMaximum(1000.0)
        self.set_pulseWidth.setProperty("value", 50.0)
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
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 9, 1, 1, 1)
        self.nPulses = QtWidgets.QSpinBox(self.frame)
        self.nPulses.setMaximum(1000)
        self.nPulses.setProperty("value", 1)
        self.nPulses.setObjectName("nPulses")
        self.gridLayout.addWidget(self.nPulses, 9, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        self.graphWidget = GraphicsLayoutWidget(Switch)
        self.graphWidget.setBackground((255, 182, 193, 25))
        self.Rplot = self.graphWidget.addPlot(
            row=0, col=0, viewBox=ViewBox(border=mkPen(color='k', width=2)))
        self.Vplot = self.graphWidget.addPlot(
            row=1, col=0, viewBox=ViewBox(border=mkPen(color='k', width=2)))
        self.graphWidget.setMinimumSize(QtCore.QSize(411, 379))
        self.graphWidget.setObjectName("graphWidget")
        self.gridLayout_2.addWidget(self.graphWidget, 0, 1, 2, 1)
        self.widget1 = QtWidgets.QWidget(Switch)
        self.widget1.setMinimumSize(QtCore.QSize(350, 151))
        self.widget1.setMaximumSize(QtCore.QSize(350, 154))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.applyPulse_Button = QtWidgets.QPushButton(self.widget1)
        self.applyPulse_Button.setObjectName("applyPulse_Button")
        self.verticalLayout.addWidget(self.applyPulse_Button)
        self.clearGraph_Button = QtWidgets.QPushButton(self.widget1)
        self.clearGraph_Button.setObjectName("clearGraph_Button")
        self.verticalLayout.addWidget(self.clearGraph_Button)
        self.save_Button = QtWidgets.QPushButton(self.widget1)
        self.save_Button.setObjectName("save_Button")
        self.verticalLayout.addWidget(self.save_Button)
        self.stop_Button = QtWidgets.QPushButton(self.widget1)
        self.stop_Button.setObjectName("stop_Button")
        self.verticalLayout.addWidget(self.stop_Button)
        self.statusbar = QtWidgets.QLineEdit(self.widget1)
        self.statusbar.setEnabled(False)
        palette = QPalette()
        brush = QBrush(QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush = QBrush(QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush = QBrush(QColor(170, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        self.statusbar.setPalette(palette)
        self.statusbar.setText("")
        self.statusbar.setAlignment(QtCore.Qt.AlignCenter)
        self.statusbar.setReadOnly(True)
        self.statusbar.setObjectName("statusbar")
        self.verticalLayout.addWidget(self.statusbar)
        self.gridLayout_2.addWidget(self.widget1, 1, 0, 1, 1)

        self.retranslateUi(Switch)
        self.reset_timeUnit.setCurrentIndex(1)
        self.set_timeUnit.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Switch)

    def retranslateUi(self, Switch):
        """
        Code generated by QT Designer.

        Parameters
        ----------
        IVLoop : Qwidget

        Returns
        -------
        None.

        """
        _translate = QtCore.QCoreApplication.translate
        Switch.setWindowTitle(_translate("Switch", "Switch Test"))
        self.title_label.setText(_translate(
            "Switch", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#0000ff;\">Switching Test</span></p></body></html>"))
        self.setting_label.setText(_translate(
            "Switch", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#aa0000;\">Settings</span></p></body></html>"))
        self.avgread_label.setText(_translate(
            "Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Readings</span></p></body></html>"))
        self.reset_pulseWidth_label.setText(_translate(
            "Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Pulse width (Reset)</span></p></body></html>"))
        self.Ilimit.setToolTip(_translate(
            "Switch", "<html><head/><body><p>The compliance current, which protects the sample from full breakdown</p></body></html>"))
        self.reset_timeUnit.setToolTip(_translate(
            "Switch", "<html><head/><body><p>Select time unit. Time below 50 ms may not be reliable for Keithley 2450</p></body></html>"))
        self.reset_timeUnit.setItemText(0, _translate("Switch", "µs"))
        self.reset_timeUnit.setItemText(1, _translate("Switch", "ms"))
        self.reset_timeUnit.setItemText(2, _translate("Switch", "s"))
        self.label.setText(_translate(
            "Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Voltage Source</span></p></body></html>"))
        self.Ilimit_label.setText(_translate(
            "Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Current Limit (mA)</span></p></body></html>"))
        self.temp_check.setToolTip(_translate(
            "Switch", "<html><head/><body><p>Use temperature only if temperature controller is attached</p></body></html>"))
        self.temp_check.setText(_translate("Switch", "Temperature (K)"))
        self.ncycles_label.setText(_translate(
            "Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Read Voltage (V)</span></p></body></html>"))
        self.temperature.setToolTip(_translate(
            "Switch", "<html><head/><body><p>Temperature range will depend on the type of heater</p></body></html>"))
        self.maxV_label.setText(_translate(
            "Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Reset Voltage (V)</span></p></body></html>"))
        self.maxV.setToolTip(_translate(
            "Switch", "<html><head/><body><p>Max 10 V</p></body></html>"))
        self.avg_label.setText(_translate(
            "Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Average over</span></p></body></html>"))
        self.minV_label.setText(_translate(
            "Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Set Voltage (V)</span></p></body></html>"))
        self.minV.setToolTip(_translate(
            "Switch", "<html><head/><body><p>Max -10 V</p></body></html>"))
        self.fname_label.setText(_translate(
            "Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">File Name</span></p></body></html>"))
        self.file_name.setText(_translate("Switch", "sample.txt"))
        self.source.setItemText(0, _translate("Switch", "Keithley 2450"))
        self.source.setItemText(1, _translate("Switch", "Tektronix AFG1022"))
        self.set_pulseWidth_label.setText(_translate(
            "Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Pulse Width (Set)</span></p></body></html>"))
        self.set_timeUnit.setToolTip(_translate(
            "Switch", "<html><head/><body><p>Select time unit. Time below 50 ms may not be reliable for Keithley 2450</p></body></html>"))
        self.set_timeUnit.setItemText(0, _translate("Switch", "µs"))
        self.set_timeUnit.setItemText(1, _translate("Switch", "ms"))
        self.set_timeUnit.setItemText(2, _translate("Switch", "s"))
        self.label_2.setText(_translate(
            "Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Number of pulses</span></p></body></html>"))
        self.applyPulse_Button.setToolTip(_translate(
            "Switch", "<html><head/><body><p>Click to start the experiment</p></body></html>"))
        self.applyPulse_Button.setText(_translate("Switch", "Apply Pulse"))
        self.clearGraph_Button.setToolTip(_translate(
            "Switch", "<html><head/><body><p>Click to save current data and start new set of measurement. Example, for new sample.</p></body></html>"))
        self.clearGraph_Button.setText(_translate(
            "Switch", "Clear graph and start new measurement"))
        self.save_Button.setText(_translate("Switch", "Save Data"))
        self.stop_Button.setText(_translate("Switch", "Stop"))

class app_Switch(Ui_Switch):
    """The Switch app module."""

    def __init__(self, parent=None, k2450=None, k2700 = None, afg1022 = None, sName="Sample_Switch.csv"):
        super(app_Switch, self).__init__(parent)
        self.parent = parent
        self.new_flag = True
        self.savedFlag = True
        self.initial_source = 0 # 0 = SMU, 1 = AFG
        self.k2450 = k2450
        self.k2700 = k2700
        self.afg1022 = afg1022
        self.save_Button.setEnabled(False)
        self.stop_Button.setEnabled(False)
        self.clearGraph_Button.setEnabled(False)
        self.applyPulse_Button.clicked.connect(self.applyPulse)
        self.clearGraph_Button.clicked.connect(self.clearGraph)
        self.save_Button.clicked.connect(self.saveData)
        self.stop_Button.clicked.connect(self.stopSwitch)
        self.applyPulse_Button.setShortcut('ctrl+Return')
        self.save_Button.setShortcut('ctrl+s')
        self.clearGraph_Button.setShortcut('ctrl+g')
        self.stop_Button.setShortcut('ctrl+q')
        self.minV_check.stateChanged.connect(self.change_setV)
        self.maxV_check.stateChanged.connect(self.change_resetV)
        self.source.currentIndexChanged.connect(self.update_limits)
        self.initialize_plot()
        self.update_limits()
        self.stopCall = False
        self.measurement_status = "Idle"
        self.k2450.nplc = 1
        self.k2450.avg = 5
        self.k2450.readV = 0.1
        self.filename = self.fullfilename = sName
        self.file_name.setText(self.filename)
        self.file_name.setReadOnly(True)
        self.params = {
            "Vsource": 0, # 0 = SMU, 1 = AFG
            "Vset": 3,
            "VsetCheck": 1,
            "setPwidth": 50,
            "set_timeUnit": 1,  # 0 = us, 1=ms, 2 = s
            "Vreset": -3,
            "VresetCheck": 1,
            "resetPwidth": 50,
            "reset_timeUnit": 1,  # 0 = us, 1=ms, 2 = s
            "Rvoltage": 0.1,
            "Average": 5,
            "nPulses": 1,
            "ILimit": 1/1000,
            "temperature": 300,
            "temp_check": 0}
        self.parameters = list(self.params.values())
    
    def update_limits(self):
        if self.source.currentIndex() == 0:
            self.minV.setMaximum(190)
            self.minV.setMinimum(-190)
            self.maxV.setMaximum(190)
            self.maxV.setMinimum(-190)
            if self.set_timeUnit.currentIndex() == 0:
                self.set_timeUnit.setCurrentIndex(1)
            self.set_timeUnit.model().item(0).setEnabled(False)
            if self.reset_timeUnit.currentIndex() == 0:
                self.reset_timeUnit.setCurrentIndex(1)
            self.reset_timeUnit.model().item(0).setEnabled(False)
            self.nPulses.setMaximum(1000)
        else:
            self.minV.setMaximum(5)
            self.minV.setMinimum(-5)
            self.maxV.setMaximum(5)
            self.maxV.setMinimum(-5)
            self.set_timeUnit.model().item(0).setEnabled(True)
            self.reset_timeUnit.model().item(0).setEnabled(True)
            self.nPulses.setMaximum(20)
            
    def change_setV(self):
        """
        Enable or disable 'set' pulse based on user preference.

        Returns
        -------
        None.

        """
        if self.minV_check.isChecked():
            self.minV.setEnabled(True)
        else:
            self.minV.setEnabled(False)

    def change_resetV(self):
        """
        Enable or disable 'reset' pulse based on user preference.

        Returns
        -------
        None.

        """
        if self.maxV_check.isChecked():
            self.maxV.setEnabled(True)
        else:
            self.maxV.setEnabled(False)
    
    def load_parameters(self):
        try:
            self.source.setCurrentIndex(self.parameters[0])
            self.minV.setValue(self.parameters[1]),
            self.minV_check.setChecked(self.parameters[2]),
            self.set_pulseWidth.setValue(self.parameters[3]),
            self.set_timeUnit.setCurrentIndex(self.parameters[4]),
            self.maxV.setValue(self.parameters[5]),
            self.maxV_check.setChecked(self.parameters[6]),
            self.reset_pulseWidth.setValue(self.parameters[7]),
            self.reset_timeUnit.setCurrentIndex(self.parameters[8]),
            self.read_voltage.setValue(self.parameters[9]),
            self.avg.setValue(self.parameters[10]),
            self.nPulses.setValue(self.parameters[11]),
            self.Ilimit.setValue(self.parameters[12]*1000),
            self.temperature.setValue(self.parameters[13]),
            self.temp_check.setChecked(self.parameters[14])
        except Exception:
            pass
    
    def configurePulse(self):
        """
        Configure the pulse parameters.

        Returns
        -------
        None.

        """
        self.params = {
            "Vsource": self.source.currentIndex(),
            "Vset": self.minV.value(),
            "VsetCheck": self.minV_check.checkState(),
            "setPwidth": self.set_pulseWidth.value(),
            "set_timeUnit": self.set_timeUnit.currentIndex(),
            "Vreset": self.maxV.value(),
            "VresetCheck": self.maxV_check.checkState(),
            "resetPwidth": self.reset_pulseWidth.value(),
            "reset_timeUnit": self.reset_timeUnit.currentIndex(),
            "Rvoltage": self.read_voltage.value(),
            "Average": self.avg.value(),
            "nPulses": self.nPulses.value(),
            "ILimit": self.Ilimit.value()/1000,
            "temperature": self.temperature.value(),
            "temp_check": int(self.temp_check.isChecked())}
        self.parameters = list(self.params.values())
        self.k2450.readV = self.params["Rvoltage"]
        self.k2450.avg = self.params["Average"]
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
        self.points = []
        for _ in range(self.params["nPulses"]):
            if self.params["VsetCheck"]:
                self.points.append(self.params["Vset"])
            if self.params["VresetCheck"]:
                self.points.append(self.params["Vreset"])
            if not self.params["VsetCheck"] and not self.params["VresetCheck"]:
                self.points.append(0)
        # set compliance current
        self.k2450.write("source:voltage:ilimit {0}".format(self.params["ILimit"]))
        # when function generator is used, limit number of pulses to 10
        # This is to avoid using the multiplexer too much, as it has finite lifetime
        if self.params["Vsource"] == 1:
            if self.params["nPulses"] > 10:
                self.params["nPulses"] = 10

    def initialize_SMU(self):
        """
        Initialize the SMU.

        Returns
        -------
        None.

        """
        if self.k2450 is None:
            self.k2450 = FakeAdapter()
        self.k2450.apply_voltage(compliance_current=self.params["ILimit"])
        self.k2450.measure_current(nplc=self.k2450.nplc)
        self.k2450.write("SENS:curr:rsen OFF")  # two wire configuration
        self.k2450.write(":DISPlay:LIGHT:STATe ON25")
        self.k2450.write("sour:volt:read:back 1")

    def pulseMeasure_SMU(self):
        """
        Apply and measure one pulse.

        Returns
        -------
        None.

        """
        if self.points[self.i] == self.params["Vset"]:
            self.timestep = self.setTimestep
        elif self.points[self.i] == self.params["Vreset"]:
            self.timestep = self.resetTimestep
        elif self.points[self.i] == 0:
            self.timestep = self.setTimestep+self.resetTimestep
        # apply pulse and measure pulse resistance
        if self.timestep > 0 and self.points[self.i] != 0:
            v1, c1 = self.k2450.apply_switch_pulse(self.points[self.i],self.timestep)
        else:
            waitFor(self.timestep*1000)
            v1 = 0
            c1 = -1
        # measure read resistance
        self.k2450.write("SENSe:CURRent:NPLCycles {0}".format(self.k2450.nplc))
        self.k2450.write("TRIG:LOAD 'SimpleLoop', {0}, 0".format(self.params["Average"]))
        self.k2450.source_voltage = self.params["Rvoltage"]
        self.k2450.start_buffer()
        self.k2450.wait_till_done()
        c2 = float(self.k2450.ask("TRAC:stat:average?")[:-1])
        self.volts.append(v1)
        if self.pulsecount == []:
            self.pulsecount = [1]
        else:
            self.pulsecount.append(self.pulsecount[-1]+1)
        self.currents.append(c1)
        self.resistances.append(v1/c1)
        self.readVolts.append(self.params["Rvoltage"])
        self.readCurrents.append(c2)
        self.readResistances.append(self.params["Rvoltage"]/c2)
        self.pulseWidths.append(self.timestep*1000)
        self.ilimits.append(self.params["ILimit"])
        # make sure that the program waits until the current measurement is taken
        self.data_lineR.setData(self.pulsecount, self.readResistances)
        self.data_lineV.setData(self.pulsecount, self.volts)
        self.i = self.i + 1
        if self.i >= len(self.points) or self.stopCall:
            self.stop_program()
            return
        self.timer.singleShot(0, self.pulseMeasure_SMU)  # Measure next pulse
    
    def pulseMeasure_AFG(self):
        """
        Apply and measure one pulse.

        Returns
        -------
        None.

        """
        if self.points[self.i] == self.params["Vset"]:
            self.timestep = self.setTimestep
        elif self.points[self.i] == self.params["Vreset"]:
            self.timestep = self.resetTimestep
        elif self.points[self.i] == 0:
            self.timestep = 0
        if self.timestep > 0 and self.points[self.i] != 0:
            self.k2700.open_Channels(SMU) # Disconnect SMU
            self.k2700.close_Channels(AFG) # connect AFG
            waitFor(20) # wait for 20msec to ensure switching is complete
            self.afg1022.setSinglePulse(self.points[self.i],self.timestep)
            self.afg1022.trgNwait()
            self.k2700.open_Channels(AFG) # disconnect function generator
            self.k2700.close_Channels(SMU) # connect SMU
            waitFor(20) # wait for 20msec to ensure switching is complete
        # Measure Read resistance using K2450
        self.k2450.start_buffer()
        self.k2450.wait_till_done()
        c2 = float(self.k2450.ask("TRAC:stat:average?")[:-1])
        self.volts.append(self.points[self.i]) 
        self.currents.append(-1)    # Junk, just so that saving does not cause error
        self.resistances.append(-1) # Junk, just so that saving does not cause error
        if self.pulsecount == []:
            self.pulsecount = [1]
        else:
            self.pulsecount.append(self.pulsecount[-1]+1)
        self.readVolts.append(self.params["Rvoltage"])
        self.readCurrents.append(c2)
        self.readResistances.append(self.params["Rvoltage"]/c2)
        self.pulseWidths.append(self.timestep*1000)
        self.ilimits.append(self.params["ILimit"])
        # make sure that the program waits until the current measurement is taken
        self.data_lineR.setData(self.pulsecount, self.readResistances)
        self.data_lineV.setData(self.pulsecount, self.volts)
        self.i = self.i + 1
        if self.i >= len(self.points) or self.stopCall:
            self.stop_program()
            return
        self.timer.singleShot(0, self.pulseMeasure_AFG)  # Measure next pulse    

    def applyPulse(self):
        """
        Begins the switching experiment.

        Note: set not to measure the actual applied voltage, as it saves time
        Returns
        -------
        None.

        """
        self.configurePulse()
        if self.params['Vsource'] == 1:
            limiting_current = self.Ilimit.value()
            max_applied_voltage = max(abs(self.minV.value()),abs(self.maxV.value()))
            resistance = round(max_applied_voltage/limiting_current,2)    
            title = "Confirm resistance."
            text = "Is resistor of {} kΩ connected?".format(resistance)
            reply = QMessageBox.question(self, title,text,QMessageBox.Yes,QMessageBox.No)
            if reply == QMessageBox.No:
                return
        self.statusbar.setText("Measurement Running..")
        self.measurement_status = "Running"
        self.i = 0
        if self.initial_source != self.source.currentIndex():
            if not self.savedFlag:
                self.clearGraph()
            self.initial_source = self.source.currentIndex()
        if self.new_flag:
            self.pulsecount = [0]
            self.volts = [0]
            self.currents = []
            self.resistances = []
            self.readVolts = []
            self.readCurrents = []
            self.readResistances = [0]
            self.pulseWidths = []
            self.ilimits = []
            self.new_flag = False
            self.fullfilename = unique_filename(directory='.', prefix=self.filename, datetimeformat="", ext='dat')
            self.initialize_SMU()
            pen1 = mkPen(color=(0, 0, 255), width=2)
            pen2 = mkPen(color=(255, 0, 0), width=2)
            self.data_lineR = self.Rplot.plot(
                self.pulsecount, self.readResistances, pen=pen1, symbol='o')
            self.data_lineV = self.Vplot.plot(
                self.pulsecount, self.volts, pen=pen2, symbol='x', symbolPen='r')
            del self.pulsecount[0]
            del self.readResistances[0]
            del self.volts[0]
            self.timer = QtCore.QTimer()
        self.applyPulse_Button.setEnabled(False)
        self.clearGraph_Button.setEnabled(False)
        self.save_Button.setEnabled(True)
        self.stop_Button.setEnabled(True)
        self.k2450.enable_source()
        self.savedFlag = False
        self.stopCall = False
        if self.params["Vsource"] == 0:
            connect_sample_with_SMU(self.k2700)
            self.timer.singleShot(0, self.pulseMeasure_SMU)
        elif self.params["Vsource"] == 1:
            connect_sample_with_AFG(self.k2700)
            self.k2450.write("SENSe:CURRent:NPLCycles {0}".format(self.k2450.nplc))
            self.k2450.write("TRIG:LOAD 'SimpleLoop', {0}, 0".format(
                                                     self.params["Average"]))
            self.k2450.source_voltage = self.params["Rvoltage"]
            self.timer.singleShot(0, self.pulseMeasure_AFG)

    def stopSwitch(self):
        self.stopCall = True
    
    def clearGraph(self):
        """
        Save the current plot, and clears the graph.

        Returns
        -------
        None.

        """
        self.new_flag = True
        self.Rplot.clear()
        self.Vplot.clear()
        self.saveData()
        self.clearGraph_Button.setEnabled(False)

    def stop_program(self):
        if self.stopCall:
            self.statusbar.setText("Measurement Aborted.")    
            self.measurement_status = "Aborted"
        else:
            self.statusbar.setText("Measurement Finished.")
            self.measurement_status = "Idle"
        self.applyPulse_Button.setEnabled(True)
        self.clearGraph_Button.setEnabled(True)
        self.k2450.source_voltage = 0
        self.k2450.disable_source()
        MessageBeep()

    def saveData(self):
        """
        Save the data to file.

        Returns
        -------
        None.

        """
        if self.savedFlag is True:
            return
        filePresent = bool(fileExists(self.fullfilename))
        with open(self.fullfilename, "a", newline='') as f:
            if self.params["Vsource"] == 0:
                if not filePresent:
                    f.write("#Pulse voltage source: Keithley 2450 source-measure unit.\n")
                    f.write("#Resistance read using Keithley 2450 source-measure unit.\n")
                    f.write("#Read voltage averaged over {0} readings\n".format(self.params["Average"]))
                    f.write("Pulse Voltage (V), Pulse Current (A), Pulse Resistance (ohms), Read Voltage (V), Read Current (A), Read Resistance (ohm), Pulse Width (ms), Compliance current (A)\n")
                data = zip(self.volts, self.currents, self.resistances, self.readVolts, self.readCurrents, self.readResistances, self.pulseWidths, self.ilimits)
            else:
                if not filePresent:
                    f.write("#Pulse voltage source: Tektronix AFG1022 MultiFunction Generator.\n")
                    f.write("#Resistance read using Keithley 2450 source-measure unit.\n")
                    f.write("#Read voltage averaged over {0} readings\n".format(self.params["Average"]))
                    f.write("Pulse Voltage (V), Read Voltage (V), Read Current (A), Read Resistance (ohm), Pulse Width (ms), Compliance current (A)\n")
                data = zip(self.volts, self.readVolts, self.readCurrents, self.readResistances, self.pulseWidths, self.ilimits)
            write_data = writer(f)
            write_data.writerows(data)
        if self.i >= len(self.points):
            self.save_Button.setEnabled(False)
        self.savedFlag = True

    def initialize_plot(self):
        """
        Initialize the plot before starting the measurement.

        Returns
        -------
        None.

        """
        styles = {'color': 'r', 'font-size': '20px'}
        self.Rplot.setXLink(self.Vplot)
        Rx = self.Rplot.getAxis('bottom')
        Rx.setStyle(showValues=False)
        self.Rplot.showGrid(x=True, y=True, alpha=1.0)
        self.Vplot.showGrid(x=True, y=True, alpha=1.0)
        self.Rplot.setLabel('left', 'Read Resistance (Ohms)', **styles)
        self.Vplot.setLabel('left', 'Pulse Voltage (V)', **styles)
        self.Vplot.setLabel('bottom', 'Pulse count', **styles)
    
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
            reply = QMessageBox.question(self, 'Message', quit_msg, QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.stopCall = True
        if reply == QMessageBox.Yes:
            if __name__ != "__main__":
                self.parent.show()
            self.clearGraph()
            self.new_flag = True
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Switch = QtWidgets.QWidget()
    k2450, k2700, afg1022 = checkInstrument(test = True)
    ui = app_Switch(Switch, k2450, k2700, afg1022)
    ui.show()
    app.exec_()
    app.quit()
