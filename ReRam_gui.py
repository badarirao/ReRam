"""
Module to initialize the main menu.

Works on Python 3.8.5, Windows 10
Not tested for other Python versions or OS

# TODO: Program to initiate forming process
# TODO: Program to investigate switching speed
# TODO: Allow for both SCPI and TSP commands (currently only SCPI works)
# TODO: Save the last entered parameters of each program in file, which is reloaded at the starting of the program
# TODO: Scan the existing directory for saved files, and obtain the last used parameters from it, and put it in the program.
# TODO: Not able to cleanly exit if no instrument is connected and TESTING = False.
# TODO: correct the tab order of all the windows
# TODO: Resolve taskbar icon issue. Currently the taskbar icon is hidden when main window is hidden.
# TODO: Bug: minimizing the main window also minimized the child window, even if child.show() is given later.
# TODO: clear the graphs in all apps when directory of filename is changed.
# TODO: If instrument is not connected by mistake, then address file erases instrument address.
# TODO: While resuming an experiment, selecting a directory should automatically select that sample's filename.
# TODO: Correct tab order of all the programs.
# TODO: Put shortcut for reconnect instrument, change directory, start experiment
# TODO: some VisaError occurs when open_resources finds an instrument over lan, and tries to connect to it.
# TODO: Implement threading to plot data in a separate thread as a separate process.
"""
# 'KEITHLEY INSTRUMENTS,MODEL 2450,04488850,1.7.3c\n'
# 'KEITHLEY INSTRUMENTS INC.,MODEL 2700,1150720,B09  /A02  \n'
# 'TEKTRONIX,AFG1022,1643763,SCPI:99.0 FV:V1.2.3\n'
#  except VisaIOError:
    
import sys
import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer
from Memory import Ui_Memory
from IVloop import app_IVLoop
from RVloop import app_RVLoop
from Switch import app_Switch
from Fatigue import app_Fatigue
from Retention import app_Retention
from utilities import get_valid_filename, checkInstrument, connect_sample_with_SMU

TESTING = True  #if True, will use a Fakeadapter when no instrument connected

class MainWindow(QtWidgets.QMainWindow, Ui_Memory):
    """Class to initialize the main menu."""

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        """
        contents of address.txt:
            line 1: path where SettingFile.dnd is (or should be) stored
        """
        self.initial = 0
        self.checkPaths()
        self.setupUi(self)
        self.filename.setText(self.sampleID)
        self.dir_Button.clicked.connect(self.openDir)
        self.iv_button.clicked.connect(self.open_ivloop)
        self.rv_button.clicked.connect(self.open_rvloop)
        self.switch_button.clicked.connect(self.open_switchTest)
        self.inst_button.clicked.connect(self.check_instrument_connection)
        self.endurance_button.clicked.connect(self.open_fatigue)
        self.retention_button.clicked.connect(self.open_retention)
        #self.endurance_button.setEnabled(False)
        #self.retention_button.setEnabled(False)
        self.speed_button.setEnabled(False)
        self.aging_button.setEnabled(False)
        self.memristor_button.setEnabled(False)
        self.temperature_button.setEnabled(False)
        self.batch_button.setEnabled(False)
        self.forming_button.setEnabled(False)
        self.filename.editingFinished.connect(self.setFilename)
        self.setFilename(1)  # 1 indicates initial setting of filename
        QTimer.singleShot(10,self.initialize_apps)
        self.abort = False

    def initialize_apps(self):
        self.check_instrument_connection()
        self.k2450.reset()
        self.iv = app_IVLoop(self, self.k2450, self.k2700, self.IVfilename)
        self.iv.setWindowModality(QtCore.Qt.ApplicationModal)
        self.rv = app_RVLoop(self, self.k2450, self.k2700, self.afg1022, self.RVfilename)
        self.rv.setWindowModality(QtCore.Qt.ApplicationModal)
        self.st = app_Switch(self, self.k2450, self.k2700, self.afg1022, self.Switchfilename)
        self.st.setWindowModality(QtCore.Qt.ApplicationModal)
        self.ft = app_Fatigue(self, self.k2450, self.k2700, self.afg1022, self.Fatiguefilename)
        self.ft.setWindowModality(QtCore.Qt.ApplicationModal)
        self.rt = app_Retention(self, self.k2450, self.k2700, self.afg1022, self.Retentionfilename)
        self.rt.setWindowModality(QtCore.Qt.ApplicationModal)
    
    
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
        try:
            with open('address.txt') as f:
                self.settingPath = f.readline().strip('\n\r')# get path of SettingFile.dnd
                self.k2450Addr = f.readline().strip('\n\r').split()[0] # get address of K2450 if present
                self.k2700Addr = f.readline().strip('\n\r').split()[0] # get address of K700 if present
                self.AFG1022Addr = f.readline().strip('\n\r').split()[0] # get address of AFG1022 if present
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
                self.sampleID = get_valid_filename(f.readline().strip('\n\r'))
                if self.sampleID == '' or self.sampleID.isspace():
                    self.sampleID = "Sample"
                os.chdir(self.currPath)
        except FileNotFoundError: # if SettingFile does not exist, set default name
            self.currPath = self.defaultPath
            os.chdir(self.defaultPath)
            self.sampleID = "Sample"

    def connectInstrument(self):
        """
        Connect to K2450, K2700 and function generator.
        
        if TESTING is True, use FakeAdapter even when instrument not available.
        if TESTING is False, quit program when instrument not available.

        Returns
        -------
        Instrument objects

        """
        global TESTING
        a1 = self.k2450Addr
        a2 = self.k2700Addr
        a3 = self.AFG1022Addr
        self.k2450, self.k2700, self.afg1022 = checkInstrument(a1,a2,a3,test = TESTING)
        
    def check_instrument_connection(self):
        try:
            self.k2450.close()
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
        self.statusBar.showMessage('Establishing instrument connection... Please wait')
        self.connectInstrument()
        self.status = 0
        if self.k2450.ID == 'Fake':
            self.status = self.status + 1
        if self.k2700.ID == 'Fake':
            self.status = self.status + 2
        if self.afg1022.ID == 'Fake':
            self.status = self.status + 4
        if self.status == 0:
            self.statusBar.showMessage('All instruments connected.')
        elif self.status == 1:
            self.statusBar.showMessage('Sourcemeter not connected.')
        elif self.status == 2:
            self.statusBar.showMessage('Multiplexer not connected.')
        elif self.status == 3:
            self.statusBar.showMessage('Function generator not connected.')
        elif self.status == 4:
            self.statusBar.showMessage('Sourcemeter, Multiplexer not connected.')
        elif self.status == 5:
            self.statusBar.showMessage('Sourcemeter, Function generator not connected.')
        elif self.status == 6:
            self.statusBar.showMessage('Multiplexer, Function generator not connected.')
        elif self.status == 7:
            self.statusBar.showMessage('No instruments connected.')
        self.inst_button.setEnabled(True)
        self.dir_Button.setEnabled(True)
        self.filename.setEnabled(True)
        self.iv_button.setEnabled(True)
        self.rv_button.setEnabled(True)
        self.switch_button.setEnabled(True)
        self.endurance_button.setEnabled(True)
        self.retention_button.setEnabled(True)
    
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
            self.currPath = dirName
            os.chdir(self.currPath)

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
        self.ft.file_name.setText(self.st.filename)
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
        quit_msg = "Are you sure you want to exit?"
        reply = QMessageBox.question(self, 'Confirm Exit',quit_msg, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.No:
            event.ignore()
        else:
            connect_sample_with_SMU(self.k2700)
            with open("parameter_file.prm",'w') as f:
                f.write(' '.join(str(item) for item in self.iv.params)+'\n')
            os.chdir(self.settingPath)
            with open('SettingFile.dnd', 'w') as f:
                f.write(self.currPath+'\n')
                f.write(self.sampleID)
            os.chdir(self.initialPath)
            if self.status == 0:
                with open('address.txt','w') as f:
                    self.k2450Addr = self.k2450.address
                    self.k2700Addr = self.k2700.address
                    self.AFG1022Addr = self.afg1022.address
                    self.AFG1022Addr
                    f.write(self.settingPath+'\n') # write path of SettingFile.dnd
                    f.write(self.k2450Addr+' (Keithley 2450 Sourcemeter)'+'\n') # write address of K2450 if present
                    f.write(self.k2700Addr+' (Keithley 2700 Multiplexer)'+'\n') # write address of K700 if present
                    f.write(self.AFG1022Addr+' (Textronix 1022 Function Generator)') # write get address of AFG1022 if present
            self.k2450.close()
            self.k2700.write("DISPlay:ENABle ON")
            self.k2700.close()
            self.afg1022.close()
            event.accept()
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec_()
    app.quit()
