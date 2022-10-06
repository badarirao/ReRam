from utilities import *
# TODO: add timestamp for each datapoint in the file

class Ui_IVLoop(QtWidgets.QWidget):
    """The pyqt5 gui class for IV loop measurement."""

    def __init__(self, parent=None):
        super(Ui_IVLoop, self).__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)

    def setupUi(self, IVLoop):
        IVLoop.setObjectName("IVLoop")
        IVLoop.resize(818, 617)
        IVLoop.setMinimumSize(QtCore.QSize(0, 0))
        self.gridLayout_2 = QtWidgets.QGridLayout(IVLoop)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(IVLoop)
        self.groupBox.setMinimumSize(QtCore.QSize(240, 260))
        self.groupBox.setMaximumSize(QtCore.QSize(242, 600))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.temp_check = QtWidgets.QCheckBox(self.groupBox)
        self.temp_check.setObjectName("temp_check")
        self.gridLayout.addWidget(self.temp_check, 14, 0, 1, 2)
        self.temperature = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.temperature.setEnabled(False)
        self.temperature.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.temperature.setMaximum(600.0)
        self.temperature.setProperty("value", 300.0)
        self.temperature.setObjectName("temperature")
        self.gridLayout.addWidget(self.temperature, 14, 2, 1, 1)
        self.scan_speed_label = QtWidgets.QLabel(self.groupBox)
        self.scan_speed_label.setObjectName("scan_speed_label")
        self.gridLayout.addWidget(self.scan_speed_label, 6, 0, 1, 2)
        self.ncycles_label = QtWidgets.QLabel(self.groupBox)
        self.ncycles_label.setObjectName("ncycles_label")
        self.gridLayout.addWidget(self.ncycles_label, 11, 0, 1, 2)
        self.Ilimit_label = QtWidgets.QLabel(self.groupBox)
        self.Ilimit_label.setObjectName("Ilimit_label")
        self.gridLayout.addWidget(self.Ilimit_label, 9, 0, 1, 2)
        self.ncycles_label_2 = QtWidgets.QLabel(self.groupBox)
        self.ncycles_label_2.setObjectName("ncycles_label_2")
        self.gridLayout.addWidget(self.ncycles_label_2, 10, 0, 1, 1)
        self.minV_label = QtWidgets.QLabel(self.groupBox)
        self.minV_label.setObjectName("minV_label")
        self.gridLayout.addWidget(self.minV_label, 3, 0, 1, 2)
        self.maxV_label = QtWidgets.QLabel(self.groupBox)
        self.maxV_label.setObjectName("maxV_label")
        self.gridLayout.addWidget(self.maxV_label, 4, 0, 1, 2)
        self.maxV = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.maxV.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.maxV.setDecimals(3)
        self.maxV.setMinimum(-9.0)
        self.maxV.setMaximum(10.0)
        self.maxV.setSingleStep(0.001)
        self.maxV.setProperty("value", 3.0)
        self.maxV.setObjectName("maxV")
        self.gridLayout.addWidget(self.maxV, 4, 2, 1, 1)
        self.minV = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.minV.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.minV.setDecimals(3)
        self.minV.setMinimum(-10.0)
        self.minV.setMaximum(9.0)
        self.minV.setSingleStep(0.001)
        self.minV.setProperty("value", -3.0)
        self.minV.setObjectName("minV")
        self.gridLayout.addWidget(self.minV, 3, 2, 1, 1)
        self.scan_speed = QtWidgets.QComboBox(self.groupBox)
        self.scan_speed.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.scan_speed.setObjectName("scan_speed")
        self.scan_speed.addItem("")
        self.scan_speed.addItem("")
        self.scan_speed.addItem("")
        self.scan_speed.addItem("")
        self.scan_speed.addItem("")
        self.gridLayout.addWidget(self.scan_speed, 6, 2, 1, 1)
        self.ncycles = QtWidgets.QSpinBox(self.groupBox)
        self.ncycles.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.ncycles.setMinimum(1)
        self.ncycles.setMaximum(500)
        self.ncycles.setProperty("value", 1)
        self.ncycles.setObjectName("ncycles")
        self.gridLayout.addWidget(self.ncycles, 11, 2, 1, 1)
        self.fname_label = QtWidgets.QLabel(self.groupBox)
        self.fname_label.setObjectName("fname_label")
        self.gridLayout.addWidget(self.fname_label, 1, 0, 1, 2)
        self.delay = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.delay.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.delay.setMaximum(10000.0)
        self.delay.setSingleStep(0.05)
        self.delay.setProperty("value", 1.0)
        self.delay.setObjectName("delay")
        self.gridLayout.addWidget(self.delay, 5, 2, 1, 1)
        self.Ilimit = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.Ilimit.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.Ilimit.setDecimals(3)
        self.Ilimit.setMaximum(1.0)
        self.Ilimit.setSingleStep(0.001)
        self.Ilimit.setProperty("value", 0.5)
        self.Ilimit.setObjectName("Ilimit")
        self.gridLayout.addWidget(self.Ilimit, 9, 2, 1, 1)
        self.setting_label = QtWidgets.QLabel(self.groupBox)
        self.setting_label.setMinimumSize(QtCore.QSize(0, 24))
        self.setting_label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.setting_label.setObjectName("setting_label")
        self.gridLayout.addWidget(self.setting_label, 0, 0, 1, 3)
        self.delay_label = QtWidgets.QLabel(self.groupBox)
        self.delay_label.setObjectName("delay_label")
        self.gridLayout.addWidget(self.delay_label, 5, 0, 1, 1)
        self.file_name = QtWidgets.QLineEdit(self.groupBox)
        self.file_name.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.file_name.setObjectName("file_name")
        self.gridLayout.addWidget(self.file_name, 1, 2, 1, 1)
        self.nPointSet = QtWidgets.QSpinBox(self.groupBox)
        self.nPointSet.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.nPointSet.setMinimum(2)
        self.nPointSet.setMaximum(1000)
        self.nPointSet.setProperty("value", 50)
        self.nPointSet.setObjectName("nPointSet")
        self.gridLayout.addWidget(self.nPointSet, 10, 2, 1, 1)
        self.scan_direction_label = QtWidgets.QLabel(self.groupBox)
        self.scan_direction_label.setObjectName("scan_direction_label")
        self.gridLayout.addWidget(self.scan_direction_label, 7, 0, 1, 1)
        self.scan_direction = QtWidgets.QComboBox(self.groupBox)
        self.scan_direction.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.scan_direction.setObjectName("scan_direction")
        self.scan_direction.addItem("")
        self.scan_direction.addItem("")
        self.gridLayout.addWidget(self.scan_direction, 7, 2, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(IVLoop)
        self.widget.setMinimumSize(QtCore.QSize(240, 200))
        self.widget.setMaximumSize(QtCore.QSize(242, 10000))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comment_checkBox = QtWidgets.QCheckBox(self.widget)
        self.comment_checkBox.setObjectName("comment_checkBox")
        self.verticalLayout.addWidget(self.comment_checkBox)
        self.commentBox = QtWidgets.QTextEdit(self.widget)
        self.commentBox.setEnabled(False)
        self.commentBox.setMaximumSize(QtCore.QSize(242, 16777215))
        self.commentBox.setObjectName("commentBox")
        self.verticalLayout.addWidget(self.commentBox)
        self.start_Button = QtWidgets.QPushButton(self.widget)
        self.start_Button.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.start_Button.setObjectName("start_Button")
        self.verticalLayout.addWidget(self.start_Button)
        self.stop_Button = QtWidgets.QPushButton(self.widget)
        self.stop_Button.setStyleSheet("font: 75 14pt \"Times New Roman\";")
        self.stop_Button.setObjectName("stop_Button")
        self.verticalLayout.addWidget(self.stop_Button)
        self.statusbar = QtWidgets.QLineEdit(self.widget)
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
        self.statusbar.setStyleSheet("font: 11pt \"Times New Roman\";")
        self.statusbar.setText("")
        self.statusbar.setReadOnly(True)
        self.statusbar.setObjectName("statusbar")
        self.verticalLayout.addWidget(self.statusbar)
        self.gridLayout_2.addWidget(self.widget, 2, 0, 1, 1)
        self.graphWidget = PlotWidget(IVLoop, viewBox=ViewBox(border=mkPen(color='k', width=2)))
        self.graphWidget.setBackground((255, 182, 193, 25))
        self.graphWidget.setMinimumSize(QtCore.QSize(411, 379))
        self.graphWidget.setObjectName("graphWidget")
        self.gridLayout_2.addWidget(self.graphWidget, 0, 1, 3, 1)

        self.retranslateUi(IVLoop)
        self.scan_speed.setCurrentIndex(3)
        self.scan_direction.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(IVLoop)
        IVLoop.setTabOrder(self.file_name, self.minV)
        IVLoop.setTabOrder(self.minV, self.maxV)
        IVLoop.setTabOrder(self.maxV, self.delay)
        IVLoop.setTabOrder(self.delay, self.scan_speed)
        IVLoop.setTabOrder(self.scan_speed, self.Ilimit)
        IVLoop.setTabOrder(self.Ilimit, self.nPointSet)
        IVLoop.setTabOrder(self.nPointSet, self.ncycles)
        IVLoop.setTabOrder(self.ncycles, self.temp_check)
        IVLoop.setTabOrder(self.temp_check, self.temperature)
        IVLoop.setTabOrder(self.temperature, self.comment_checkBox)
        IVLoop.setTabOrder(self.comment_checkBox, self.commentBox)
        IVLoop.setTabOrder(self.commentBox, self.start_Button)
        IVLoop.setTabOrder(self.start_Button, self.stop_Button)
        IVLoop.setTabOrder(self.stop_Button, self.statusbar)

    def retranslateUi(self, IVLoop):
        _translate = QtCore.QCoreApplication.translate
        IVLoop.setWindowTitle(_translate("IVLoop", "IV Loop"))
        self.temp_check.setToolTip(_translate("IVLoop",
                                              "<html><head/><body><p>Use temperature only if temperature controller is attached</p></body></html>"))
        self.temp_check.setText(_translate("IVLoop", "Temperature (K)"))
        self.temperature.setToolTip(_translate("IVLoop",
                                               "<html><head/><body><p>Temperature range will depend on the type of heater</p></body></html>"))
        self.scan_speed_label.setText(_translate("IVLoop",
                                                 "<html><head/><body><p><span style=\" font-size:10pt;\">Scan Speed</span></p></body></html>"))
        self.ncycles_label.setText(_translate("IVLoop",
                                              "<html><head/><body><p><span style=\" font-size:10pt;\">Number of Cycles</span></p></body></html>"))
        self.Ilimit_label.setText(_translate("IVLoop",
                                             "<html><head/><body><p><span style=\" font-size:10pt;\">Current Limit (mA)</span></p></body></html>"))
        self.ncycles_label_2.setText(_translate("IVLoop",
                                                "<html><head/><body><p><span style=\" font-size:10pt;\">Number of Points</span></p></body></html>"))
        self.minV_label.setText(_translate("IVLoop",
                                           "<html><head/><body><p><span style=\" font-size:10pt;\">Minimum Voltage (V)</span></p></body></html>"))
        self.maxV_label.setText(_translate("IVLoop",
                                           "<html><head/><body><p><span style=\" font-size:10pt;\">Maximum Voltage (V)</span></p></body></html>"))
        self.maxV.setToolTip(_translate("IVLoop", "<html><head/><body><p>Max 10 V</p></body></html>"))
        self.minV.setToolTip(_translate("IVLoop", "<html><head/><body><p>Max -10 V</p></body></html>"))
        self.scan_speed.setItemText(0, _translate("IVLoop", "Very Slow"))
        self.scan_speed.setItemText(1, _translate("IVLoop", "Slow"))
        self.scan_speed.setItemText(2, _translate("IVLoop", "Normal"))
        self.scan_speed.setItemText(3, _translate("IVLoop", "Fast"))
        self.scan_speed.setItemText(4, _translate("IVLoop", "Very Fast"))
        self.ncycles.setToolTip(
            _translate("IVLoop", "<html><head/><body><p>Number of cycles to be executed</p></body></html>"))
        self.fname_label.setText(_translate("IVLoop",
                                            "<html><head/><body><p><span style=\" font-size:10pt;\">File Name</span></p></body></html>"))
        self.Ilimit.setToolTip(_translate("IVLoop",
                                          "<html><head/><body><p>The compliance current, which protects the sample from full breakdown</p></body></html>"))
        self.setting_label.setText(_translate("IVLoop",
                                              "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Parameters</span></p></body></html>"))
        self.delay_label.setText(_translate("IVLoop",
                                            "<html><head/><body><p><span style=\" font-size:10pt;\">Delay per point (ms)</span></p></body></html>"))
        self.file_name.setText(_translate("IVLoop", "Sample_IV"))
        self.nPointSet.setToolTip(
            _translate("IVLoop", "<html><head/><body><p>Number of cycles to be executed</p></body></html>"))
        self.scan_direction_label.setText(_translate("IVLoop",
                                                     "<html><head/><body><p><span style=\" font-size:10pt;\">Scan Direction</span></p></body></html>"))
        self.scan_direction.setItemText(0, _translate("IVLoop", "Positive"))
        self.scan_direction.setItemText(1, _translate("IVLoop", "Negative"))
        self.comment_checkBox.setText(_translate("IVLoop", "Add Comments"))
        self.start_Button.setToolTip(
            _translate("IVLoop", "<html><head/><body><p>Click to start the experiment</p></body></html>"))
        self.start_Button.setText(_translate("IVLoop", "START"))
        self.stop_Button.setToolTip(
            _translate("IVLoop", "<html><head/><body><p>Click to abort the experiment</p></body></html>"))
        self.stop_Button.setText(_translate("IVLoop", "STOP"))

class app_IVLoop(Ui_IVLoop):
    """The IV-Loop app module."""

    def __init__(self, parent=None, smu=None, k2700 = None, sName="Sample_IV.txt",connection=1):
        super(app_IVLoop, self).__init__(parent)
        self.parent = parent
        self.file_name.setReadOnly(True)
        self.smu = smu
        self.k2700 = k2700
        self.connection = connection
        self.smu.reset()
        self.stop_Button.setEnabled(False)
        self.stop_flag = False
        self.minV.setSingleStep(0.1)
        self.maxV.setSingleStep(0.1)
        self.minV.setMaximum(199)
        self.maxV.setMaximum(199)
        self.minV.setMinimum(-199)
        self.maxV.setMinimum(-199)
        self.Ilimit.setMaximum(500)
        self.Ilimit.setMinimum(0.001)
        self.Ilimit.setSingleStep(0.1)
        self.delay.setDecimals(3)
        self.start_Button.clicked.connect(self.start_ivloop)
        self.stop_Button.clicked.connect(self.stop_ivloop)
        self.start_Button.setShortcut('Ctrl+Return')
        self.stop_Button.setShortcut('Ctrl+q')
        self.initialize_plot()
        self.filename = sName
        self.file_name.setText(self.filename)
        self.measurement_status = "Idle"
        self.params = {
            "Vmin": -3,
            "Vmax": 3,
            "Delay": 50/1000,
            "Speed": 3,
            "Direction": 0,
            "ILimit": 1/1000,
            "npoints": 100,
            "ncycles": 1,
            "temperature": 300,
            "temp_check": 0,
            "comments": ""}
        self.parameters = list(self.params.values())[:-1]
        self.comment_checkBox.stateChanged.connect(self.updateCommentBox)
    
    def updateCommentBox(self):
        if self.comment_checkBox.isChecked():
            self.commentBox.setEnabled(True)
        else:
            self.commentBox.setEnabled(False)

    def load_parameters(self):
        try:
            self.minV.setValue(self.parameters[0])
            self.maxV.setValue(self.parameters[1])
            self.delay.setValue(self.parameters[2]*1000)
            self.scan_speed.setCurrentIndex(self.parameters[3])
            self.scan_direction.setCurrentIndex(self.parameters[4])
            self.Ilimit.setValue(self.parameters[5]*1000)
            self.nPointSet.setValue(self.parameters[6])
            self.ncycles.setValue(self.parameters[7])
            self.temperature.setValue(self.parameters[8])
            self.temp_check.setChecked(self.parameters[9])
        except Exception as e:
            print(f"Problem with loading IV parameters. {e}")
            print("Deleting parameter file from the folder may resolve the issue.")
    
    def update_params(self):
        """
        Update the measurement parameters.

        Returns
        -------
        None.

        """
        maincomment = self.parent.commentBox.toPlainText()
        wholeComment = maincomment + '\n' + self.commentBox.toPlainText()
        formattedComment = ""
        if self.smu.ID == "B2902B":
            if self.delay < 0.05:
                self.delay.setValue(0)
        for t in wholeComment.split('\n'):
            formattedComment += '## ' + t + '\n'
        self.params = {
            "Vmin": self.minV.value(),
            "Vmax": self.maxV.value(),
            "Delay": self.delay.value()/1000,
            "Speed": self.scan_speed.currentIndex(),
            "Direction": self.scan_direction.currentIndex(),
            "ILimit": self.Ilimit.value()/1000,
            "npoints": self.nPointSet.value(),
            "ncycles": self.ncycles.value(),
            "temperature": self.temperature.value(),
            "temp_check": int(self.temp_check.isChecked()),
            "comments": formattedComment}
        self.parameters = list(self.params.values())[:-1]
        if self.params["Vmax"] < self.params["Vmin"]:
            t = self.params["Vmax"]
            self.params["Vmax"] = self.params["Vmin"]
            self.params["Vmin"] = t
            self.minV.setValue(self.params["Vmin"])
            self.maxV.setValue(self.params["Vmax"])

    def plot_IVloop(self, Data):
        """
        Plot the ith IV loop into the graph.

        Parameters
        ----------
        data : list
            I values for every applied Voltage
        i : int
            Loop number

        Returns
        -------
        None.

        """
        data = Data[0]
        i = Data[1]
        self.currentCycle = i
        volts, currents = np.hsplit(data, 2)
        volts = volts.flatten()
        currents = abs(currents.flatten())
        pen1 = mkPen(intColor(3*i, values=3), width=2)
        if self.currentCycle == self.previousCycle:
            self.data_line.setData(self.points[0:len(volts)], currents)
        else:
            self.data_line = self.graphWidget.plot(self.points[0:len(volts)], currents, name="Cycle {0}".format(i), pen=pen1)
        self.previousCycle = i

    def start_ivloop(self):
        """
        Start the IV measurement based on given parameters.

        Returns
        -------
        None.

        """
        if self.smu.ID == 'K2450':
            if self.nPointSet.value() > 2500:
                self.nPointSet.setValue(2500)
        self.previousCycle = 0
        self.fullfilename = unique_filename(directory='.', prefix=self.filename, ext='dat', datetimeformat="")
        self.statusbar.setText("Measurement Running..")
        self.measurement_status = "Running"
        self.stop_flag = False
        self.graphWidget.clear()
        self.stop_Button.setEnabled(True)
        self.groupBox.setEnabled(False)
        self.start_Button.setEnabled(False)
        self.comment_checkBox.setEnabled(False)
        self.commentBox.setEnabled(False)
        self.update_params()
        self.startThread()

    def startThread(self):
        self.thread = QThread()
        self.worker = Worker(self.params, self.smu, self.k2700, self.fullfilename, self.connection)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.start_IV)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.data.connect(self.plot_IVloop)
        self.thread.finished.connect(self.finishAction)
        self.worker.sendPoints.connect(self.getPoints)
        self.thread.start()

    def getPoints(self,points):
        self.points = points[0]

    def finishAction(self):
        if not self.stop_flag:
            self.statusbar.setText("Measurement Finished.")
            self.measurement_status = "Idle"
            self.stop_flag = True
        self.groupBox.setEnabled(True)
        self.start_Button.setEnabled(True)
        self.comment_checkBox.setEnabled(True)
        self.commentBox.setEnabled(True)
        self.smu.source_voltage = 0
        self.stop_Button.setEnabled(False)
        #app_IVLoop.formatIV_Excel(self.fullfilename)
    
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
        self.graphWidget.setRange(QtCore.QRectF(self.minV.value(), 1e-12,
                                                self.maxV.value()-self.minV.value(),
                                                self.Ilimit.value()), padding=0)
        self.graphWidget.getPlotItem().setLogMode(None, True)
        self.graphWidget.addLegend()

    def stop_ivloop(self):
        """
        Trigger to stop the IV measurement.

        Returns
        -------
        None.

        """
        self.statusbar.setText("Measurement Aborted!")
        self.measurement_status = "Aborted"
        self.stop_flag = True
        self.worker.stopcall.emit()

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
        reply = QMessageBox.Yes
        if self.measurement_status == "Running":
            quit_msg = "Measurement is in Progress. Are you sure you want to stop and exit?"
            reply = QMessageBox.question(self, 'Message', quit_msg, QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.worker.stopcall.emit()
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
    sendPoints = pyqtSignal(list)
    
    def __init__(self, params, smu=None, k2700=None, fullfilename="sample.dat", connection = 1):
        super(Worker,self).__init__()
        self.stopCall = False
        self.params = params
        self.smu = smu
        self.k2700 = k2700
        self.connection = connection
        self.fullfilename = fullfilename
        self.stopcall.connect(self.stopcalled)
        self.smu.nplc = 1
        self.status = 1
        self.mtime = 0
        
    def initialize_SMU(self):
        """
        Initialize the SMU.

        Returns
        -------
        None.

        """
        if self.smu is None:
            self.smu = FakeAdapter()
        if self.k2700 is None:
            self.k2700 = FakeAdapter()
        
        # if afg is connected, remove and connect the source meter
        connect_sample_with_SMU(self.k2700,self.connection)
        self.smu.measure_current()
        self.smu.auto_range_sense()
        self.smu.set_wire_configuration(self.smu.wire_config) # two wire configuration
        if self.params["Speed"] == 0:
            nplc = 5
            self.speed = "Very Slow"
        elif self.params["Speed"] == 1:
            nplc = 2
            self.speed = "Slow"
        elif self.params["Speed"] == 2:
            nplc = 1
            self.speed = "Normal"
        elif self.params["Speed"] == 3:
            nplc = 0.1
            self.speed = "Fast"
        elif self.params["Speed"] == 4:
            nplc = 0.01
            self.speed = "Very Fast"
        self.smu.nplc = nplc
        self.smu.apply_voltage(compliance_current=self.params["ILimit"])
        # correct for zero only at the beginning
        self.smu.correct_zero_at_beginning_only()
        self.smu.set_read_back_on()

    def configure_sweep(self):
        """
        Configure the sweep conditions based on given parameters.

        Returns
        -------
        None.

        """
        self.npoints = self.params['npoints']
        if self.params["Vmax"] == self.params["Vmin"]:
            self.points = [self.params["Vmax"]]
            self.smu.set_voltage_points(self.points[0])
        elif self.params["Vmax"] >= 0 >= self.params["Vmin"]:
            nplus = int(self.params["Vmax"]/(self.params["Vmax"]-self.params["Vmin"])*self.npoints*0.5)
            nminus = int(abs(self.params["Vmin"])/(self.params["Vmax"]-self.params["Vmin"])*self.npoints*0.5)
            l1 = np.linspace(0, self.params["Vmax"], nplus, endpoint=False)
            l2 = np.linspace(self.params["Vmax"], self.params["Vmin"], nplus+nminus, endpoint=False)
            l3 = np.linspace(self.params["Vmin"], 0, nminus+1, endpoint=True)
            self.points = np.around(np.concatenate((l1, l2, l3)), 4)
            self.npoints = len(self.points)
            self.points[self.points == 0] = 0.0001
            if self.params["Direction"] == 1:
                self.points = np.flip(self.points)
            # split the points into 6 chunks of equal size
            chunk_size = ceil(self.npoints/100)
            self.chunks = np.array_split(self.points, chunk_size)
            # write the first chunk into the list
            self.smu.set_voltage_points(str(list(self.chunks[0]))[1:-1])
            # append the remaining chunks into the list
            if len(self.chunks) > 1:
                for i in self.chunks[1:]:
                    self.smu.append_voltage_points(str(list(i))[1:-1])
        else:
            l1 = np.linspace(self.params["Vmin"], self.params["Vmax"], int(
                self.npoints/2), endpoint=False)
            l2 = np.linspace(self.params["Vmax"], self.params["Vmin"], int(
                self.npoints/2)+1, endpoint=True)
            self.points = np.around(np.concatenate((l1, l2)), 4)
            if self.params["Direction"] == 1:
                self.points = np.flip(self.points)
            self.npoints = len(self.points)
            chunk_size = ceil(self.npoints/100)
            self.chunks = np.array_split(self.points, chunk_size)
            # write the first chunk into the list
            self.smu.set_voltage_points(str(list(self.chunks[0]))[1:-1])
            # append the remaining chunks into the list
            if len(self.chunks) > 1:
                for i in self.chunks[1:]:
                    self.smu.append_voltage_points(str(list(i))[1:-1])
        # set the sweep function with the above list
        self.smu.configure_sweep(self.params["Delay"])
        self.sendPoints.emit([self.points])
    
    def start_IV(self):
        self.mtime = datetime.now()
        self.initialize_SMU()
        self.configure_sweep()
        i = 0
        self.tempfileName = self.fullfilename[:-4] + "_tmp.dat"
        while i<self.params["ncycles"] and not self.stopCall:
            self.smu.clear_buffer(self.npoints)
            self.smu.start_buffer()  # start the measurement
            while self.stopCall == False:
                sleep(1)
                start_point = self.smu.get_start_point()
                if start_point == 0:
                    continue
                end_point = self.smu.get_end_point()
                data = self.smu.get_trace_data(start_point, end_point)
                data = np.reshape(np.array(data.split(','), dtype=float), (-1, 2))
                self.data.emit([data,i+1])
                state = self.smu.get_trigger_state()
                if state != 'RUNNING':
                    if state != 'IDLE':
                        self.status = 0
                    break
            with open(self.tempfileName, "a") as f:
                f.write("#Cycle {0}\n".format(i+1))
                data = np.insert(data, 0, self.points[0:len(data)], axis=1)
                np.savetxt(f, data, delimiter='\t')
                f.write("\n\n")
            i = i + 1
        if self.stopCall:
            self.smu.abort()
        self.smu.source_voltage = 0
        self.smu.disable_source()
        MessageBeep()
        self.mtime = str(datetime.now() - self.mtime)
        self.saveFile()
        self.finished.emit()
    
    def saveFile(self):
        with open(self.fullfilename,'w') as f:
            if self.params["Direction"] == 0:
                direction = "Positive first"
            else:
                direction = "Negative first"
            if self.smu.ID == 'K2450':
                f.write("## IV loop measurement using Keithley 2450 source measure unit.\n")
            elif self.smu.ID == 'B2902B':
                f.write("## IV loop measurement using Keysight B2902B source measure unit "
                        f"(channel-{self.smu.ch}).\n")
            f.write(f"## Date & Time: {datetime.now().strftime('%m/%d/%Y; %H:%M:%S')}, "
                    f"Total measurement time = {self.mtime}\n")
            f.write(f"## Min voltage = {self.params['Vmin']}V, Max voltage = {self.params['Vmax']}V\n")
            f.write(f"## Limiting current = {self.params['ILimit']*1000} mA, "
                    f"Delay per point = {self.params['Delay']}ms\n")
            f.write(f"## Scan speed = {self.speed}, Points per cycle = {self.params['npoints']}\n")
            f.write(f"## Requested number of IV loops = {self.params['ncycles']}, "
                    f"Scan Direction = {direction}\n")
            f.write(self.params["comments"])
            f.write("#Set Voltage(V)\tActual Voltage(V)\tCurrent(A)\n")
            if fileExists(self.tempfileName):
                with open(self.tempfileName, 'r') as tmp:
                    lines = tmp.readlines()
                    f.writelines(lines)
                os.remove(self.tempfileName)
    
    def stopcalled(self):
        self.stopCall = True

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IVLoop = QtWidgets.QWidget()
    smu, k2700, _ = checkInstrument(test = True)
    ui = app_IVLoop(IVLoop,smu,k2700)
    ui.show()
    app.exec_()
    app.quit()