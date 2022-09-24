"""
Module to initialize the main menu.

Works on Python 3.8.5, Windows 10.
Not tested for other Python versions or OS.

# TODO: when mux is not connected, source meter is expected to be connected by default.
        hence, use of function generator must be disabled.
# TODO: Program to investigate switching speed, using Keysight SMU.
# TODO: Allow for both SCPI and TSP commands (currently only SCPI works).
# TODO: Not able to cleanly exit if no instrument is connected and TESTING = False.
# TODO: correct the tab order of all the windows.
# TODO: Bug: minimizing the main window also minimized the child window, even if child.show() is given later.
# TODO: clear the graphs in all apps when directory of filename is changed.
# TODO: Implement threading to plot data in a separate thread as a separate process.
# TODO: Include date, start and end time of experiment in saved file.
# TODO: Include timestamp for each datapoint
# TODO: BUG: If soucemeter is Idle for long time, it connects, but no command works, gives visaerror.
# TODO: Correct the channel connections after Sample and instrument connections in MUX have been modified.
# TODO: Enable using cryochamber.
# TODO: Connect chino temperature controller, and Linkam temperature controller.
# TODO: if function generator is not connected, disable usage of MUX also!
# TODO: MUX should only change AFG and SMU connection. It should not interfere with sample connections
# TODO: If function generator is connected with another sample, make sure this program will not use function generator
# TODO: combine all common import modules and put it in utilities, and import from
# TODO: Keysight SMU can probably do PUND current measurement. Apply pulse, and measure current decay (min 20 us interval)
"""
# 'KEITHLEY INSTRUMENTS,MODEL 2450,04488850,1.7.3c\n'
# 'KEITHLEY INSTRUMENTS INC.,MODEL 2700,1150720,B09  /A02  \n'
# 'TEKTRONIX,AFG1022,1643763,SCPI:99.0 FV:V1.2.3\n'
#  except VisaIOError:

# 2700: when power on, by default all switches are opened
# You can save the presently closed channels into instrument using: *SAV 1 (saves into 1st place, can be 2, 3 or 4)    
# TO recall during startup, *RCL 1
# To automatically recall during startup: SYST:POS SAV1 (This will directly keep closed channels in sav1 as closed.)
import sys
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal
from functools import partial
from Memory import Ui_Memory
from IVloop import app_IVLoop
from RVloop import app_RVLoop
from Switch import app_Switch
from Fatigue import app_Fatigue
from Retention import app_Retention
from Forming import app_Forming
from utilities import get_valid_filename, connect_known_instruments, connect_sample_with_SMU, checkMUX_SMU

TESTING = True  #if True, will use a Fakeadapter when no instrument connected

class Worker(QObject):
    finished = pyqtSignal()
    adapters = pyqtSignal(list)
    
    def __init__(self):
        super(Worker,self).__init__()
        
    def connect_instrument(self,a1,a2,a3,a4,test):
        instruments = list(connect_known_instruments(a1,a2,a3,a4,test))
        self.adapters.emit(instruments)
        self.finished.emit()


# creating VLine class
class VLine(QtWidgets.QFrame):

    # a simple Vertical line
    def __init__(self):
        super(VLine, self).__init__()
        self.setFrameShape(self.VLine | self.Sunken)

class MainWindow(QtWidgets.QMainWindow, Ui_Memory):
    """Class to initialize the main menu."""

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        """
        contents of address.txt:
            line 1: path where SettingFile.dnd is (or should be) stored
        """
        self.abortMessage = False
        self.checkPaths()
        self.setupUi(self)
        self.filename.setText(self.sampleID)
        self.dir_Button.clicked.connect(self.openDir)
        self.dir_Button.setShortcut('Ctrl+d')
        self.dir_Button.setAutoDefault(True)
        self.iv_button.clicked.connect(self.open_ivloop)
        self.iv_button.setAutoDefault(True)
        self.rv_button.clicked.connect(self.open_rvloop)
        self.rv_button.setAutoDefault(True)
        self.switch_button.clicked.connect(self.open_switchTest)
        self.switch_button.setAutoDefault(True)
        self.inst_button.clicked.connect(self.check_instrument_connection)
        self.inst_button.setAutoDefault(True)
        self.inst_button.setShortcut('Ctrl+r')
        self.endurance_button.clicked.connect(self.open_fatigue)
        self.endurance_button.setAutoDefault(True)
        self.retention_button.clicked.connect(self.open_retention)
        self.retention_button.setAutoDefault(True)
        self.forming_button.setAutoDefault(True)
        self.forming_button.clicked.connect(self.open_forming)
        self.speed_button.setEnabled(False)
        self.aging_button.setEnabled(False)
        self.neuromorphic_Button.setEnabled(False)
        self.memristor_button.setEnabled(False)
        self.temperature_button.setEnabled(False)
        self.batch_button.setEnabled(False)
        self.filename.editingFinished.connect(self.setFilename)
        self.setFilename(1)  # 1 indicates initial setting of filename
        self.abort = False
        self.connection = 1
        self.currentSample = 0
        self.configLabel = QtWidgets.QLabel("")
        self.configLabel.setText("2-wire sense configuration")
        self.statusBar().addPermanentWidget(self.configLabel)
        self.statusBar().addPermanentWidget(VLine())
        self.instLabel = QtWidgets.QLabel("")
        self.statusBar().addPermanentWidget(self.instLabel)
        self.comment_checkBox.stateChanged.connect(self.updateCommentBox)
        self.check_instrument_connection()
        self.actionSet_2_wire_configuration.triggered.connect(self.set_two_wire_config)
        self.actionSet_4_wire_configuration.triggered.connect(self.set_four_wire_config)

    def updateCommentBox(self):
        if self.comment_checkBox.isChecked():
            self.commentBox.setEnabled(True)
            self.commentBox.blockSignals(False)
        else:
            self.commentBox.setEnabled(False)
            self.commentBox.blockSignals(True)
    
    def checkPaths(self):
        """
        Check for paths to store data and setting files.
        
        address.txt stores path where SettingFile.dnd is stored.
        If address.txt not found, or path in it is invalid, 
        put SettingFile.dnd in current working directory.
        
        SettingFile.dnd stores path where last measurement data is stored,
        and also the last used filename. 
        If SettingFile.dnd does not exist or if path given in SettingFile.dnd 
        does not exist, set desktop as the default path to store the 
        measurement data. 
        If desktop is not found in C: drive, then make current working 
        directory as default path to store measurement data. 
        Use default sample name as "Sample".

        Returns
        -------
        None.

        """
        self.settingPath = ""
        self.sampleID = ''
        self.initialPath = os.getcwd()
        self.k2450Addr = self.k2700Addr = self.AFG1022Addr = self.B2902bAddr = ''
        try:
            with open('address.txt') as f:
                self.settingPath = f.readline().strip()# get path of SettingFile.dnd
                lines = f.readlines()
                for line in lines:
                    l = line.split()
                    detail = " ".join(l[1:])
                    if '2450' in detail:
                        self.k2450Addr = l[0]
                    elif '2700' in detail:
                        self.k2700Addr = l[0]
                    elif '1022' in detail:
                        self.AFG1022Addr = l[0]
                    elif '2902b' in detail.lower():
                        self.B2902bAddr = l[0]
                os.chdir(self.settingPath)
        except FileNotFoundError:
            with open('address.txt','w') as f:
                f.write(self.initialPath)
            self.settingPath = self.initialPath
            
        # set default path to store measured data as desktop
        self.defaultPath = os.path.join(
            os.path.expandvars("%userprofile%"), "Desktop")
        # set default path as current directory if desktop is not found in C drive
        if not os.path.exists(self.defaultPath):
            self.defaultPath = self.initialPath 

        # SettingFile contains last used filename & its location, which is loaded initially
        try:
            with open('SettingFile.dnd', 'r') as f:
                self.currPath = f.readline().strip('\n\r')
                self.sampleID = get_valid_filename(f.readline().strip())
                if self.sampleID == '' or self.sampleID.isspace():
                    self.sampleID = "Sample"
                os.chdir(self.currPath)
        except FileNotFoundError: # if SettingFile does not exist, set default name
            self.currPath = self.defaultPath
            os.chdir(self.defaultPath)
            self.sampleID = "Sample"
        
    def check_instrument_connection(self):
        global TESTING
        try:
            self.smu.close()
            self.k2700.close()
            self.afg1022.close()
        except:
            pass
        self.inst_button.setDisabled(True)
        self.dir_Button.setDisabled(True)
        self.filename.setDisabled(True)
        self.iv_button.setDisabled(True)
        self.rv_button.setDisabled(True)
        self.switch_button.setDisabled(True)
        self.endurance_button.setDisabled(True)
        self.retention_button.setDisabled(True)
        self.forming_button.setDisabled(True)
        self.instLabel.setText('Establishing instrument connection... Please wait')
        
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        a1 = self.k2450Addr
        a2 = self.k2700Addr
        a3 = self.AFG1022Addr
        a4 = self.B2902bAddr
        self.thread.started.connect(partial(self.worker.connect_instrument,a1,a2,a3,a4,TESTING))
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.adapters.connect(self.getInstruments)
        self.thread.finished.connect(self.afterConnect)
        self.thread.finished.connect(self.initialize_apps)
        self.thread.start()
    
    def getInstruments(self,instruments):
        self.smu = instruments[0]
        self.k2700 = instruments[1]
        self.afg1022 = instruments[2]
        
    def afterConnect(self):
        self.connection, self.currentSample = checkMUX_SMU(self.k2700)
        if self.connection == 0:
            info = QMessageBox(self)
            info.setWindowTitle("Multiplexer connection error")
            info.setIcon(QMessageBox.Critical)
            info.setText(
                "Looks like Sourcemeter is not connected in multiplexer. Run the MUX program and fix the connection. Press cancel if using external connection, and you want to continue measurement.")
            info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            reply = info.exec()
            if reply == QMessageBox.Ok:
                self.abortMessage = True
                self.close()
        elif self.connection == -1:
            info = QMessageBox(self)
            info.setWindowTitle("Multiplexer connection error")
            info.setIcon(QMessageBox.Critical)
            info.setText(
                "Looks like Sourcemeter is connected for 4 probe measurement. This software currently only supports 2-probe measurement. Run the MUX program and fix the connection. Press cancel if using external connection, and you want to continue measurement.")
            info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            reply = info.exec()
            if reply == QMessageBox.Ok:
                self.abortMessage = True
                self.close()
        elif self.connection != -2:
            print("Closed channels = {}".format(self.k2700.display_closed_channels()))
        self.status = 0
        if self.smu.ID == 'Fake':
            self.status = self.status + 1
        if self.k2700.ID == 'Fake':
            self.status = self.status + 2
        if self.afg1022.ID == 'Fake':
            self.status = self.status + 4
        if self.status == 0:
            self.instLabel.setText('All instruments connected.')
        elif self.status == 1:
            self.instLabel.setText('Sourcemeter not connected.')
        elif self.status == 2:
            self.instLabel.setText('Sourcemeter, function generator connected')
        elif self.status == 3:
            self.instLabel.setText('Sourcemeter not connected. Function generator connected')
        elif self.status == 4:
            self.instLabel.setText('Sourcemeter, multiplexer connected.')
        elif self.status == 5:
            self.instLabel.setText('Sourcemeter not connected. Multiplexer connected')
        elif self.status == 6:
            self.instLabel.setText(f'Sourcemeter connected ({self.smu.name}).')
        elif self.status == 7:
            self.instLabel.setText('No instruments connected.')
        self.inst_button.setEnabled(True)
        self.dir_Button.setEnabled(True)
        self.filename.setEnabled(True)
        self.iv_button.setEnabled(True)
        self.rv_button.setEnabled(True)
        self.switch_button.setEnabled(True)
        self.endurance_button.setEnabled(True)
        self.retention_button.setEnabled(True)
        self.forming_button.setEnabled(True)
    
    def initialize_apps(self):
        self.iv = app_IVLoop(self, self.smu, self.k2700, self.IVfilename, self.connection, self.currentSample)
        self.iv.setWindowModality(QtCore.Qt.ApplicationModal)
        self.rv = app_RVLoop(self, self.smu, self.k2700, self.afg1022, self.RVfilename, self.connection, self.currentSample)
        self.rv.setWindowModality(QtCore.Qt.ApplicationModal)
        self.st = app_Switch(self, self.smu, self.k2700, self.afg1022, self.Switchfilename, self.connection, self.currentSample)
        self.st.setWindowModality(QtCore.Qt.ApplicationModal)
        self.ft = app_Fatigue(self, self.smu, self.k2700, self.afg1022, self.Fatiguefilename, self.connection, self.currentSample)
        self.ft.setWindowModality(QtCore.Qt.ApplicationModal)
        self.rt = app_Retention(self, self.smu, self.k2700, self.afg1022, self.Retentionfilename, self.connection, self.currentSample)
        self.rt.setWindowModality(QtCore.Qt.ApplicationModal)
        self.fr = app_Forming(self, self.smu, self.k2700, self.Formingfilename, self.connection, self.currentSample)
        self.fr.setWindowModality(QtCore.Qt.ApplicationModal)
        self.load_parameters()
    
    def openDir(self):
        """
        Open the dialog for selecting directory.

        Returns
        -------
        None.

        """
        options = QtWidgets.QFileDialog()
        options.setFileMode(QtWidgets.QFileDialog.Directory)
        options.setDirectory(os.getcwd())
        dirName = options.getExistingDirectory()
        if dirName:
            if self.currPath != dirName:
                self.save_parameters()
                self.currPath = dirName
                self.load_parameters()

    def set_two_wire_config(self):
        try:
            self.smu.set_wire_configuration(2)
            self.configLabel.setText("2-wire sense configuration")
            QMessageBox.warning(self,"Ensure proper wiring","In two wire configuration, "
                                                            "connect positive terminal to Force-high (red), "
                                                            "and negative terminal to Force-low (black)",QMessageBox.Ok)
        except NotImplementedError:
            QMessageBox.critical(self,"Error in setting configuration",
                                 "There was an error in setting the configuration. "
                                 "Most likely the SMU is not connected.",QMessageBox.Ok)

    def set_four_wire_config(self):
        try:
            self.smu.set_wire_configuration(4)
            QMessageBox.warning(self,"Ensure proper wiring","In four wire configuration, "
                                                            "connect positive source terminal to Force-high (red), "
                                                            "positive sense terminal to Sense-high (red), "
                                                            "negative source terminal to Force-low (black),"
                                                            "and negative sense terminal to Sense-low (black)",QMessageBox.Ok)
            self.configLabel.setText("4-wire sense configuration")
        except NotImplementedError:
            QMessageBox.critical(self, "Error in setting configuration",
                                 "There was an error in setting the configuration. "
                                 "Most likely the SMU is not connected.", QMessageBox.Ok)

    def setFilename(self, initial=0):
        """
        Autogenerate the filenames for various operations.

            Generate only if changes to existing filename are made,
            except when initial not equal to 0

        Parameters
        ----------
        initial : int, optional
            Set initial = 1 to generate the default names.
            The default is 0.

        Returns
        -------
        None.

        """
        if self.filename.isModified() or initial:
            self.sampleID = get_valid_filename(self.filename.text())
            if self.sampleID.find('.') != -1:
                # rindex returns the last location of '.'
                index = self.sampleID.rindex('.')
                self.sampleID = self.sampleID[:index]
            self.filename.setText(self.sampleID)
            self.IVfilename = self.sampleID+'_IV'
            self.RVfilename = self.sampleID+'_RV'
            self.Switchfilename = self.sampleID+'_Switch'
            self.Fatiguefilename = self.sampleID+'_Fatigue'
            self.Retentionfilename = self.sampleID+'_Retention'
            self.Formingfilename = self.sampleID+'_Forming'

    def combine_comments(self):
        newtext = self.commentBox.toPlainText()
        self.iv_text = newtext + '\n' + self.iv.commentBox.toPlainText()
        self.rv_text = newtext + '\n' +self.rv.commentBox.toPlainText()
        self.switch_text = newtext + '\n' +self.st.commentBox.toPlainText()
        self.fatigue_text = newtext + '\n' +self.ft.commentBox.toPlainText()
        self.retention_text = newtext + '\n' +self.rt.commentBox.toPlainText()
        self.forming_text = newtext + '\n' +self.fr.commentBox.toPlainText()

    def open_ivloop(self):
        """
        Load the IV-Loop module.

        Returns
        -------
        None.

        """
        self.iv.filename = self.IVfilename
        self.iv.file_name.setText(self.iv.filename)
        #self.hide()
        self.iv.show()

    def open_rvloop(self):
        """
        Load the RV-Loop module.

        Returns
        -------
        None.

        """
        self.rv.filename = self.RVfilename
        self.rv.file_name.setText(self.rv.filename)
        #self.hide()
        #self.showMinimized()
        self.rv.show()

    def open_switchTest(self):
        """
        Load the Switching module.

        Returns
        -------
        None.

        """
        self.st.filename = self.Switchfilename
        self.st.file_name.setText(self.st.filename)
        #self.hide()
        #self.showMinimized()
        self.st.show()
    
    def open_fatigue(self):
        """
        Load the Fatigue testing module.

        Returns
        -------
        None.

        """
        self.ft.filename = self.Fatiguefilename
        self.ft.file_name.setText(self.ft.filename)
        #self.hide()
        #self.showMinimized()
        self.ft.show()
    
    def open_retention(self):
        """
        Load the Retention testing module.

        Returns
        -------
        None.

        """
        self.rt.filename = self.Retentionfilename
        self.rt.file_name.setText(self.rt.filename)
        #self.hide()
        #self.showMinimized()
        self.rt.show()
    
    def open_forming(self):
        """
        Load the Forming program module.

        Returns
        -------
        None.

        """
        self.fr.filename = self.Formingfilename
        self.fr.file_name.setText(self.fr.filename)
        #self.hide()
        #self.showMinimized()
        self.fr.show()
    
    def load_parameters(self):
        os.chdir(self.currPath)
        if os.path.isfile("parameter_file.prm"):
            with open("parameter_file.prm",'r') as f:
                self.filename.setText(f.readline().strip())
                self.setFilename(1)
                self.iv.parameters = [float(i) if '.' in i or 'e' in i else int(i) for i in f.readline().strip().split()]
                self.rv.parameters = [float(i) if '.' in i or 'e' in i else int(i) for i in f.readline().strip().split()]
                self.st.parameters = [float(i) if '.' in i or 'e' in i else int(i) for i in f.readline().strip().split()]
                self.ft.parameters = [float(i) if '.' in i or 'e' in i else int(i) for i in f.readline().strip().split()]
                self.rt.parameters = [float(i) if '.' in i or 'e' in i else int(i) for i in f.readline().strip().split()]
                self.fr.parameters = [float(i) if '.' in i or 'e' in i else int(i) for i in f.readline().strip().split()]
                comments = f.readlines()
                self.commentBox.setText("".join(comments))
                self.iv.load_parameters()
                self.rv.load_parameters()
                self.st.load_parameters()
                self.ft.load_parameters()
                self.rt.load_parameters()
                self.fr.load_parameters()
        else:
            cp = os.path.normpath(self.currPath)
            self.filename.setText(cp.split('\\')[-1])
            self.setFilename(1)

    def save_parameters(self):
        os.chdir(self.currPath)
        with open("parameter_file.prm",'w') as f:
            f.write(self.filename.text()+'\n')
            f.write(' '.join(str(item) for item in self.iv.parameters)+'\n')
            f.write(' '.join(str(item) for item in self.rv.parameters)+'\n')
            f.write(' '.join(str(item) for item in self.st.parameters)+'\n')
            f.write(' '.join(str(item) for item in self.ft.parameters)+'\n')
            f.write(' '.join(str(item) for item in self.rt.parameters)+'\n')
            f.write(' '.join(str(item) for item in self.fr.parameters)+'\n')
            f.write(self.commentBox.toPlainText())
                
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
        def perform_preCloseOperations():
            connect_sample_with_SMU(self.k2700, self.connection, self.currentSample)
            self.save_parameters()
            os.chdir(self.settingPath)
            with open('SettingFile.dnd', 'w') as f:
                f.write(self.currPath+'\n')
                f.write(self.sampleID)
            os.chdir(self.initialPath)
            try:
                if self.status == 0: # if all instruments are connected
                    with open('address.txt','w') as f:
                        lines = f.readlines()
                        lines = lines[1:]
                        keeplines = []
                        for line in lines:
                            if 'k2450' in line.lower() or 'b2902' in line.lower():
                                keeplines.append(line)
                    with open('address.txt','w') as f:
                        self.smuAddr = self.smu.address + ' ' + self.smu.name
                        if len(keeplines) in (1,2): # check if address of unconnected smu needs to be stored
                            if 'b2902' in self.smu.name.lower():
                                if 'b2902' in keeplines[0].lower():
                                    keeplines.pop(0)
                                elif 'b2902' in keeplines[1].lower():
                                    keeplines.pop(1)
                            elif 'k2450' in self.smu.name.lower():
                                if 'k2450' in keeplines[0].lower():
                                    keeplines.pop(0)
                                elif 'k2450' in keeplines[1].lower():
                                    keeplines.pop(1)
                        if len(keeplines) == 1:
                            self.smuAddr += '\n' + keeplines[0]
                        self.k2700Addr = self.k2700.address + ' ' + self.k2700.name
                        self.AFG1022Addr = self.afg1022.address + ' ' + self.afg1022.name
                        f.write(self.settingPath+'\n') # write path of SettingFile.dnd
                        f.write(self.smuAddr + '\n') # write address of active smu
                        f.write(self.k2700Addr + '\n') # write address of K700
                        f.write(self.AFG1022Addr) # write address of AFG1022
            except AttributeError:
                pass
            self.smu.close()
            self.k2700.write("DISPlay:ENABle ON")
            self.k2700.close()
            self.afg1022.close()
            
        reply = QMessageBox.Yes
        if self.abortMessage == False:
            quit_msg = "Are you sure you want to exit?"
            reply = QMessageBox.question(self, 'Confirm Exit',quit_msg, QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.No:
                event.ignore()
            else:
                perform_preCloseOperations()
                event.accept()
        else:
            event.accept()
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    screen_resolution = app.desktop().screenGeometry()
    width, height = screen_resolution.width(), screen_resolution.height()
    main = MainWindow()
    main.show()
    app.exec_()
    app.quit()
