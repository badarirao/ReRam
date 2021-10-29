"""
Module to initialize the main menu.

# TODO: In Switch program, option to just measure resistance without switching
# TODO: Program to initiate forming process
# TODO: Search for the correct instrument address, promopt error if not found
# TODO: replace pymeasure with pyvisa implementation
# TODO: Ensure will work on other machines
"""

import sys
import os
from re import sub
from PyQt5 import QtWidgets, QtCore
from pymeasure.instruments.keithley import Keithley2450
from Memory import Ui_Memory
from IVloop import app_IVLoop
from RVloop import app_RVLoop
from Switch import app_Switch
from utilities import checkInstrument


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
        self.initialPath = os.getcwd()
        #with open('address.txt') as f:
        #    self.settingPath = f.readline()# store path of SettingFile.dnd here
        #    k2450Addr = f.readline()
        k2450Addr = "USB0::0x05E6::0x2450::04488850::INSTR"
        self.k2450 = checkInstrument(k2450Addr,test=True)
        self.k2450.reset()
        #Default file storage location is set to desktop
        self.settingPath = self.initialPath
        self.defaultPath = os.path.join(os.path.expandvars("%userprofile%"), "Desktop")
        if not os.path.exists(self.defaultPath):
            self.defaultPath = self.initialPath 
        #if not os.path.exists(self.settingPath):
        #    self.settingPath = self.initialPath
        self.setupUi(self)
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
        os.chdir(self.settingPath)
        # SettingFile contains last used filename, which is loaded initially
        try:
            with open('SettingFile.dnd', 'r') as f:
                self.currPath = f.readline().strip('\n\r')
                self.sampleID = get_valid_filename(f.readline().strip('\n\r'))
                if os.path.exists(self.currPath):
                    os.chdir(self.currPath)
                else:  # if SettingFile does not exist, set default name
                    self.currPath = self.defaultPath
                    os.chdir(self.defaultPath)
                if self.sampleID == '' or self.sampleID.isspace():
                    self.sampleID = "Sample"
                self.filename.setText(self.sampleID)
        except FileNotFoundError:
            os.chdir(self.defaultPath)
        self.setFilename(1)  # 1 indicates initial setting of filename
        self.iv = app_IVLoop(self, self.k2450, self.IVfilename)
        self.iv.setWindowModality(QtCore.Qt.ApplicationModal)
        self.rv = app_RVLoop(self, self.k2450, self.RVfilename)
        self.rv.setWindowModality(QtCore.Qt.ApplicationModal)
        self.st = app_Switch(self, self.k2450, self.Switchfilename)
        self.st.setWindowModality(QtCore.Qt.ApplicationModal)

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
            f.write(self.sampleID+'\n')
        os.chdir(self.initialPath)
        with open('address.txt','w') as f:
            f.write(self.settingPath)
            if self.k2450.address:
                f.write('\n'+self.k2450.address)
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
