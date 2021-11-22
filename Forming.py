# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Forming.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, ViewBox, mkPen, intColor
from PyQt5.QtCore import Qt
from utilities import unique_filename, FakeAdapter, checkInstrument

class Ui_Forming(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_Forming, self).__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)
    
    def setupUi(self, Forming):
        Forming.setObjectName("Forming")
        Forming.resize(1050, 600)
        Forming.setMinimumSize(QtCore.QSize(1050, 550))
        self.gridLayout_2 = QtWidgets.QGridLayout(Forming)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(Forming)
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
        self.iLimit_label = QtWidgets.QLabel(self.frame)
        self.iLimit_label.setObjectName("iLimit_label")
        self.gridLayout.addWidget(self.iLimit_label, 4, 1, 1, 1)
        self.source = QtWidgets.QComboBox(self.frame)
        self.source.setEnabled(False)
        self.source.setObjectName("source")
        self.source.addItem("")
        self.gridLayout.addWidget(self.source, 2, 2, 1, 1)
        self.file_name = QtWidgets.QLineEdit(self.frame)
        self.file_name.setObjectName("file_name")
        self.gridLayout.addWidget(self.file_name, 1, 2, 1, 1)
        self.temp_check = QtWidgets.QCheckBox(self.frame)
        self.temp_check.setObjectName("temp_check")
        self.gridLayout.addWidget(self.temp_check, 10, 1, 1, 1)
        self.temperature = QtWidgets.QDoubleSpinBox(self.frame)
        self.temperature.setEnabled(False)
        self.temperature.setMaximum(600.0)
        self.temperature.setProperty("value", 300.0)
        self.temperature.setObjectName("temperature")
        self.gridLayout.addWidget(self.temperature, 10, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.vLimit = QtWidgets.QDoubleSpinBox(self.frame)
        self.vLimit.setDecimals(3)
        self.vLimit.setMinimum(-50.0)
        self.vLimit.setMaximum(49.0)
        self.vLimit.setSingleStep(0.1)
        self.vLimit.setProperty("value", -3.0)
        self.vLimit.setObjectName("vLimit")
        self.horizontalLayout_2.addWidget(self.vLimit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 2, 1, 1)
        self.source_label = QtWidgets.QLabel(self.frame)
        self.source_label.setObjectName("source_label")
        self.gridLayout.addWidget(self.source_label, 2, 1, 1, 1)
        self.fname_label = QtWidgets.QLabel(self.frame)
        self.fname_label.setObjectName("fname_label")
        self.gridLayout.addWidget(self.fname_label, 1, 1, 1, 1)
        self.vLimit_label = QtWidgets.QLabel(self.frame)
        self.vLimit_label.setObjectName("vLimit_label")
        self.gridLayout.addWidget(self.vLimit_label, 3, 1, 1, 1)
        self.iLimit = QtWidgets.QDoubleSpinBox(self.frame)
        self.iLimit.setDecimals(3)
        self.iLimit.setMaximum(500.0)
        self.iLimit.setSingleStep(0.001)
        self.iLimit.setProperty("value", 1.0)
        self.iLimit.setObjectName("iLimit")
        self.gridLayout.addWidget(self.iLimit, 4, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        self.widget1 = QtWidgets.QWidget(Forming)
        self.widget1.setMinimumSize(QtCore.QSize(350, 151))
        self.widget1.setMaximumSize(QtCore.QSize(350, 154))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.start_Button = QtWidgets.QPushButton(self.widget1)
        self.start_Button.setObjectName("start_Button")
        self.verticalLayout.addWidget(self.start_Button)
        self.abort_Button = QtWidgets.QPushButton(self.widget1)
        self.abort_Button.setObjectName("abort_Button")
        self.verticalLayout.addWidget(self.abort_Button)
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
        self.graphWidget = PlotWidget(Forming, viewBox=ViewBox(border=mkPen(color='k', width=2)))
        self.graphWidget.setBackground((255, 182, 193, 25))
        self.graphWidget.setMinimumSize(QtCore.QSize(411, 379))
        self.graphWidget.setObjectName("graphWidget")
        self.gridLayout_2.addWidget(self.graphWidget, 0, 1, 2, 1)

        self.retranslateUi(Forming)
        QtCore.QMetaObject.connectSlotsByName(Forming)

    def retranslateUi(self, Forming):
        _translate = QtCore.QCoreApplication.translate
        Forming.setWindowTitle(_translate("Forming", "Forming Program"))
        self.title_label.setText(_translate("Forming", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#0000ff;\">Forming</span></p></body></html>"))
        self.setting_label.setText(_translate("Forming", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#aa0000;\">Settings</span></p></body></html>"))
        self.iLimit_label.setText(_translate("Forming", "<html><head/><body><p><span style=\" font-size:10pt;\">Current Limit (mA)</span></p></body></html>"))
        self.source.setItemText(0, _translate("Forming", "Keithley 2450"))
        self.file_name.setText(_translate("Forming", "sample.txt"))
        self.temp_check.setToolTip(_translate("Forming", "<html><head/><body><p>Use temperature only if temperature controller is attached</p></body></html>"))
        self.temp_check.setText(_translate("Forming", "Temperature (K)"))
        self.temperature.setToolTip(_translate("Forming", "<html><head/><body><p>Temperature range will depend on the type of heater</p></body></html>"))
        self.vLimit.setToolTip(_translate("Forming", "<html><head/><body><p>Max -10 V</p></body></html>"))
        self.source_label.setText(_translate("Forming", "<html><head/><body><p><span style=\" font-size:10pt;\">Voltage Source</span></p></body></html>"))
        self.fname_label.setText(_translate("Forming", "<html><head/><body><p><span style=\" font-size:10pt;\">File Name</span></p></body></html>"))
        self.vLimit_label.setText(_translate("Forming", "<html><head/><body><p><span style=\" font-size:10pt;\">Voltage Limit (V)</span></p></body></html>"))
        self.iLimit.setToolTip(_translate("Forming", "<html><head/><body><p>The compliance current, which protects the sample from full breakdown</p></body></html>"))
        self.start_Button.setToolTip(_translate("Forming", "<html><head/><body><p>Click to start the experiment</p></body></html>"))
        self.start_Button.setText(_translate("Forming", "Start"))
        self.abort_Button.setToolTip(_translate("Forming", "<html><head/><body><p>Click to abort the experiment</p></body></html>"))
        self.abort_Button.setText(_translate("Forming", "Abort"))

class app_Forming(Ui_Forming):
    """The IV-Loop app module."""

    def __init__(self, parent=None, k2450=None, k2700 = None, sName="Sample_IV.txt"):
        super(app_Forming, self).__init__(parent)
        self.parent = parent
        self.file_name.setReadOnly(True)
        self.k2450 = k2450
        self.k2700 = k2700
        self.abort_Button.setEnabled(False)
        self.stop_flag = False
        self.start_Button.clicked.connect(self.start_Forming)
        self.abort_Button.clicked.connect(self.stop_Forming)
        self.start_Button.setShortcut('Ctrl+Return')
        self.abort_Button.setShortcut('Ctrl+q')
        self.initialize_plot()
        self.k2450.nplc = 1
        self.filename = sName
        self.file_name.setText(self.filename)
        self.measurement_status = "Idle"
        self.params = {
            "VLimit": 3,
            "ILimit": 1/1000,
            "temperature": 300,
            "temp_check": 0}
        self.parameters = list(self.params.values())
    
    def initialize_plot(self):
        pass
    
    def start_Forming(self):
        pass
    
    def stop_Forming(self):
        pass
    
    def keyPressEvent(self, event):
        """Close application from escape key.

        results in QMessageBox dialog from closeEvent, good but how/why?
        """
        if event.key() == Qt.Key_Escape:
            self.close()
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Forming = QtWidgets.QWidget()
    #k2450, k2700, _ = checkInstrument(test = True)
    k2450 = FakeAdapter()
    k2700 = FakeAdapter()
    ui = app_Forming(Forming,k2450,k2700)
    ui.show()
    app.exec_()
    app.quit()

