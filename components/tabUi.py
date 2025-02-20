# Form implementation generated from reading ui file '.\components\tabUi.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_tabWidget(object):
    def setupUi(self, tabWidget):
        tabWidget.setObjectName("tabWidget")
        tabWidget.resize(180, 35)
        tabWidget.setMinimumSize(QtCore.QSize(40, 35))
        tabWidget.setMaximumSize(QtCore.QSize(180, 35))
        self.horizontalLayout = QtWidgets.QHBoxLayout(tabWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget_2 = QtWidgets.QWidget(parent=tabWidget)
        self.tabWidget_2.setMinimumSize(QtCore.QSize(40, 35))
        self.tabWidget_2.setMaximumSize(QtCore.QSize(180, 35))
        self.tabWidget_2.setStyleSheet("QWidget{\n"
"    background-color:rgb(35, 34, 39);\n"
"    color:rgb(170, 170, 170);\n"
"    border-top-left-radius:5px;\n"
"    border-top-right-radius:5px;\n"
"    padding:2px;\n"
"}")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tabWidget_2)
        self.horizontalLayout_2.setContentsMargins(3, 0, 3, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabIcon = QtWidgets.QToolButton(parent=self.tabWidget_2)
        self.tabIcon.setText("")
        self.tabIcon.setObjectName("tabIcon")
        self.horizontalLayout_2.addWidget(self.tabIcon)
        self.tabLabel = QtWidgets.QLabel(parent=self.tabWidget_2)
        self.tabLabel.setMinimumSize(QtCore.QSize(10, 25))
        self.tabLabel.setMaximumSize(QtCore.QSize(150, 25))
        self.tabLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tabLabel.setObjectName("tabLabel")
        self.horizontalLayout_2.addWidget(self.tabLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.tabPushButton = QtWidgets.QPushButton(parent=self.tabWidget_2)
        self.tabPushButton.setMinimumSize(QtCore.QSize(25, 25))
        self.tabPushButton.setMaximumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tabPushButton.setFont(font)
        self.tabPushButton.setStyleSheet("QPushButton{\n"
"    background-color:rgba(0, 0, 0, 0);\n"
"    color:rgb(144, 144, 144);\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.tabPushButton.setObjectName("tabPushButton")
        self.horizontalLayout_2.addWidget(self.tabPushButton)
        self.horizontalLayout.addWidget(self.tabWidget_2)

        self.retranslateUi(tabWidget)
        QtCore.QMetaObject.connectSlotsByName(tabWidget)

    def retranslateUi(self, tabWidget):
        _translate = QtCore.QCoreApplication.translate
        tabWidget.setWindowTitle(_translate("tabWidget", "Form"))
        self.tabLabel.setText(_translate("tabWidget", "New Tab"))
        self.tabPushButton.setText(_translate("tabWidget", "x"))
