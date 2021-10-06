# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 16:47:30 2021
USER5 is pospulse # custom positive pulse, already set in the instrument
USER6 is negpulse # custom negative pulse, already set in the instrument
@author: Badari
"""
# USB::0x0699::0x0353::1643763::INSTR
from pyvisa import ResourceManager, VisaIOError
from PyQt5.QtCore import QEventLoop, QTimer, QSize, QRect, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QWidget, QPushButton, QStatusBar, QApplication, QMainWindow

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(192, 129)
        MainWindow.setMinimumSize(QSize(192, 129))
        MainWindow.setMaximumSize(QSize(192, 129))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.trigger_Button = QPushButton(self.centralwidget)
        self.trigger_Button.setGeometry(QRect(60, 20, 75, 23))
        self.trigger_Button.setObjectName("trigger_Button")
        self.triggerNwait_Button = QPushButton(self.centralwidget)
        self.triggerNwait_Button.setGeometry(QRect(30, 60, 131, 23))
        self.triggerNwait_Button.setObjectName("triggerNwait_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.trigger_Button.setText(_translate("MainWindow", "Apply trigger"))
        self.triggerNwait_Button.setText(_translate("MainWindow", "Apply trigger and wait"))
        
class AFG1022:
    def __init__(self,adapter,**kwargs):
        if isinstance(adapter,str):
            rm = ResourceManager()
            self.inst = rm.open_resource(adapter)
            self.address = adapter
        else:
            raise VisaIOError(-1073807346)
        
    def getinfo(self):
        print(self.inst.query('*IDN?'))
    
    def ask(self,cmd):
        return self.inst.query(cmd)
    
    def write(self,cmd):
        self.inst.write(cmd)
    
    def read(self):
        self.inst.read()
        
    def configure_pulse_measurement(self):
        self.write("SOURce1:BURST:MODE TRIGgered")
        self.write("SOURce1:BURST:NCYCles 1")
        self.write("SOURce1:BURST:STATE ON")
    
    def setSinglePulse(self,volts,pulseWidth): # seconds
        if pulseWidth > 5.0: # max width is is set to 5 seconds
            pulseWidth = 5.0
            print("Pulse width exceeded max limit, reset to 5 s.")
        elif pulseWidth < 1e-7: # min width is 100 ns -> machine limit
            pulseWidth = 1e-7
            print("Pulse width less than min limit, reset to 100 ns.")
        self.write('SOURce1:FREQuency:FIXed {}'.format((1/(pulseWidth*2))))
        if volts >= 0.001 and volts <= 10:
            self.write("SOURce1:FUNCtion:SHAPe USER5")
            self.write('SOURce1:VOLTage:LEVel:IMMediate:AMPLitude {}'.format(volts/2))
            self.write('SOURce1:VOLTage:LEVel:IMMediate:OFFSet {}'.format(volts/4))
        elif volts < -0.001 and volts >= -10:
            self.write("SOURce1:FUNCtion:SHAPe USER6")
            self.write('SOURce1:VOLTage:LEVel:IMMediate:AMPLitude {}'.format(-volts/2))
            self.write('SOURce1:VOLTage:LEVel:IMMediate:OFFSet {}'.format(volts/4))
        else:
            print("ERROR! Voltage out of range. Select within (-5V,5V) and magnitude greater than 1 mV")
            
    def setPulses(self,v,pw,n): # multiple pulses
        pass
    
    def apply_pulse(self,volts,pulse_width):
        pass
    
    def trgNwait(self):
        pw = 1000/float(self.ask('source1:frequency:fixed?'))  # milliseconds
        nc = int(self.ask("SOURce1:BURST:NCYCles?"))
        self.trigger()
        if (pw*nc) < 10: # fix min wait time as 10 ms.
            pw = 10
            nc = 1
        loop = QEventLoop()
        QTimer.singleShot(pw*nc, loop.quit)
        loop.exec_()
    
    def trigger(self):
        self.write('*TRG')
        
    def close(self):
        self.inst.close()
        
    def output(self,state):
        self.write('OUTPut1:STATe {}'.format(state))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    afg = AFG1022('USB::0x0699::0x0353::1643763::INSTR')
    ui.trigger_Button.clicked.connect(afg.trigger)
    ui.triggerNwait_Button.clicked.connect(afg.trgNwait)
    sys.exit(app.exec_())
        