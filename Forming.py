# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Forming.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, ViewBox, mkPen
from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal
from utilities import unique_filename, checkInstrument
from PyQt5.QtWidgets import QMessageBox
from numpy import linspace
from time import sleep
from functools import partial

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
        self.source = QtWidgets.QComboBox(self.frame)
        self.source.setEnabled(False)
        self.source.setObjectName("source")
        self.source.addItem("")
        self.gridLayout.addWidget(self.source, 2, 2, 1, 1)
        self.source_label = QtWidgets.QLabel(self.frame)
        self.source_label.setObjectName("source_label")
        self.gridLayout.addWidget(self.source_label, 2, 1, 1, 1)
        self.temp_check = QtWidgets.QCheckBox(self.frame)
        self.temp_check.setObjectName("temp_check")
        self.gridLayout.addWidget(self.temp_check, 9, 1, 1, 1)
        self.fname_label = QtWidgets.QLabel(self.frame)
        self.fname_label.setObjectName("fname_label")
        self.gridLayout.addWidget(self.fname_label, 1, 1, 1, 1)
        self.vEnd_label = QtWidgets.QLabel(self.frame)
        self.vEnd_label.setObjectName("vEnd_label")
        self.gridLayout.addWidget(self.vEnd_label, 4, 1, 1, 1)
        self.vStart_label = QtWidgets.QLabel(self.frame)
        self.vStart_label.setObjectName("vStart_label")
        self.gridLayout.addWidget(self.vStart_label, 3, 1, 1, 1)
        self.temperature = QtWidgets.QDoubleSpinBox(self.frame)
        self.temperature.setEnabled(False)
        self.temperature.setMaximum(600.0)
        self.temperature.setProperty("value", 300.0)
        self.temperature.setObjectName("temperature")
        self.gridLayout.addWidget(self.temperature, 9, 2, 1, 1)
        self.file_name = QtWidgets.QLineEdit(self.frame)
        self.file_name.setObjectName("file_name")
        self.gridLayout.addWidget(self.file_name, 1, 2, 1, 1)
        self.vEnd = QtWidgets.QDoubleSpinBox(self.frame)
        self.vEnd.setDecimals(3)
        self.vEnd.setMinimum(-50.0)
        self.vEnd.setMaximum(49.0)
        self.vEnd.setSingleStep(0.1)
        self.vEnd.setProperty("value", 3.0)
        self.vEnd.setObjectName("vEnd")
        self.gridLayout.addWidget(self.vEnd, 4, 2, 1, 1)
        self.iLimit_label = QtWidgets.QLabel(self.frame)
        self.iLimit_label.setObjectName("iLimit_label")
        self.gridLayout.addWidget(self.iLimit_label, 5, 1, 1, 1)
        self.iLimit = QtWidgets.QDoubleSpinBox(self.frame)
        self.iLimit.setDecimals(3)
        self.iLimit.setMaximum(500.0)
        self.iLimit.setSingleStep(0.001)
        self.iLimit.setProperty("value", 1.0)
        self.iLimit.setObjectName("iLimit")
        self.gridLayout.addWidget(self.iLimit, 5, 2, 1, 1)
        self.vStart = QtWidgets.QDoubleSpinBox(self.frame)
        self.vStart.setDecimals(3)
        self.vStart.setMinimum(-50.0)
        self.vStart.setMaximum(49.0)
        self.vStart.setSingleStep(0.1)
        self.vStart.setProperty("value", 0.0)
        self.vStart.setObjectName("vStart")
        self.gridLayout.addWidget(self.vStart, 3, 2, 1, 1)
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
        Forming.setWindowTitle(_translate("Forming", "Form"))
        self.title_label.setText(_translate("Forming", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#0000ff;\">Forming</span></p></body></html>"))
        self.setting_label.setText(_translate("Forming", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#aa0000;\">Settings</span></p></body></html>"))
        self.source.setItemText(0, _translate("Forming", "Keithley 2450"))
        self.source_label.setText(_translate("Forming", "<html><head/><body><p><span style=\" font-size:10pt;\">Voltage Source</span></p></body></html>"))
        self.temp_check.setToolTip(_translate("Forming", "<html><head/><body><p>Use temperature only if temperature controller is attached</p></body></html>"))
        self.temp_check.setText(_translate("Forming", "Temperature (K)"))
        self.fname_label.setText(_translate("Forming", "<html><head/><body><p><span style=\" font-size:10pt;\">File Name</span></p></body></html>"))
        self.vEnd_label.setText(_translate("Forming", "<html><head/><body><p><span style=\" font-size:10pt;\">Voltage End (V)</span></p></body></html>"))
        self.vStart_label.setText(_translate("Forming", "<html><head/><body><p><span style=\" font-size:10pt;\">Voltage Start (V)</span></p></body></html>"))
        self.temperature.setToolTip(_translate("Forming", "<html><head/><body><p>Temperature range will depend on the type of heater</p></body></html>"))
        self.file_name.setText(_translate("Forming", "sample.txt"))
        self.vEnd.setToolTip(_translate("Forming", "<html><head/><body><p>Max -10 V</p></body></html>"))
        self.iLimit_label.setText(_translate("Forming", "<html><head/><body><p><span style=\" font-size:10pt;\">Current Limit (mA)</span></p></body></html>"))
        self.iLimit.setToolTip(_translate("Forming", "<html><head/><body><p>The compliance current, which protects the sample from full breakdown</p></body></html>"))
        self.vStart.setToolTip(_translate("Forming", "<html><head/><body><p>Max -10 V</p></body></html>"))
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
        self.abort_Button.clicked.connect(self.abort)
        self.start_Button.setShortcut('Ctrl+Return')
        self.abort_Button.setShortcut('Ctrl+q')
        self.initialize_plot()
        self.k2450.nplc = 1
        self.filename = sName
        self.file_name.setText(self.filename)
        self.measurement_status = "Idle"
        self.params = {
            "VStart": 0,
            "VEnd": 3,
            "ILimit": 1/1000,
            "temperature": 300,
            "temp_check": 0}
        self.parameters = list(self.params.values())
    
    def load_parameters(self):
        try:
            self.vStart.setValue(self.parameters[0])
            self.vEnd.setValue(self.parameters[1])
            self.iLimit.setValue(self.parameters[2]*1000)
            self.temperature.setValue(self.parameters[3])
            self.temp_check.setChecked(self.parameters[4])
        except Exception:
            pass
        
    def initialize_plot(self):
        """
        Initialize the plot to display IV loop.

        Returns
        -------
        None.

        """
        styles = {'color': 'r', 'font-size': '20px'}
        self.graphWidget.setLabel('left', '|Current (A)|', **styles)
        self.graphWidget.setLabel('bottom', 'Voltage (V)', **styles)
        #self.graphWidget.setRange(QtCore.QRectF(self.minV.value(), 1e-12, self.maxV.value()-self.minV.value(), self.Ilimit.value()), padding=0)
        #self.graphWidget.getPlotItem().setLogMode(None, True)
        self.graphWidget.addLegend()
    
    def plotData(self, data):
        self.volts.append(data[0])
        self.currents.append(abs(data[1]))
        self.data_line.setData(self.volts, self.currents)
    
    def disable_input(self):
        self.vStart.setEnabled(False)
        self.vEnd.setEnabled(False)
        self.iLimit.setEnabled(False)
        self.start_Button.setEnabled(False)
        self.abort_Button.setEnabled(True)
    
    def enable_input(self):
        self.vStart.setEnabled(True)
        self.vEnd.setEnabled(True)
        self.iLimit.setEnabled(True)
        self.start_Button.setEnabled(True)
        self.abort_Button.setEnabled(False)
        
    def startThread(self,vPoints,iPoints):
        self.thread = QThread()
        self.worker = Worker(self.k2450,self.fullfilename)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(partial(self.worker.start_forming,vPoints,iPoints))
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.data.connect(self.plotData)
        self.thread.finished.connect(self.stop_Forming)
        self.thread.start()
        
    def start_Forming(self):
        self.params = {
            "VStart": self.vStart.value(),
            "VEnd": self.vEnd.value(),
            "ILimit": self.iLimit.value()/1000,
            "temperature": self.temperature.value(),
            "temp_check": int(self.temp_check.isChecked())}
        self.measurement_status = "Running"
        self.parameters = list(self.params.values())
        self.disable_input()
        self.fullfilename = unique_filename('.',prefix=self.filename,ext='dat',datetimeformat="")
        nPoints = int(abs(self.vEnd.value()-self.vStart.value())) * 10 + 1
        if nPoints < 11:
            nPoints = 11
        vPoints = linspace(self.vStart.value(),self.vEnd.value(),nPoints)
        nIpoints = int(abs(self.iLimit.value())) * 10 + 1
        if nIpoints < 11:
            nIpoints = 11
        iPoints = linspace(0,self.iLimit.value(),nIpoints)/1000
        pen1 = mkPen(color=(0, 0, 255), width=2)
        self.volts = [vPoints[0]]
        self.currents = [iPoints[0]]
        self.graphWidget.clear()
        self.data_line = self.graphWidget.plot(self.volts, self.currents, pen=pen1)
        del self.volts[0]
        del self.currents[0]
        self.startThread(vPoints,iPoints)
    
    def abort(self):
        self.worker.stopcall.emit()
    
    def stop_Forming(self):
        self.measurement_status = "Idle"
        self.enable_input()
    
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
                self.abort()
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
    
    def __init__(self, k2450=None, fullfilename="sample.dat"):
        super(Worker,self).__init__()
        self.stopCall = False
        self.k2450 = k2450
        self.fullfilename = fullfilename
        self.stopcall.connect(self.stopcalled)
     
    def stopcalled(self):
        self.stopCall = True
    
    def start_forming(self, vPoints, iPoints):
        l = 1
        i = iPoints[l]
        self.k2450.measure_current(nplc=2)
        self.k2450.source_voltage = 0
        self.k2450.write(":Sense:count 1")
        self.k2450.write("SOUR:VOLT:READ:BACK ON")
        self.k2450.enable_source()
        
        file = open(self.fullfilename,'w')
        file.write("#Voltage Source and current measured from Keithely 2450 Sourcemeter.\n")
        file.write("# Voltage Limit = {}\n".format(vPoints[-1]))
        file.write("# Current Limit = {}\n".format(iPoints[-1]))
        file.write("# Applied Voltgage (V)\tCurrent(A)\n")
        iFlag = False
        for v in vPoints[1:]:
            self.k2450.write("SOUR:VOLT:ILIM {}".format(i))
            self.k2450.source_voltage = v
            m = 0
            while True:
                if self.stopCall:
                    iFlag = True
                    break
                if int(self.k2450.ask("SOUR:VOLT:ILIM:TRIP?").strip()):
                    m = 11
                    if l < len(iPoints)-1:
                        l = l+1
                        i = iPoints[l]
                    else:
                        iFlag = True # if the user specified current limit is reached
                        
                else:
                    m = m + 1
                sleep(0.1)
                if m > 10:
                    values = self.k2450.ask(":read? 'defbuffer1', SOURce, READing").strip().split(',')
                    file.write(values[0]+'\t'+values[1]+'\n')
                    file.flush()
                    volt = float(values[0])
                    current = float(values[1])
                    self.data.emit([volt,current])
                    break
            if iFlag:
                break
        file.close()
        self.k2450.source_voltage = 0
        self.k2450.disable_source()
        self.finished.emit()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Forming = QtWidgets.QWidget()
    k2450, k2700, _ = checkInstrument(test = True)
    ui = app_Forming(Forming,k2450,k2700)
    ui.show()
    app.exec_()
    app.quit()

