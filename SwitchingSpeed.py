# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'switching_speed.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Switch(object):
    def setupUi(self, Switch):
        Switch.setObjectName("Switch")
        Switch.resize(1050, 600)
        Switch.setMinimumSize(QtCore.QSize(1050, 550))
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
        self.set_pulseWidth_label = QtWidgets.QLabel(self.frame)
        self.set_pulseWidth_label.setObjectName("set_pulseWidth_label")
        self.gridLayout.addWidget(self.set_pulseWidth_label, 4, 1, 1, 1)
        self.maxV_label = QtWidgets.QLabel(self.frame)
        self.maxV_label.setObjectName("maxV_label")
        self.gridLayout.addWidget(self.maxV_label, 6, 1, 1, 1)
        self.read_voltage = QtWidgets.QDoubleSpinBox(self.frame)
        self.read_voltage.setDecimals(3)
        self.read_voltage.setMaximum(10.0)
        self.read_voltage.setSingleStep(0.1)
        self.read_voltage.setProperty("value", 0.1)
        self.read_voltage.setObjectName("read_voltage")
        self.gridLayout.addWidget(self.read_voltage, 11, 2, 1, 1)
        self.temperature = QtWidgets.QDoubleSpinBox(self.frame)
        self.temperature.setEnabled(False)
        self.temperature.setMaximum(600.0)
        self.temperature.setProperty("value", 300.0)
        self.temperature.setObjectName("temperature")
        self.gridLayout.addWidget(self.temperature, 16, 2, 1, 1)
        self.source = QtWidgets.QComboBox(self.frame)
        self.source.setEnabled(False)
        self.source.setObjectName("source")
        self.source.addItem("")
        self.gridLayout.addWidget(self.source, 2, 2, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.avg = QtWidgets.QSpinBox(self.frame)
        self.avg.setMaximumSize(QtCore.QSize(50, 20))
        self.avg.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.avg.setMinimum(1)
        self.avg.setMaximum(1000)
        self.avg.setProperty("value", 5)
        self.avg.setObjectName("avg")
        self.horizontalLayout_4.addWidget(self.avg)
        self.avgread_label = QtWidgets.QLabel(self.frame)
        self.avgread_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.avgread_label.setObjectName("avgread_label")
        self.horizontalLayout_4.addWidget(self.avgread_label)
        self.gridLayout.addLayout(self.horizontalLayout_4, 12, 2, 1, 1)
        self.file_name = QtWidgets.QLineEdit(self.frame)
        self.file_name.setObjectName("file_name")
        self.gridLayout.addWidget(self.file_name, 1, 2, 1, 1)
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.resetV = QtWidgets.QDoubleSpinBox(self.frame)
        self.resetV.setDecimals(3)
        self.resetV.setMinimum(-49.0)
        self.resetV.setMaximum(50.0)
        self.resetV.setSingleStep(0.001)
        self.resetV.setProperty("value", 3.0)
        self.resetV.setObjectName("resetV")
        self.horizontalLayout_3.addWidget(self.resetV)
        self.resetV_check = QtWidgets.QCheckBox(self.frame)
        self.resetV_check.setMaximumSize(QtCore.QSize(20, 16777215))
        self.resetV_check.setText("")
        self.resetV_check.setChecked(True)
        self.resetV_check.setObjectName("resetV_check")
        self.horizontalLayout_3.addWidget(self.resetV_check)
        self.gridLayout.addLayout(self.horizontalLayout_3, 6, 2, 1, 1)
        self.reset_pulseWidth_label = QtWidgets.QLabel(self.frame)
        self.reset_pulseWidth_label.setObjectName("reset_pulseWidth_label")
        self.gridLayout.addWidget(self.reset_pulseWidth_label, 7, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.temp_check = QtWidgets.QCheckBox(self.frame)
        self.temp_check.setObjectName("temp_check")
        self.gridLayout.addWidget(self.temp_check, 16, 1, 1, 1)
        self.avg_label = QtWidgets.QLabel(self.frame)
        self.avg_label.setObjectName("avg_label")
        self.gridLayout.addWidget(self.avg_label, 12, 1, 1, 1)
        self.minV_label = QtWidgets.QLabel(self.frame)
        self.minV_label.setObjectName("minV_label")
        self.gridLayout.addWidget(self.minV_label, 3, 1, 1, 1)
        self.ncycles_label = QtWidgets.QLabel(self.frame)
        self.ncycles_label.setObjectName("ncycles_label")
        self.gridLayout.addWidget(self.ncycles_label, 11, 1, 1, 1)
        self.fname_label = QtWidgets.QLabel(self.frame)
        self.fname_label.setObjectName("fname_label")
        self.gridLayout.addWidget(self.fname_label, 1, 1, 1, 1)
        self.Ilimit_label = QtWidgets.QLabel(self.frame)
        self.Ilimit_label.setObjectName("Ilimit_label")
        self.gridLayout.addWidget(self.Ilimit_label, 9, 1, 1, 1)
        self.Ilimit = QtWidgets.QDoubleSpinBox(self.frame)
        self.Ilimit.setDecimals(3)
        self.Ilimit.setMaximum(500.0)
        self.Ilimit.setSingleStep(0.001)
        self.Ilimit.setProperty("value", 1.0)
        self.Ilimit.setObjectName("Ilimit")
        self.gridLayout.addWidget(self.Ilimit, 9, 2, 1, 1)
        self.set_pulseWidth_label_3 = QtWidgets.QLabel(self.frame)
        self.set_pulseWidth_label_3.setObjectName("set_pulseWidth_label_3")
        self.gridLayout.addWidget(self.set_pulseWidth_label_3, 8, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.set_pulseWidth_6 = QtWidgets.QDoubleSpinBox(self.frame)
        self.set_pulseWidth_6.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.set_pulseWidth_6.setDecimals(2)
        self.set_pulseWidth_6.setMaximum(1000.0)
        self.set_pulseWidth_6.setProperty("value", 1.0)
        self.set_pulseWidth_6.setObjectName("set_pulseWidth_6")
        self.horizontalLayout.addWidget(self.set_pulseWidth_6)
        self.set_timeUnit_6 = QtWidgets.QComboBox(self.frame)
        self.set_timeUnit_6.setMaximumSize(QtCore.QSize(41, 22))
        self.set_timeUnit_6.setObjectName("set_timeUnit_6")
        self.set_timeUnit_6.addItem("")
        self.set_timeUnit_6.addItem("")
        self.set_timeUnit_6.addItem("")
        self.horizontalLayout.addWidget(self.set_timeUnit_6)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 2, 1, 1)
        self.set_pulseWidth_label_2 = QtWidgets.QLabel(self.frame)
        self.set_pulseWidth_label_2.setObjectName("set_pulseWidth_label_2")
        self.gridLayout.addWidget(self.set_pulseWidth_label_2, 5, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.set_pulseWidth_2 = QtWidgets.QDoubleSpinBox(self.frame)
        self.set_pulseWidth_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.set_pulseWidth_2.setDecimals(2)
        self.set_pulseWidth_2.setMaximum(1000.0)
        self.set_pulseWidth_2.setProperty("value", 0.01)
        self.set_pulseWidth_2.setObjectName("set_pulseWidth_2")
        self.horizontalLayout_5.addWidget(self.set_pulseWidth_2)
        self.set_timeUnit_2 = QtWidgets.QComboBox(self.frame)
        self.set_timeUnit_2.setMaximumSize(QtCore.QSize(41, 22))
        self.set_timeUnit_2.setObjectName("set_timeUnit_2")
        self.set_timeUnit_2.addItem("")
        self.set_timeUnit_2.addItem("")
        self.set_timeUnit_2.addItem("")
        self.horizontalLayout_5.addWidget(self.set_timeUnit_2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.set_pulseWidth_3 = QtWidgets.QDoubleSpinBox(self.frame)
        self.set_pulseWidth_3.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.set_pulseWidth_3.setDecimals(1)
        self.set_pulseWidth_3.setMaximum(1000.0)
        self.set_pulseWidth_3.setProperty("value", 100.0)
        self.set_pulseWidth_3.setObjectName("set_pulseWidth_3")
        self.horizontalLayout_5.addWidget(self.set_pulseWidth_3)
        self.set_timeUnit_3 = QtWidgets.QComboBox(self.frame)
        self.set_timeUnit_3.setMaximumSize(QtCore.QSize(41, 22))
        self.set_timeUnit_3.setObjectName("set_timeUnit_3")
        self.set_timeUnit_3.addItem("")
        self.set_timeUnit_3.addItem("")
        self.set_timeUnit_3.addItem("")
        self.horizontalLayout_5.addWidget(self.set_timeUnit_3)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 2, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.set_pulseWidth_4 = QtWidgets.QDoubleSpinBox(self.frame)
        self.set_pulseWidth_4.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.set_pulseWidth_4.setDecimals(2)
        self.set_pulseWidth_4.setMaximum(1000.0)
        self.set_pulseWidth_4.setProperty("value", 0.01)
        self.set_pulseWidth_4.setObjectName("set_pulseWidth_4")
        self.horizontalLayout_6.addWidget(self.set_pulseWidth_4)
        self.set_timeUnit_4 = QtWidgets.QComboBox(self.frame)
        self.set_timeUnit_4.setMaximumSize(QtCore.QSize(41, 22))
        self.set_timeUnit_4.setObjectName("set_timeUnit_4")
        self.set_timeUnit_4.addItem("")
        self.set_timeUnit_4.addItem("")
        self.set_timeUnit_4.addItem("")
        self.horizontalLayout_6.addWidget(self.set_timeUnit_4)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.set_pulseWidth_5 = QtWidgets.QDoubleSpinBox(self.frame)
        self.set_pulseWidth_5.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.set_pulseWidth_5.setDecimals(1)
        self.set_pulseWidth_5.setMaximum(1000.0)
        self.set_pulseWidth_5.setProperty("value", 100.0)
        self.set_pulseWidth_5.setObjectName("set_pulseWidth_5")
        self.horizontalLayout_6.addWidget(self.set_pulseWidth_5)
        self.set_timeUnit_5 = QtWidgets.QComboBox(self.frame)
        self.set_timeUnit_5.setMaximumSize(QtCore.QSize(41, 22))
        self.set_timeUnit_5.setObjectName("set_timeUnit_5")
        self.set_timeUnit_5.addItem("")
        self.set_timeUnit_5.addItem("")
        self.set_timeUnit_5.addItem("")
        self.horizontalLayout_6.addWidget(self.set_timeUnit_5)
        self.gridLayout.addLayout(self.horizontalLayout_6, 7, 2, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.set_pulseWidth_7 = QtWidgets.QDoubleSpinBox(self.frame)
        self.set_pulseWidth_7.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.set_pulseWidth_7.setDecimals(2)
        self.set_pulseWidth_7.setMaximum(1000.0)
        self.set_pulseWidth_7.setProperty("value", 1.0)
        self.set_pulseWidth_7.setObjectName("set_pulseWidth_7")
        self.horizontalLayout_7.addWidget(self.set_pulseWidth_7)
        self.set_timeUnit_7 = QtWidgets.QComboBox(self.frame)
        self.set_timeUnit_7.setMaximumSize(QtCore.QSize(41, 22))
        self.set_timeUnit_7.setObjectName("set_timeUnit_7")
        self.set_timeUnit_7.addItem("")
        self.set_timeUnit_7.addItem("")
        self.set_timeUnit_7.addItem("")
        self.horizontalLayout_7.addWidget(self.set_timeUnit_7)
        self.gridLayout.addLayout(self.horizontalLayout_7, 8, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 10, 1, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.nPulses = QtWidgets.QSpinBox(self.frame)
        self.nPulses.setMinimum(5)
        self.nPulses.setMaximum(100)
        self.nPulses.setProperty("value", 20)
        self.nPulses.setObjectName("nPulses")
        self.horizontalLayout_8.addWidget(self.nPulses)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox)
        self.gridLayout.addLayout(self.horizontalLayout_8, 10, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
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
        self.statusbar = QtWidgets.QLineEdit(self.widget1)
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
        self.gridLayout_2.addWidget(self.widget1, 1, 0, 1, 1)
        self.graphWidget = PlotWidget(Switch)
        self.graphWidget.setMinimumSize(QtCore.QSize(411, 379))
        self.graphWidget.setObjectName("graphWidget")
        self.gridLayout_2.addWidget(self.graphWidget, 0, 1, 2, 1)

        self.retranslateUi(Switch)
        self.set_timeUnit_6.setCurrentIndex(1)
        self.set_timeUnit_2.setCurrentIndex(0)
        self.set_timeUnit_3.setCurrentIndex(1)
        self.set_timeUnit_4.setCurrentIndex(0)
        self.set_timeUnit_5.setCurrentIndex(1)
        self.set_timeUnit_7.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Switch)

    def retranslateUi(self, Switch):
        _translate = QtCore.QCoreApplication.translate
        Switch.setWindowTitle(_translate("Switch", "Form"))
        self.title_label.setText(_translate("Switch", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#0000ff;\">Switching Speed Test</span></p></body></html>"))
        self.setting_label.setText(_translate("Switch", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#aa0000;\">Settings</span></p></body></html>"))
        self.set_pulseWidth_label.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Set Pulse Width range</span></p></body></html>"))
        self.maxV_label.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Reset Voltage (V)</span></p></body></html>"))
        self.temperature.setToolTip(_translate("Switch", "<html><head/><body><p>Temperature range will depend on the type of heater</p></body></html>"))
        self.source.setItemText(0, _translate("Switch", "Tektronix AFG1022"))
        self.avgread_label.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Readings</span></p></body></html>"))
        self.file_name.setText(_translate("Switch", "sample.txt"))
        self.setV.setToolTip(_translate("Switch", "<html><head/><body><p>Max -10 V</p></body></html>"))
        self.resetV.setToolTip(_translate("Switch", "<html><head/><body><p>Max 10 V</p></body></html>"))
        self.reset_pulseWidth_label.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Reset Pulse width range</span></p></body></html>"))
        self.label.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Voltage Source</span></p></body></html>"))
        self.temp_check.setToolTip(_translate("Switch", "<html><head/><body><p>Use temperature only if temperature controller is attached</p></body></html>"))
        self.temp_check.setText(_translate("Switch", "Temperature (K)"))
        self.avg_label.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Average over</span></p></body></html>"))
        self.minV_label.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Set Voltage (V)</span></p></body></html>"))
        self.ncycles_label.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Read Voltage (V)</span></p></body></html>"))
        self.fname_label.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">File Name</span></p></body></html>"))
        self.Ilimit_label.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Current Limit (mA)</span></p></body></html>"))
        self.Ilimit.setToolTip(_translate("Switch", "<html><head/><body><p>The compliance current, which protects the sample from full breakdown</p></body></html>"))
        self.set_pulseWidth_label_3.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Ideal set pulse width</span></p></body></html>"))
        self.set_timeUnit_6.setToolTip(_translate("Switch", "<html><head/><body><p>Select time unit. Time below 50 ms may not be reliable for Keithley 2450</p></body></html>"))
        self.set_timeUnit_6.setItemText(0, _translate("Switch", "µs"))
        self.set_timeUnit_6.setItemText(1, _translate("Switch", "ms"))
        self.set_timeUnit_6.setItemText(2, _translate("Switch", "s"))
        self.set_pulseWidth_label_2.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Ideal set pulse width</span></p></body></html>"))
        self.set_timeUnit_2.setToolTip(_translate("Switch", "<html><head/><body><p>Select time unit. Time below 50 ms may not be reliable for Keithley 2450</p></body></html>"))
        self.set_timeUnit_2.setItemText(0, _translate("Switch", "µs"))
        self.set_timeUnit_2.setItemText(1, _translate("Switch", "ms"))
        self.set_timeUnit_2.setItemText(2, _translate("Switch", "s"))
        self.label_3.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">to</span></p></body></html>"))
        self.set_timeUnit_3.setToolTip(_translate("Switch", "<html><head/><body><p>Select time unit. Time below 50 ms may not be reliable for Keithley 2450</p></body></html>"))
        self.set_timeUnit_3.setItemText(0, _translate("Switch", "µs"))
        self.set_timeUnit_3.setItemText(1, _translate("Switch", "ms"))
        self.set_timeUnit_3.setItemText(2, _translate("Switch", "s"))
        self.set_timeUnit_4.setToolTip(_translate("Switch", "<html><head/><body><p>Select time unit. Time below 50 ms may not be reliable for Keithley 2450</p></body></html>"))
        self.set_timeUnit_4.setItemText(0, _translate("Switch", "µs"))
        self.set_timeUnit_4.setItemText(1, _translate("Switch", "ms"))
        self.set_timeUnit_4.setItemText(2, _translate("Switch", "s"))
        self.label_4.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">to</span></p></body></html>"))
        self.set_timeUnit_5.setToolTip(_translate("Switch", "<html><head/><body><p>Select time unit. Time below 50 ms may not be reliable for Keithley 2450</p></body></html>"))
        self.set_timeUnit_5.setItemText(0, _translate("Switch", "µs"))
        self.set_timeUnit_5.setItemText(1, _translate("Switch", "ms"))
        self.set_timeUnit_5.setItemText(2, _translate("Switch", "s"))
        self.set_timeUnit_7.setToolTip(_translate("Switch", "<html><head/><body><p>Select time unit. Time below 50 ms may not be reliable for Keithley 2450</p></body></html>"))
        self.set_timeUnit_7.setItemText(0, _translate("Switch", "µs"))
        self.set_timeUnit_7.setItemText(1, _translate("Switch", "ms"))
        self.set_timeUnit_7.setItemText(2, _translate("Switch", "s"))
        self.label_2.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Number of points</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Switch", "Log"))
        self.comboBox.setItemText(1, _translate("Switch", "Linear"))
        self.applyPulse_Button.setToolTip(_translate("Switch", "<html><head/><body><p>Click to start the experiment</p></body></html>"))
        self.applyPulse_Button.setText(_translate("Switch", "Apply Pulse"))
        self.clearGraph_Button.setToolTip(_translate("Switch", "<html><head/><body><p>Click to abort the experiment</p></body></html>"))
        self.clearGraph_Button.setText(_translate("Switch", "Clear graph and start new measurement"))
        self.save_Button.setText(_translate("Switch", "Save Data"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Switch = QtWidgets.QWidget()
    ui = Ui_Switch()
    ui.setupUi(Switch)
    Switch.show()
    sys.exit(app.exec_())
