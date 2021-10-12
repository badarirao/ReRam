"""
Module to initialize the main menu.

Works on Python 3.8.5, Windows 10
Not tested for other Python versions or OS

# TODO: In Switch program, option to just measure resistance without switching
# TODO: Program to initiate forming process
# TODO: Search for the correct instrument address, promopt error if not found
# TODO: replace pymeasure with pyvisa implementation
# TODO: Get relevant machine address automatically (currently, must be specified in address.txt)
# TODO: Allow for both SCPI and TSP commands (currently only SCPI works)
# TODO: Implement endurance testing
# TODO: Restrict input parameter valid range correctly for each program
"""
# 'KEITHLEY INSTRUMENTS,MODEL 2450,04488850,1.7.3c\n'
# 'KEITHLEY INSTRUMENTS INC.,MODEL 2700,1150720,B09  /A02  \n'
# 'TEKTRONIX,AFG1022,1643763,SCPI:99.0 FV:V1.2.3\n'
#  except VisaIOError:
import sys
import os
from PyQt5 import QtWidgets, QtCore
from Memory import Ui_Memory
from IVloop import app_IVLoop
from RVloop import app_RVLoop
from Switch import app_Switch
from utilities import get_valid_filename, checkInstrument

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
        self.connectInstrument()
        self.k2450.reset()
        self.setupUi(self)
        self.filename.setText(self.sampleID)
        self.dir_Button.clicked.connect(self.openDir)
        self.iv_button.clicked.connect(self.open_ivloop)
        self.rv_button.clicked.connect(self.open_rvloop)
        self.switch_button.clicked.connect(self.open_switchTest)
        self.endurance_button.setEnabled(False)
        self.retention_button.setEnabled(False)
        self.speed_button.setEnabled(False)
        self.aging_button.setEnabled(False)
        self.memristor_button.setEnabled(False)
        self.temperature_button.setEnabled(False)
        self.batch_button.setEnabled(False)
        self.filename.editingFinished.connect(self.setFilename)
        self.setFilename(1)  # 1 indicates initial setting of filename
        self.iv = app_IVLoop(self, self.k2450, self.IVfilename)
        self.iv.setWindowModality(QtCore.Qt.ApplicationModal)
        self.rv = app_RVLoop(self, self.k2450, self.RVfilename)
        self.rv.setWindowModality(QtCore.Qt.ApplicationModal)
        self.st = app_Switch(self, self.k2450, self.Switchfilename)
        self.st.setWindowModality(QtCore.Qt.ApplicationModal)

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
                self.k2450Addr = f.readline().strip('\n\r') # get address of K2450 if present
                self.k2700Addr = f.readline().strip('\n\r') # get address of K700 if present
                self.AFG1022Addr = f.readline().strip('\n\r') # get address of AFG1022 if present
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
        os.chdir(self.settingPath)
        with open('SettingFile.dnd', 'w') as f:
            f.write(self.currPath+'\n')
            f.write(self.sampleID)
        os.chdir(self.initialPath)
        with open('address.txt','w') as f:
            self.k2450Addr = self.k2450.address
            self.k2700Addr = self.k2700.address
            self.AFG1022Addr = self.afg1022.address
            self.AFG1022Addr
            f.write(self.settingPath+'\n') # write path of SettingFile.dnd
            f.write(self.k2450Addr+'\n') # write address of K2450 if present
            f.write(self.k2700Addr+'\n') # write address of K700 if present
            f.write(self.AFG1022Addr) # write get address of AFG1022 if present
        event.accept()

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

    def open_ivloop(self):
        """
        Load the IV-Loop module.

        Returns
        -------
        None.

        """
        self.iv.filename = self.IVfilename
        self.iv.file_name.setText(self.iv.filename)
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
        self.st.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
