from PyQt5 import QtCore, QtGui, QtWidgets
from modules.config import jsonParser

class Settings(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Window.setWindowIcon(icon)
        self.hometext = QtWidgets.QLineEdit(Window)
        self.hometext.setGeometry(QtCore.QRect(110, 30, 181, 20))
        self.hometext.setObjectName("hometext")
        self.hometext.setText(jsonParser.read_key("homepage"))
        self.homelabel = QtWidgets.QLabel(Window)
        self.homelabel.setGeometry(QtCore.QRect(30, 30, 61, 16))
        self.homelabel.setTextFormat(QtCore.Qt.PlainText)
        self.homelabel.setObjectName("homelabel")
        self.darklabel = QtWidgets.QLabel(Window)
        self.darklabel.setGeometry(QtCore.QRect(30, 80, 61, 16))
        self.darklabel.setTextFormat(QtCore.Qt.PlainText)
        self.darklabel.setObjectName("darklabel")
        self.darkcheck = QtWidgets.QCheckBox(Window)
        self.darkcheck.setGeometry(QtCore.QRect(120, 80, 70, 17))
        self.darkcheck.setText("")
        self.darkcheck.setCheckable(True)
        self.darkcheck.setChecked(jsonParser.read_key("darkmode"))
        self.darkcheck.setObjectName("darkcheck")
        self.linkpreviewlabel = QtWidgets.QLabel(Window)
        self.linkpreviewlabel.setGeometry(QtCore.QRect(30, 130, 61, 16))
        self.linkpreviewlabel.setTextFormat(QtCore.Qt.PlainText)
        self.linkpreviewlabel.setObjectName("linkpreviewlabel")
        self.linkpreviewcheck = QtWidgets.QCheckBox(Window)
        self.linkpreviewcheck.setGeometry(QtCore.QRect(120, 130, 70, 17))
        self.linkpreviewcheck.setText("")
        self.linkpreviewcheck.setCheckable(True)
        self.linkpreviewcheck.setChecked(jsonParser.read_key("linkpreview"))
        self.linkpreviewcheck.setObjectName("linkpreviewcheck")

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Settings"))
        self.homelabel.setText(_translate("Window", "Homepage"))
        self.darklabel.setText(_translate("Window", "Dark Mode"))
        self.linkpreviewlabel.setText(_translate("Window", "Link Preview"))