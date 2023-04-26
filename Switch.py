# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'switching_test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
#TODO: Preserve graph even after switch is closed. Only if filename is changed, clear the switch graph.
#TODO: also calculate standard deviation for the average read resistance calculated
from utilities import *

class Ui_Switch(QtWidgets.QWidget):
    """The pyqt5 gui class for switching experiment."""

    def __init__(self, parent=None):
        super(Ui_Switch, self).__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)

    def setupUi(self, Switch):
        Switch.setObjectName("Switch")
        Switch.resize(1050, 768)
        Switch.setMinimumSize(QtCore.QSize(1050, 550))
        self.gridLayout_2 = QtWidgets.QGridLayout(Switch)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(Switch)
        self.widget.setMinimumSize(QtCore.QSize(350, 370))
        self.widget.setMaximumSize(QtCore.QSize(350, 430))
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
        self.set_pulseWidth_label = QtWidgets.QLabel(self.frame)
        self.set_pulseWidth_label.setObjectName("set_pulseWidth_label")
        self.gridLayout.addWidget(self.set_pulseWidth_label, 4, 1, 1, 1)
        self.Ilimit = QtWidgets.QDoubleSpinBox(self.frame)
        self.Ilimit.setDecimals(3)
        self.Ilimit.setMaximum(500.0)
        self.Ilimit.setSingleStep(0.001)
        self.Ilimit.setProperty("value", 1.0)
        self.Ilimit.setObjectName("Ilimit")
        self.gridLayout.addWidget(self.Ilimit, 10, 2, 1, 1)
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
        self.maxV_label = QtWidgets.QLabel(self.frame)
        self.maxV_label.setObjectName("maxV_label")
        self.gridLayout.addWidget(self.maxV_label, 5, 1, 1, 1)
        self.fname_label = QtWidgets.QLabel(self.frame)
        self.fname_label.setObjectName("fname_label")
        self.gridLayout.addWidget(self.fname_label, 1, 1, 1, 1)
        self.ncycles_label = QtWidgets.QLabel(self.frame)
        self.ncycles_label.setObjectName("ncycles_label")
        self.gridLayout.addWidget(self.ncycles_label, 7, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.resetV = QtWidgets.QDoubleSpinBox(self.frame)
        self.resetV.setDecimals(3)
        self.resetV.setMinimum(-199.0)
        self.resetV.setMaximum(199.0)
        self.resetV.setSingleStep(0.1)
        self.resetV.setProperty("value", 1.0)
        self.resetV.setObjectName("resetV")
        self.horizontalLayout_3.addWidget(self.resetV)
        self.resetV_check = QtWidgets.QCheckBox(self.frame)
        self.resetV_check.setMaximumSize(QtCore.QSize(20, 16777215))
        self.resetV_check.setText("")
        self.resetV_check.setChecked(True)
        self.resetV_check.setObjectName("resetV_check")
        self.horizontalLayout_3.addWidget(self.resetV_check)
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
        self.minV_label = QtWidgets.QLabel(self.frame)
        self.minV_label.setObjectName("minV_label")
        self.gridLayout.addWidget(self.minV_label, 3, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.avg = QtWidgets.QSpinBox(self.frame)
        self.avg.setMaximumSize(QtCore.QSize(50, 20))
        self.avg.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
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
        self.file_name = QtWidgets.QLineEdit(self.frame)
        self.file_name.setObjectName("file_name")
        self.gridLayout.addWidget(self.file_name, 1, 2, 1, 1)
        self.source = QtWidgets.QComboBox(self.frame)
        self.source.setObjectName("source")
        self.source.addItem("")
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
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.reset_pulseWidth_label = QtWidgets.QLabel(self.frame)
        self.reset_pulseWidth_label.setObjectName("reset_pulseWidth_label")
        self.gridLayout.addWidget(self.reset_pulseWidth_label, 6, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.setV = QtWidgets.QDoubleSpinBox(self.frame)
        self.setV.setDecimals(3)
        self.setV.setMinimum(-50.0)
        self.setV.setMaximum(49.0)
        self.setV.setSingleStep(0.1)
        self.setV.setProperty("value", -3.0)
        self.setV.setObjectName("setV")
        self.horizontalLayout_2.addWidget(self.setV)
        self.setV_check = QtWidgets.QCheckBox(self.frame)
        self.setV_check.setMaximumSize(QtCore.QSize(20, 16777215))
        self.setV_check.setText("")
        self.setV_check.setChecked(True)
        self.setV_check.setObjectName("setV_check")
        self.horizontalLayout_2.addWidget(self.setV_check)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 2, 1, 1)
        self.nPulses = QtWidgets.QSpinBox(self.frame)
        self.nPulses.setMinimum(1)
        self.nPulses.setMaximum(1000)
        self.nPulses.setProperty("value", 1)
        self.nPulses.setObjectName("nPulses")
        self.gridLayout.addWidget(self.nPulses, 9, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        ### Modified code
        self.graphWidget = GraphicsLayoutWidget(Switch)
        self.graphWidget.setBackground((255, 182, 193, 25))
        self.Rplot = self.graphWidget.addPlot(
            row=0, col=0, viewBox=ViewBox(border=mkPen(color='k', width=2)))
        self.Vplot = self.graphWidget.addPlot(
            row=1, col=0, viewBox=ViewBox(border=mkPen(color='k', width=2)))
        self.graphWidget.setMinimumSize(QtCore.QSize(411, 379))
        self.graphWidget.setObjectName("graphWidget")
        self.gridLayout_2.addWidget(self.graphWidget, 0, 1, 2, 1)
        ###
        self.widget1 = QtWidgets.QWidget(Switch)
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
        self.set_timeUnit.setCurrentIndex(1)
        self.reset_timeUnit.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Switch)
        Switch.setTabOrder(self.file_name, self.source)
        Switch.setTabOrder(self.source, self.setV)
        Switch.setTabOrder(self.setV, self.setV_check)
        Switch.setTabOrder(self.setV_check, self.set_pulseWidth)
        Switch.setTabOrder(self.set_pulseWidth, self.set_timeUnit)
        Switch.setTabOrder(self.set_timeUnit, self.resetV)
        Switch.setTabOrder(self.resetV, self.resetV_check)
        Switch.setTabOrder(self.resetV_check, self.reset_pulseWidth)
        Switch.setTabOrder(self.reset_pulseWidth, self.reset_timeUnit)
        Switch.setTabOrder(self.reset_timeUnit, self.read_voltage)
        Switch.setTabOrder(self.read_voltage, self.avg)
        Switch.setTabOrder(self.avg, self.nPulses)
        Switch.setTabOrder(self.nPulses, self.Ilimit)
        Switch.setTabOrder(self.Ilimit, self.temp_check)
        Switch.setTabOrder(self.temp_check, self.temperature)
        Switch.setTabOrder(self.temperature, self.comment_checkBox)
        Switch.setTabOrder(self.comment_checkBox, self.commentBox)
        Switch.setTabOrder(self.commentBox, self.applyPulse_Button)
        Switch.setTabOrder(self.applyPulse_Button, self.clearGraph_Button)
        Switch.setTabOrder(self.clearGraph_Button, self.save_Button)
        Switch.setTabOrder(self.save_Button, self.stop_Button)
        Switch.setTabOrder(self.stop_Button, self.statusbar)

    def retranslateUi(self, Switch):
        _translate = QtCore.QCoreApplication.translate
        Switch.setWindowTitle(_translate("Switch", "Switch Test"))
        self.title_label.setText(_translate("Switch",
                                            "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#0000ff;\">Switching Test</span></p></body></html>"))
        self.setting_label.setText(_translate("Switch",
                                              "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#aa0000;\">Settings</span></p></body></html>"))
        self.set_timeUnit.setToolTip(_translate("Switch",
                                                "<html><head/><body><p>Select time unit. Time below 50 ms may not be reliable for Keithley 2450</p></body></html>"))
        self.set_timeUnit.setItemText(0, _translate("Switch", "us"))
        self.set_timeUnit.setItemText(1, _translate("Switch", "ms"))
        self.set_timeUnit.setItemText(2, _translate("Switch", "s"))
        self.label_2.setText(_translate("Switch",
                                        "<html><head/><body><p><span style=\" font-size:10pt;\">Number of pulse sets</span></p></body></html>"))
        self.set_pulseWidth_label.setText(_translate("Switch",
                                                     "<html><head/><body><p><span style=\" font-size:10pt;\">Set Pulse Width</span></p></body></html>"))
        self.Ilimit.setToolTip(_translate("Switch",
                                          "<html><head/><body><p>The compliance current, which protects the sample from full breakdown</p></body></html>"))
        self.temperature.setToolTip(_translate("Switch",
                                               "<html><head/><body><p>Temperature range will depend on the type of heater</p></body></html>"))
        self.maxV_label.setText(_translate("Switch",
                                           "<html><head/><body><p><span style=\" font-size:10pt;\">Reset Voltage (V)</span></p></body></html>"))
        self.fname_label.setText(_translate("Switch",
                                            "<html><head/><body><p><span style=\" font-size:10pt;\">File Name</span></p></body></html>"))
        self.ncycles_label.setText(_translate("Switch",
                                              "<html><head/><body><p><span style=\" font-size:10pt;\">Read Voltage (V)</span></p></body></html>"))
        self.resetV.setToolTip(_translate("Switch", "<html><head/><body><p>Max 10 V</p></body></html>"))
        self.reset_timeUnit.setToolTip(_translate("Switch",
                                                  "<html><head/><body><p>Select time unit. Time below 50 ms may not be reliable for Keithley 2450</p></body></html>"))
        self.reset_timeUnit.setItemText(0, _translate("Switch", "us"))
        self.reset_timeUnit.setItemText(1, _translate("Switch", "ms"))
        self.reset_timeUnit.setItemText(2, _translate("Switch", "s"))
        self.minV_label.setText(_translate("Switch",
                                           "<html><head/><body><p><span style=\" font-size:10pt;\">Set Voltage (V)</span></p></body></html>"))
        self.avgread_label.setText(_translate("Switch",
                                              "<html><head/><body><p><span style=\" font-size:10pt;\">Readings</span></p></body></html>"))
        self.file_name.setText(_translate("Switch", "Sample_Switch"))
        self.source.setItemText(0, _translate("Switch", "Keysight B2902B"))
        self.source.setItemText(1, _translate("Switch", "Keithley 2450"))
        self.source.setItemText(2, _translate("Switch", "Tektronix AFG1022"))
        self.Ilimit_label.setText(_translate("Switch",
                                             "<html><head/><body><p><span style=\" font-size:10pt;\">Current Limit (mA)</span></p></body></html>"))
        self.temp_check.setToolTip(_translate("Switch",
                                              "<html><head/><body><p>Use temperature only if temperature controller is attached</p></body></html>"))
        self.temp_check.setText(_translate("Switch", "Temperature (K)"))
        self.avg_label.setText(_translate("Switch",
                                          "<html><head/><body><p><span style=\" font-size:10pt;\">Average over</span></p></body></html>"))
        self.label.setText(_translate("Switch",
                                      "<html><head/><body><p><span style=\" font-size:10pt;\">Voltage Source</span></p></body></html>"))
        self.reset_pulseWidth_label.setText(_translate("Switch",
                                                       "<html><head/><body><p><span style=\" font-size:10pt;\">Reset Pulse width</span></p></body></html>"))
        self.setV.setToolTip(_translate("Switch", "<html><head/><body><p>Max -10 V</p></body></html>"))
        self.comment_checkBox.setText(_translate("Switch", "Add Comments"))
        self.applyPulse_Button.setToolTip(
            _translate("Switch", "<html><head/><body><p>Click to start the experiment</p></body></html>"))
        self.applyPulse_Button.setText(_translate("Switch", "Apply Pulse"))
        self.clearGraph_Button.setToolTip(
            _translate("Switch", "<html><head/><body><p>Click to abort the experiment</p></body></html>"))
        self.clearGraph_Button.setText(_translate("Switch", "Clear graph and start new measurement"))
        self.save_Button.setText(_translate("Switch", "Save Data"))
        self.stop_Button.setText(_translate("Switch", "Stop"))


class app_Switch(Ui_Switch):
    """The Switch app module."""

    def __init__(self, parent=None, smu=None, k2700=None, afg1022=None, sName="Sample_Switch.dat", connection=1):
        super(app_Switch, self).__init__(parent)
        self.parent = parent
        self.new_flag = True
        self.savedFlag = True
        self.stop_flag = False
        self.initial_source = -1  # 0 = SMU, 1 = AFG
        self.smu = smu
        self.k2700 = k2700
        self.afg1022 = afg1022
        self.connection = connection
        self.Ilimit.setMaximum(500)
        self.Ilimit.setMinimum(0.001)
        self.Ilimit.setSingleStep(0.1)
        self.read_voltage.setMinimum(-10)
        self.read_voltage.setMaximum(10)
        self.save_Button.hide()
        if self.afg1022:
            if self.afg1022.ID == 'Fake':
                self.source.removeItem(2)  # Remove AFG source option
        else:
            self.source.removeItem(2)  # Remove AFG source option
        if self.smu:
            if self.smu.ID == 'Fake':
                self.widget.setEnabled(False)
                self.statusbar.setText("Sourcemeter not connected. Reconnect and try again.")
                self.widget1.setEnabled(False)
                self.Rplot.setEnabled(False)
                self.Vplot.setEnabled(False)
            elif self.smu.ID == 'B2902B':
                self.source.removeItem(1)  # Remove Keithley SMU source option
            elif self.smu.ID == 'K2450':
                self.source.removeItem(0)  # Remove Keysight SMU source option
            self.smu.avg = 5
        else:
            self.widget.setEnabled(False)
            self.statusbar.setText("Sourcemeter not connected. Reconnect and try again.")
            self.widget1.setEnabled(False)
            self.Rplot.setEnabled(False)
            self.Vplot.setEnabled(False)
        self.stop_Button.setEnabled(False)
        self.clearGraph_Button.setEnabled(False)
        self.applyPulse_Button.clicked.connect(self.applyPulse)
        self.clearGraph_Button.clicked.connect(self.clearGraph)
        self.stop_Button.clicked.connect(self.stopSwitch)
        self.applyPulse_Button.setShortcut('ctrl+Return')
        self.clearGraph_Button.setShortcut('ctrl+g')
        self.stop_Button.setShortcut('ctrl+q')
        self.setV_check.stateChanged.connect(self.change_setV)
        self.resetV_check.stateChanged.connect(self.change_resetV)
        self.source.currentIndexChanged.connect(self.update_limits)
        self.set_timeUnit.currentIndexChanged.connect(self.update_limits)
        self.reset_timeUnit.currentIndexChanged.connect(self.update_limits)
        self.set_timeUnit.currentIndexChanged.connect(self.update_setTimeunit)
        self.reset_timeUnit.currentIndexChanged.connect(self.update_resetTimeunit)
        self.initialize_plot()
        self.update_limits()
        self.stopCall = False
        self.measurement_status = "Idle"
        self.smu.nplc = 1
        self.smu.readV = 0.1
        self.filename = self.fullfilename = sName
        self.file_name.setText(self.filename)
        self.file_name.setReadOnly(True)
        self.params = {
            "Vsource": 0,  # 0 = SMU, 1 = AFG
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
            "ILimit": 1 / 1000,
            "temperature": 300,
            "temp_check": 0,
            "comments": ""}
        self.parameters = list(self.params.values())[:-1]
        self.comment_checkBox.stateChanged.connect(self.updateCommentBox)
        self.comment_checkBox.setChecked(True)
        self.pulsecount = [1]

    def updateCommentBox(self):
        if self.comment_checkBox.isChecked():
            self.commentBox.setEnabled(True)
        else:
            self.commentBox.setEnabled(False)

    def update_setTimeunit(self):
        self.set_pulseWidth.setValue(self.set_pulseWidth.minimum())

    def update_resetTimeunit(self):
        self.reset_pulseWidth.setValue(self.reset_pulseWidth.minimum())

    def update_limits(self):
        print(1)
        self.set_pulseWidth.setMaximum(999)
        self.reset_pulseWidth.setMaximum(999)
        self.set_pulseWidth.setMinimum(1)
        self.reset_pulseWidth.setMinimum(1)
        if self.source.currentIndex() == 0:
            self.setV.setMaximum(199)
            self.setV.setMinimum(-199)
            self.resetV.setMaximum(199)
            self.resetV.setMinimum(-199)
            if self.smu.ID == "K2450":
                if self.set_timeUnit.currentIndex() == 0:
                    self.set_timeUnit.setCurrentIndex(1)
                self.set_timeUnit.model().item(0).setEnabled(False)
                if self.reset_timeUnit.currentIndex() == 0:
                    self.reset_timeUnit.setCurrentIndex(1)
                self.reset_timeUnit.model().item(0).setEnabled(False)
                self.nPulses.setMaximum(1000)
            elif self.smu.ID == "B2902B":
                self.set_timeUnit.model().item(0).setEnabled(True)
                self.reset_timeUnit.model().item(0).setEnabled(True)
                if self.set_timeUnit.currentIndex() == 0: #μs
                    self.set_pulseWidth.setMinimum(50)
                if self.reset_timeUnit.currentIndex() == 0: #μs
                    self.reset_pulseWidth.setMinimum(50)
                if self.set_timeUnit.currentIndex() == 2: #s
                    self.set_pulseWidth.setMaximum(2)
                if self.reset_timeUnit.currentIndex() == 2: #s
                    self.reset_pulseWidth.setMaximum(2)
        else:
            self.setV.setMaximum(5)
            self.setV.setMinimum(-5)
            self.resetV.setMaximum(5)
            self.resetV.setMinimum(-5)
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
        if self.setV_check.isChecked():
            self.setV.setEnabled(True)
        else:
            self.setV.setEnabled(False)

    def change_resetV(self):
        """
        Enable or disable 'reset' pulse based on user preference.

        Returns
        -------
        None.

        """
        if self.resetV_check.isChecked():
            self.resetV.setEnabled(True)
        else:
            self.resetV.setEnabled(False)

    def load_parameters(self):
        try:
            self.source.setCurrentIndex(self.parameters[0])
        except Exception as e:
            print(e)
            pass
        try:
            self.setV.setValue(self.parameters[1]),
            self.setV_check.setChecked(self.parameters[2]),
            self.set_pulseWidth.setValue(self.parameters[3]),
            self.set_timeUnit.setCurrentIndex(self.parameters[4]),
            self.resetV.setValue(self.parameters[5]),
            self.resetV_check.setChecked(self.parameters[6]),
            self.reset_pulseWidth.setValue(self.parameters[7]),
            self.reset_timeUnit.setCurrentIndex(self.parameters[8]),
            self.read_voltage.setValue(self.parameters[9]),
            self.avg.setValue(self.parameters[10]),
            self.nPulses.setValue(self.parameters[11]),
            self.Ilimit.setValue(self.parameters[12] * 1000),
            self.temperature.setValue(self.parameters[13]),
            self.temp_check.setChecked(self.parameters[14])
        except Exception as e:
            print(f"Problem with loading switch parameters. {e}")
            print("Deleting parameter file from the folder may resolve the issue.")

    def update_params(self):
        """
        Update the measurement parameters.

        Note: Function gen: Vlimit: +-5V, npoints < 50
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
            "Vsource": self.source.currentIndex(),
            "Vset": self.setV.value(),
            "VsetCheck": self.setV_check.checkState(),
            "setPwidth": self.set_pulseWidth.value(),
            "set_timeUnit": self.set_timeUnit.currentIndex(),
            "Vreset": self.resetV.value(),
            "VresetCheck": self.resetV_check.checkState(),
            "resetPwidth": self.reset_pulseWidth.value(),
            "reset_timeUnit": self.reset_timeUnit.currentIndex(),
            "Rvoltage": self.read_voltage.value(),
            "Average": self.avg.value(),
            "nPulses": self.nPulses.value(),
            "ILimit": self.Ilimit.value() / 1000,
            "temperature": self.temperature.value(),
            "temp_check": int(self.temp_check.isChecked()),
            "comments": formattedComment}
        self.parameters = list(self.params.values())[:-1]

    def plot_realtime_data(self, data):
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
        self.volts.extend(data[0])
        self.readResistances.extend(data[1])
        nPulses = len(data[0])
        if self.pulsecount:
            startPulse = self.pulsecount[-1] + 1
        else:
            startPulse = 1
        endPulse = startPulse+nPulses-1
        self.pulsecount.extend(np.linspace(startPulse,endPulse,nPulses,dtype=int))
        self.readResistances = [abs(x) for x in self.readResistances]
        try:
            self.data_lineR.setData(self.pulsecount, self.readResistances)
            self.data_lineV.setData(self.pulsecount, self.volts)
        except Exception as e:
            print("Some error in plotting")
            print(e)

    def applyPulse(self):
        """
        Begins the switching experiment.

        Note: set not to measure the actual applied voltage, as it saves time
        Returns
        -------
        None.

        """
        self.stop_flag = False
        self.update_params()
        if self.initial_source != self.source.currentIndex():
            self.clearGraph()
            self.initial_source = self.source.currentIndex()
            if self.params['Vsource'] == 1:
                limiting_current = self.Ilimit.value()
                max_applied_voltage = max(abs(self.setV.value()), abs(self.resetV.value()))
                resistance = round(max_applied_voltage / limiting_current, 2)
                title = "Confirm resistance."
                text = "Is resistor of {} kΩ connected?".format(resistance)
                reply = QMessageBox.question(self, title, text, QMessageBox.Yes, QMessageBox.No)
                if reply == QMessageBox.No:
                    return
                # if nPulses is > 10 when using AFG, limit nPulses to 10, to avoid too much multiplex usage.
                if self.nPulses.value() > 10:
                    self.nPulses.setValue(10)
        self.statusbar.setText("Measurement Running..")
        self.measurement_status = "Running"
        if self.new_flag:
            self.pulsecount = [0]
            self.readResistances = [0]
            self.volts = [0]
            self.fullfilename = unique_filename(directory='.', prefix=self.filename, datetimeformat="", ext='dat')
            pen1 = mkPen(color=(0, 0, 255), width=2)
            pen2 = mkPen(color=(255, 0, 0), width=2)
            self.data_lineR = self.Rplot.plot(
                self.pulsecount, self.readResistances, pen=pen1, symbol='o')
            self.data_lineV = self.Vplot.plot(
                self.pulsecount, self.volts, pen=pen2, symbol='x', symbolPen='r')
            del self.pulsecount[0]
            del self.readResistances[0]
            del self.volts[0]
        self.widget.setEnabled(False)
        #self.comment_checkBox.setEnabled(False)
        #self.commentBox.setEnabled(False)
        self.applyPulse_Button.setEnabled(False)
        self.clearGraph_Button.setEnabled(False)
        self.stop_Button.setEnabled(True)
        self.smu.enable_source()
        self.stopCall = False
        self.initialize_thread()
        self.new_flag = False

    def initialize_thread(self):
        self.thread = QThread()
        self.worker = Worker(self.smu, self.k2700, self.connection, self.params,
                             self.new_flag, self.fullfilename)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.start_switch)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.data.connect(self.plot_realtime_data)
        self.thread.finished.connect(self.finishAction)
        self.thread.start()

    def stopSwitch(self):
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
        self.clearGraph_Button.setEnabled(False)

    def finishAction(self):
        """
        Trigger to stop the Switch measurement.
        Returns
        -------
        None.

        """
        if not self.stop_flag:
            self.measurement_status = "Idle"
            self.statusbar.setText("Measurement Finished.")
            self.stop_flag = True
        self.widget.setEnabled(True)
        self.applyPulse_Button.setEnabled(True)
        self.clearGraph_Button.setEnabled(True)
        # self.comment_checkBox.setEnabled(True)
        # self.commentBox.setEnabled(True)
        self.stop_Button.setEnabled(False)
        MessageBeep()

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

class Worker(QObject):
    finished = pyqtSignal()
    data = pyqtSignal(list)
    stopcall = pyqtSignal()
    def __init__(self, smu = None, k2700 = None, connection = 1, params = [],
                 new_flag = True, fullfilename = "sample.dat"):
        super(Worker, self).__init__()
        self.stopCall = False
        self.smu = smu
        self.savedFlag = False
        self.k2700 = k2700
        self.connection = connection
        self.params = params
        self.new_flag = new_flag
        self.fullfilename = fullfilename
        self.tempfileName = self.fullfilename[:-4] + "_tmp.dat"
        self.npoints = self.params["nPulses"]
        self.stopcall.connect(self.stopcalled)
        self.smu.nplc = 1
        self.status = 1

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
        self.smu.apply_voltage(compliance_current=self.params["ILimit"])
        self.smu.measure_current()
        self.smu.set_wire_configuration(self.smu.wire_config)

    def configure_pulse(self):
        """
            Configure the pulse parameters.

            Returns
            -------
            None.

        """
        self.smu.set_compliance(self.params["ILimit"])
        self.smu.readV = self.params["Rvoltage"]
        if self.params["set_timeUnit"] == 0:
            self.set_pulse_width = self.params["setPwidth"] * 1e-6
        elif self.params["set_timeUnit"] == 1:
            self.set_pulse_width = self.params["setPwidth"] * 1e-3
        elif self.params["set_timeUnit"] == 2:
            self.set_pulse_width = self.params["setPwidth"]
        if self.params["reset_timeUnit"] == 0:
            self.reset_pulse_width = self.params["resetPwidth"] * 1e-6
        elif self.params["reset_timeUnit"] == 1:
            self.reset_pulse_width = self.params["resetPwidth"] * 1e-3
        elif self.params["reset_timeUnit"] == 2:
            self.reset_pulse_width = self.params["resetPwidth"]

        self.points = []
        self.pulsewidths = []
        pulsewidth = 1e-3
        if self.params["VsetCheck"]:
            self.points.append(self.params["Vset"])
            pulsewidth = self.set_pulse_width
            self.pulsewidths.append(self.set_pulse_width)
        if self.params["VresetCheck"]:
            self.points.append(self.params["Vreset"])
            pulsewidth = self.reset_pulse_width
            self.pulsewidths.append(self.reset_pulse_width)
        if not self.params["VsetCheck"] and not self.params["VresetCheck"]:
            self.points.append(0)
            self.pulsewidths.append(pulsewidth)
        self.points = np.tile(self.points, self.npoints)
        self.pulsewidths = np.tile(self.pulsewidths, self.npoints)
        self.smu.avg = self.params["Average"]
        if self.smu.ID == 'B2902B' and self.params["Vsource"] == 0:
            voltages = ",".join(self.points.astype('str'))
            if self.set_pulse_width == self.reset_pulse_width or \
                    not self.params["VsetCheck"] or not self.params["VresetCheck"]:
                self.smu.configure_pulse_sweep(voltages,
                                               baseV=self.params["Rvoltage"],
                                               pulse_width=pulsewidth)
            else:
                self.smu.configure_pulse(baseV = self.params["Rvoltage"],
                                         pw1 = self.set_pulse_width,
                                         pw2 = self.reset_pulse_width)

    def pulseMeasure_B2902B(self):
        whole_writeData = []
        whole_readData = []
        if self.set_pulse_width == self.reset_pulse_width or \
                not self.params["VsetCheck"] or not self.params["VresetCheck"]:
            self.npoints = len(self.points)
            self.smu.clear_buffer((self.smu.avg + 1) * self.npoints)
            self.smu.start_buffer()
            buffer = []
            number_of_data_per_point = 4
            finished = False
            while True:
                if len(whole_writeData) == self.npoints:  # break if required number of data is already obtained
                    finished = True
                    break
                if self.smu.get_trigger_state() == 'IDLE' or self.stopCall: # This line ensures last set of data is collected
                    finished = True
                data2 = buffer
                buffer = []
                while True:
                    sleep(0.2)
                    data = self.smu.get_trace_data_recent()
                    data2.extend(np.reshape(np.array(data.split(','), dtype=float), (-1, number_of_data_per_point)))
                    data_length = len(data2)
                    if data_length >= self.smu.avg + 1:
                        trimmed_length = int(data_length / (self.smu.avg + 1)) * (self.smu.avg + 1)
                        buffer = data2[trimmed_length:]
                        data2 = np.array(data2[:trimmed_length])
                        break
                writeData = data2[::self.smu.avg + 1]
                if self.smu.avg == 1:
                    readData = data2[1::self.smu.avg + 1]
                else:
                    readData = data2[np.mod(np.arange(data2.shape[0]), self.smu.avg + 1) != 0].copy()
                    readData = np.reshape(readData, (-1, self.smu.avg, number_of_data_per_point))
                    readData = np.mean(readData, axis=1)
                whole_writeData.extend(writeData)
                whole_readData.extend(readData)
                requestedVoltage = writeData[:, 3]
                read_currents = readData[:, 1]
                read_currents[read_currents==0] = 1e-20
                resistances = self.params["Rvoltage"] / read_currents
                self.data.emit([requestedVoltage, resistances])
                if finished:
                    break
        else:
            # TODO: check if this algorithm will work
            cycleNum = 0
            while cycleNum < self.npoints and not self.stopCall:
                self.smu.set_pulse1(self.set_pulse_width, self.params["Vset"])
                self.smu.start_buffer()
                self.smu.wait_till_done()
                setData = self.smu.get_trace_data()
                self.smu.set_pulse2(self.reset_pulse_width, self.params["Vreset"])
                self.smu.start_buffer()
                self.smu.wait_till_done()
                resetData = self.smu.get_trace_data()
                setData = np.reshape(np.array(setData.split(','), dtype=float),(-1,4))
                resetData = np.reshape(np.array(resetData.split(','), dtype=float),(-1,4))
                requestedVoltage = [setData[0][3],resetData[0][3]] # actual voltage applied
                avgreadData_set = np.mean(setData[1:], axis=0)
                avgreadData_reset = np.mean(resetData[1:], axis=0)
                rc = np.array([avgreadData_set[1],avgreadData_reset[1]]) # read current
                rc[rc==0] = 1e-20
                resistance = np.divide(self.params["Rvoltage"] , rc)
                whole_writeData.extend([setData[0], resetData[0]])
                whole_readData.extend([avgreadData_set, avgreadData_reset])
                self.data.emit([requestedVoltage, resistance])
                cycleNum += 1
        whole_writeData = np.array(whole_writeData)
        whole_readData = np.array(whole_readData)
        volts = whole_writeData[:, 0]
        read_currents = whole_readData[:, 1]
        requestedVoltage = whole_writeData[:, 3]
        set_currents = whole_writeData[:, 1]
        set_currents[set_currents==0] = 1e-20
        read_currents[read_currents==0] = 1e-20
        time_stamp = whole_writeData[:, 2]
        data = np.array((requestedVoltage, volts, set_currents, read_currents, time_stamp))
        return data

    def pulseMeasure_K2450(self):
        """
        Initiate the measurement of one data point.

        Returns
        -------
        None.

        """
        i = 0
        requestedVoltage = []
        volts = []
        set_currents = []
        read_currents = []
        time_stamp = []
        while i < self.npoints and not self.stopCall:
            self.smu.setNPLC(0.01)
            self.smu.set_simple_loop(delayTime=self.timestep)
            self.smu.source_voltage = self.points[i]
            self.smu.start_buffer()
            self.wait_till_done(1)
            setData = self.smu.get_trace_data(1, 1)
            setData = array(setData.split(','), dtype=float)
            volt, c, t = setData[0], setData[1], setData[2]
            if c == 0:
                c = 1e-20
            self.smu.setNPLC()
            self.smu.set_simple_loop(count=self.smu.avg)
            self.smu.source_voltage = self.params["Rvoltage"]
            self.smu.start_buffer()
            self.wait_till_done()
            rc = self.smu.get_average_trace_data() # read current
            if rc == 0:
                rc = 1e-20
            resistance = self.params["Rvoltage"] / rc
            self.data.emit([[volt], [resistance]])
            requestedVoltage.append(self.points[i])
            volts.append(v)
            set_currents.append(c)
            read_currents.append(rc)
            time_stamp.append(t)
            i = i + 1
        data = np.array((requestedVoltage, volts, set_currents, read_currents, time_stamp))
        return data

    def pulseMeasure_AFG(self):
        """
        Initiate the measurement of one data point.

        Returns
        -------
        None.

        """
        i = 0
        requestedVoltage = []
        read_currents = []
        while i < self.npoints and not self.stopCall:
            self.afg1022.setSinglePulse(self.points[i],self.timestep)
            self.afg1022.trgNwait()
            if self.connection == 1:
                self.k2700.open_Channels(AFG) # disconnect function generator
                self.k2700.close_Channels(SMU) # connect SMU
            elif self.connection == 2:
                self.k2700.open_Channels(AFG+10) # disconnect function generator
                self.k2700.close_Channels(SMU+10) # connect SMU
            sleep(0.2) # wait for 200msec to ensure switching is complete
            self.smu.start_buffer()
            self.wait_till_done()
            rc = self.smu.get_average_trace_data() # mean read current of avg samples
            if rc == 0:
                rc = 1e-20
            resistance = self.params["Rvoltage"]/ rc
            self.data.emit([self.points[i], [resistance]])
            requestedVoltage.append(self.points[i])
            read_currents.append(rc)
            i += 1
        data = np.array((requestedVoltage, read_currents))
        return data

    def start_switch(self):
        """
                Begins the switching experiment.

                Returns
                -------
                None.

                """
        self.i = 0
        if self.new_flag:
            self.initialize_SMU()
        self.configure_pulse()
        self.smu.enable_source()
        if self.params["Vsource"] == 0:
            connect_sample_with_SMU(self.k2700, self.connection)
            if self.smu.ID == 'K2450':
                data =  self.pulseMeasure_K2450()
            elif self.smu.ID == 'B2902B':
                data = self.pulseMeasure_B2902B()
            complianceCurrents = np.ones(data.shape[1]) * self.params["ILimit"]
            readVs = np.ones(data.shape[1]) * self.params["Rvoltage"]
            pulseResistances = data[1] / data[2]
            readResistances = self.params["Rvoltage"] / data[3]
            self.pulsewidths = self.pulsewidths[:data.shape[1]]
            totalData = np.array((data[0], data[1], data[2], pulseResistances,
                                  readVs, data[3], readResistances, self.pulsewidths,
                                  complianceCurrents, data[4]), dtype=float)
        elif self.params["Vsource"] == 1:
            # TODO: check if this will work with Keysight SMU
            connect_sample_with_AFG(self.k2700, self.connection)
            self.smu.setNPLC()
            self.smu.set_simple_loop(count=self.params["Average"])
            self.smu.source_voltage = self.params["Rvoltage"]
            data = self.pulseMeasure_AFG()
            complianceCurrents = np.ones(data.shape[1]) * self.params["ILimit"]
            readVs = np.ones(data.shape[1]) * self.params["Rvoltage"]
            readResistances = self.params["Rvoltage"]/ data[1]
            totalData = np.array((data[0], readVs, data[1],
                                  readResistances, self.pulsewidths,
                                  complianceCurrents))
        with open(self.tempfileName, "w") as f:
            np.savetxt(f, totalData.T, delimiter='\t')
            f.write("\n\n")
        self.saveData()
        self.stop_program()

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

    def saveData(self):
        """
        Save the data to file.

        Returns
        -------
        None.

        """
        filePresent = bool(fileExists(self.fullfilename))
        if not filePresent:
            if not self.savedFlag:
                with open(self.fullfilename, "w", newline='') as f:
                    if self.params["Vsource"] == 0:
                        if self.smu.ID == "K2450":
                            f.write("##Pulse voltage source: Keithley 2450 source-measure unit.\n")
                            f.write("##Resistance read using Keithley 2450 source-measure unit.\n")
                        elif self.smu.ID == 'B2902':
                            f.write("##Pulse voltage source: Keysight B2902 source-measure unit."
                                    f"(channel {self.smu.ch})\n")
                            f.write("##Resistance read using Keysight B2902 source-measure unit."
                                    f"(channel {self.smu.ch})\n")
                        f.write(f"## Date & Time: {datetime.now().strftime('%m/%d/%Y; %H:%M:%S')}\n")
                        f.write(f"##Read voltage averaged over {self.smu.avg} readings\n")
                        f.write(self.params["comments"])
                        f.write("#Pulse Voltage (V)\tActual Pulse Voltage (V)\t"
                                "Pulse Current (A)\tPulse Resistance (ohms)\t"
                                "Read Voltage (V)\tRead Current (A)\tRead Resistance (ohm)\t"
                                "Pulse Width (ms)\tCompliance current (A)\tTime Stamp (s)\n")
                    else:
                        f.write("##Pulse voltage source: Tektronix AFG1022 MultiFunction Generator.\n")
                        if self.smu.ID == 'K2450':
                            f.write("##Resistance read using Keithley 2450 source-measure unit.\n")
                        elif self.smu.ID == 'B2902B':
                            f.write("##Resistance read using Keysight B2902B source-measure unit "
                                    f"channel {self.smu.ch}.\n")
                        f.write(f"## Date & Time: {datetime.now().strftime('%m/%d/%Y; %H:%M:%S')}\n")
                        f.write(f"##Read voltage averaged over {self.params['Average']} readings\n")
                        f.write(self.params["comments"])
                        f.write("#Pulse Voltage (V)\tRead Voltage (V)\tRead Current (A)\tRead Resistance (ohm)\t"
                                "Pulse Width (ms)\tCompliance current (A)\n")
        f = open(self.fullfilename, 'a')
        if fileExists(self.tempfileName):
            with open(self.tempfileName, 'r') as tmp:
                lines = tmp.readlines()
                f.writelines(lines)
            f.close()
            os.remove(self.tempfileName)
        self.savedFlag = True

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
    Switch = QtWidgets.QWidget()
    smu, k2700, afg1022 = checkInstrument(test=True)
    ui = app_Switch(Switch, smu, k2700, afg1022)
    ui.show()
    app.exec_()
    app.quit()