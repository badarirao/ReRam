# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'switching_test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Switch(object):
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
        self.Rplot = PlotWidget(Switch)
        self.Rplot.setMinimumSize(QtCore.QSize(411, 379))
        self.Rplot.setObjectName("Rplot")
        self.gridLayout_2.addWidget(self.Rplot, 0, 1, 2, 1)
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
        self.title_label.setText(_translate("Switch", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#0000ff;\">Switching Test</span></p></body></html>"))
        self.setting_label.setText(_translate("Switch", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#aa0000;\">Settings</span></p></body></html>"))
        self.set_timeUnit.setToolTip(_translate("Switch", "<html><head/><body><p>Select time unit. Time below 50 ms may not be reliable for Keithley 2450</p></body></html>"))
        self.set_timeUnit.setItemText(0, _translate("Switch", "us"))
        self.set_timeUnit.setItemText(1, _translate("Switch", "ms"))
        self.set_timeUnit.setItemText(2, _translate("Switch", "s"))
        self.label_2.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Number of pulse sets</span></p></body></html>"))
        self.set_pulseWidth_label.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Set Pulse Width</span></p></body></html>"))
        self.Ilimit.setToolTip(_translate("Switch", "<html><head/><body><p>The compliance current, which protects the sample from full breakdown</p></body></html>"))
        self.temperature.setToolTip(_translate("Switch", "<html><head/><body><p>Temperature range will depend on the type of heater</p></body></html>"))
        self.maxV_label.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Reset Voltage (V)</span></p></body></html>"))
        self.fname_label.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">File Name</span></p></body></html>"))
        self.ncycles_label.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Read Voltage (V)</span></p></body></html>"))
        self.resetV.setToolTip(_translate("Switch", "<html><head/><body><p>Max 10 V</p></body></html>"))
        self.reset_timeUnit.setToolTip(_translate("Switch", "<html><head/><body><p>Select time unit. Time below 50 ms may not be reliable for Keithley 2450</p></body></html>"))
        self.reset_timeUnit.setItemText(0, _translate("Switch", "us"))
        self.reset_timeUnit.setItemText(1, _translate("Switch", "ms"))
        self.reset_timeUnit.setItemText(2, _translate("Switch", "s"))
        self.minV_label.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Set Voltage (V)</span></p></body></html>"))
        self.avgread_label.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Readings</span></p></body></html>"))
        self.file_name.setText(_translate("Switch", "Sample_Switch"))
        self.source.setItemText(0, _translate("Switch", "Keysight B2902B"))
        self.source.setItemText(1, _translate("Switch", "Keithley 2450"))
        self.source.setItemText(2, _translate("Switch", "Tektronix AFG1022"))
        self.Ilimit_label.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Current Limit (mA)</span></p></body></html>"))
        self.temp_check.setToolTip(_translate("Switch", "<html><head/><body><p>Use temperature only if temperature controller is attached</p></body></html>"))
        self.temp_check.setText(_translate("Switch", "Temperature (K)"))
        self.avg_label.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Average over</span></p></body></html>"))
        self.label.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Voltage Source</span></p></body></html>"))
        self.reset_pulseWidth_label.setText(_translate("Switch", "<html><head/><body><p><span style=\" font-size:10pt;\">Reset Pulse width</span></p></body></html>"))
        self.setV.setToolTip(_translate("Switch", "<html><head/><body><p>Max -10 V</p></body></html>"))
        self.comment_checkBox.setText(_translate("Switch", "Add Comments"))
        self.applyPulse_Button.setToolTip(_translate("Switch", "<html><head/><body><p>Click to start the experiment</p></body></html>"))
        self.applyPulse_Button.setText(_translate("Switch", "Apply Pulse"))
        self.clearGraph_Button.setToolTip(_translate("Switch", "<html><head/><body><p>Click to abort the experiment</p></body></html>"))
        self.clearGraph_Button.setText(_translate("Switch", "Clear graph and start new measurement"))
        self.save_Button.setText(_translate("Switch", "Save Data"))
        self.stop_Button.setText(_translate("Switch", "Stop"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Switch = QtWidgets.QWidget()
    ui = Ui_Switch()
    ui.setupUi(Switch)
    Switch.show()
    sys.exit(app.exec_())

