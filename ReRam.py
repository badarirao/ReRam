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
"""
# 'KEITHLEY INSTRUMENTS,MODEL 2450,04488850,1.7.3c\n'
# 'KEITHLEY INSTRUMENTS INC.,MODEL 2700,1150720,B09  /A02  \n'
# 'TEKTRONIX,AFG1022,1643763,SCPI:99.0 FV:V1.2.3\n'
#  except VisaIOError:
import sys
import os
from re import sub
from PyQt5 import QtWidgets, QtCore
from pyvisa import ResourceManager, VisaIOError
from pymeasure.instruments.keithley import Keithley2450
from pymeasure.instruments.keithley import Keithley2700
from afg1022 import AFG1022 
from Memory import Ui_Memory
from IVloop import app_IVLoop
from RVloop import app_RVLoop
from Switch import app_Switch
from utilities import FakeAdapter

TESTING = True  #if True, will use a Fakeadapter when no instrument connected

def get_valid_filename(s):
    """
    Check if given filename is valid, and correct it if its not.

    Parameters
    ----------
    s : string
        file-name

    Returns
    -------
    string
        Valid file-name

    """
    s = str(s).strip().replace(' ', '_')
    return sub(r'(?u)[^-\w.]', '', s)


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
        self.checkInstrument()
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
        self.settingPath = ""
        self.sampleID = ''
        if os.path.exists('address.txt'):
            with open('address.txt') as f:
                self.settingPath = f.readline().strip('\n\r')# get path of SettingFile.dnd
        else:
            with open('address.txt') as f:
                f.write(os.getcwd())
        self.initialPath = os.getcwd()
        # set defaultPath as desktop
        self.defaultPath = os.path.join(
            os.path.expandvars("%userprofile%"), "Desktop")
        if not os.path.exists(self.defaultPath):
            self.defaultPath = self.initialPath 
        if not os.path.exists(self.settingPath):
            self.settingPath = self.initialPath
            with open('address.txt','w') as f:
                f.write(self.settingPath)
        os.chdir(self.settingPath)
        # SettingFile contains last used filename, which is loaded initially
        try:
            with open('SettingFile.dnd', 'r') as f:
                self.currPath = f.readline().strip('\n\r')
                self.sampleID = get_valid_filename(f.readline().strip('\n\r'))
                if os.path.exists(self.currPath):
                    os.chdir(self.currPath)
                else: 
                    raise FileNotFoundError
                if self.sampleID == '' or self.sampleID.isspace():
                    self.sampleID = "Sample"
        except FileNotFoundError: # if SettingFile does not exist, set default name
            self.currPath = self.defaultPath
            os.chdir(self.defaultPath)
            self.sampleID = "Sample"

    def checkInstrument(self):
        global TESTING
        rm = ResourceManager()
        instList = rm.list_resources()
        self.k2450Addr = None
        self.k2700Addr = None
        self.AFG1022Addr = None
        for inst in instList:
            try:
                myInst = rm.open_resource(inst)
                instID = myInst.query('*IDN?').split(',')
                if 'KEITHLEY' in instID[0] and '2450' in instID[1]:
                    self.k2450Addr = inst
                    self.k2450 = Keithley2450(self.k2450Addr)
                elif 'KEITHLEY' in instID[0] and '2700' in instID[1]:
                    self.k2700Addr = inst
                    self.k2700 = Keithley2700(self.k2700Addr)
                elif 'TEKTRONIX' in instID[0] and 'AFG1022' in instID[1]:
                    self.AFG1022Addr = inst
                    self.afg = AFG1022(self.AFG1022Addr)
            except VisaIOError:
                pass
        # For debugging purpose, invoke a fake adapter
        if TESTING is True:
            if not self.k2450Addr:
                self.k2450 = FakeAdapter()
            if not self.k2700Addr:
                self.k2700 = FakeAdapter()
            if not self.AFG1022Addr:
                self.afg = FakeAdapter()
        elif not all((self.k2450Addr,self.k2700Addr,self.AFG1022Addr)):
            print("Instrument not connected! Check connections!")
            sys.exit()

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
