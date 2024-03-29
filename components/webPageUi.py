# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'components/webPageUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wpWidget(object):
    def setupUi(self, wpWidget):
        wpWidget.setObjectName("wpWidget")
        wpWidget.resize(600, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wpWidget.sizePolicy().hasHeightForWidth())
        wpWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(wpWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.wpWidget_2 = QtWidgets.QWidget(wpWidget)
        self.wpWidget_2.setObjectName("wpWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.wpWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.wpWidget_3 = QtWidgets.QWidget(self.wpWidget_2)
        self.wpWidget_3.setMinimumSize(QtCore.QSize(0, 40))
        self.wpWidget_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.wpWidget_3.setStyleSheet("QWidget#wpWidget_3{\n"
"    background-color:rgb(35, 34, 39);\n"
"}")
        self.wpWidget_3.setObjectName("wpWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.wpWidget_3)
        self.horizontalLayout_2.setContentsMargins(-1, 0, 18, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.wpWidget_5 = QtWidgets.QWidget(self.wpWidget_3)
        self.wpWidget_5.setMinimumSize(QtCore.QSize(0, 40))
        self.wpWidget_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.wpWidget_5.setStyleSheet("QPushButton{\n"
"    background-color:rgba(0, 0, 0, 0);\n"
"    color:rgb(255, 255, 255);\n"
"    font-size:17px;\n"
"    font-family:dripicons-v2;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(144, 144, 144, 30);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.wpWidget_5.setObjectName("wpWidget_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.wpWidget_5)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.wpPushButton = QtWidgets.QPushButton(self.wpWidget_5)
        self.wpPushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.wpPushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.wpPushButton.setObjectName("wpPushButton")
        self.horizontalLayout.addWidget(self.wpPushButton)
        self.wpPushButton_2 = QtWidgets.QPushButton(self.wpWidget_5)
        self.wpPushButton_2.setMinimumSize(QtCore.QSize(30, 30))
        self.wpPushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        self.wpPushButton_2.setObjectName("wpPushButton_2")
        self.horizontalLayout.addWidget(self.wpPushButton_2)
        self.wpPushButton_3 = QtWidgets.QPushButton(self.wpWidget_5)
        self.wpPushButton_3.setMinimumSize(QtCore.QSize(30, 30))
        self.wpPushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        self.wpPushButton_3.setObjectName("wpPushButton_3")
        self.horizontalLayout.addWidget(self.wpPushButton_3)
        self.wpPushButton_4 = QtWidgets.QPushButton(self.wpWidget_5)
        self.wpPushButton_4.setMinimumSize(QtCore.QSize(30, 30))
        self.wpPushButton_4.setMaximumSize(QtCore.QSize(30, 30))
        self.wpPushButton_4.setObjectName("wpPushButton_4")
        self.horizontalLayout.addWidget(self.wpPushButton_4)
        self.horizontalLayout_2.addWidget(self.wpWidget_5)
        self.wpLineEdit = QtWidgets.QLineEdit(self.wpWidget_3)
        self.wpLineEdit.setMinimumSize(QtCore.QSize(300, 28))
        self.wpLineEdit.setMaximumSize(QtCore.QSize(16777215, 28))
        self.wpLineEdit.setStyleSheet("QLineEdit{\n"
"    background-color:rgb(27, 27, 27);\n"
"    border-radius:12px;\n"
"    color:rgb(240, 240, 240);\n"
"    padding-left:15px;\n"
"    border: 1px solid rgba(255, 255, 255, 50);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 1px solid rgba(99, 173, 229, 150);\n"
"}")
        self.wpLineEdit.setObjectName("wpLineEdit")
        self.horizontalLayout_2.addWidget(self.wpLineEdit)
        self.wpPushButton_5 = QtWidgets.QPushButton(self.wpWidget_3)
        self.wpPushButton_5.setMinimumSize(QtCore.QSize(30, 30))
        self.wpPushButton_5.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("dripicons-v2")
        self.wpPushButton_5.setFont(font)
        self.wpPushButton_5.setStyleSheet("QPushButton{\n"
"    background-color:rgba(0, 0, 0, 0);\n"
"    color:rgb(255, 255, 255);\n"
"    font-size:17px;\n"
"    font-family:dripicons-v2;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(144, 144, 144, 30);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.wpPushButton_5.setObjectName("wpPushButton_5")
        self.horizontalLayout_2.addWidget(self.wpPushButton_5)
        self.verticalLayout_2.addWidget(self.wpWidget_3)
        self.wpWidget_4 = QtWidgets.QWidget(self.wpWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wpWidget_4.sizePolicy().hasHeightForWidth())
        self.wpWidget_4.setSizePolicy(sizePolicy)
        self.wpWidget_4.setObjectName("wpWidget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.wpWidget_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2.addWidget(self.wpWidget_4)
        self.verticalLayout.addWidget(self.wpWidget_2)

        self.retranslateUi(wpWidget)
        QtCore.QMetaObject.connectSlotsByName(wpWidget)

    def retranslateUi(self, wpWidget):
        _translate = QtCore.QCoreApplication.translate
        wpWidget.setWindowTitle(_translate("wpWidget", "Form"))
        self.wpPushButton.setText(_translate("wpWidget", "l"))
        self.wpPushButton_2.setText(_translate("wpWidget", "m"))
        self.wpPushButton_3.setText(_translate("wpWidget", "Z"))
        self.wpPushButton_4.setText(_translate("wpWidget", ""))
        self.wpLineEdit.setPlaceholderText(_translate("wpWidget", "Type a URL"))
        self.wpPushButton_5.setText(_translate("wpWidget", "/"))
