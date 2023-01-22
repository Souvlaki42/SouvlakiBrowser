from PyQt5 import QtCore, QtWidgets

class DownloadManager(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 166)
        self.progress = QtWidgets.QProgressBar(Form)
        self.progress.setGeometry(QtCore.QRect(50, 80, 311, 23))
        self.progress.setProperty("value", 0)
        self.progress.setObjectName("progress")
        self.filename = QtWidgets.QLabel(Form)
        self.filename.setGeometry(QtCore.QRect(160, 50, 141, 20))
        self.filename.setObjectName("filename")
        self.openfolder = QtWidgets.QPushButton(Form)
        self.openfolder.setGeometry(QtCore.QRect(150, 120, 75, 23))
        self.openfolder.setObjectName("openfolder")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Download Manager"))
        self.filename.setText(_translate("Form", "TextLabel"))
        self.openfolder.setText(_translate("Form", "Open Folder"))
