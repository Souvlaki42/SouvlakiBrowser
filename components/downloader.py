from PyQt6 import QtCore, QtGui, QtWidgets

class DownloadManager(object):
    def setupUi(self, DownloadManager):
        DownloadManager.setObjectName("DownloadManager")
        DownloadManager.resize(400, 217)
        self.progressBar = QtWidgets.QProgressBar(parent=DownloadManager)
        self.progressBar.setGeometry(QtCore.QRect(90, 100, 231, 23))
        self.progressBar.setProperty("value", 25)
        self.progressBar.setObjectName("progressBar")
        self.filenameText = QtWidgets.QLabel(parent=DownloadManager)
        self.filenameText.setGeometry(QtCore.QRect(20, 50, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.filenameText.setFont(font)
        self.filenameText.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.filenameText.setScaledContents(False)
        self.filenameText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.filenameText.setWordWrap(True)
        self.filenameText.setObjectName("filenameText")
        self.folderBtn = QtWidgets.QPushButton(parent=DownloadManager)
        self.folderBtn.setEnabled(False)
        self.folderBtn.setGeometry(QtCore.QRect(160, 150, 75, 23))
        self.folderBtn.setObjectName("folderBtn")

        self.retranslateUi(DownloadManager)
        QtCore.QMetaObject.connectSlotsByName(DownloadManager)

    def retranslateUi(self, DownloadManager):
        _translate = QtCore.QCoreApplication.translate
        DownloadManager.setWindowTitle(_translate("DownloadManager", "Download Manager"))
        self.filenameText.setText(_translate("DownloadManager", "Filename"))
        self.folderBtn.setText(_translate("DownloadManager", "Open Folder"))
