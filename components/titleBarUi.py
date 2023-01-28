######################################################
##  SihinaCode > Search YouTube for more tutorials  ##
######################################################
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'titleBarUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tbWidget(object):
    def setupUi(self, tbWidget):
        tbWidget.setObjectName("tbWidget")
        tbWidget.resize(600, 40)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tbWidget.sizePolicy().hasHeightForWidth())
        tbWidget.setSizePolicy(sizePolicy)
        tbWidget.setMinimumSize(QtCore.QSize(0, 40))
        tbWidget.setMaximumSize(QtCore.QSize(16777215, 40))
        self.verticalLayout = QtWidgets.QVBoxLayout(tbWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tbWidget_2 = QtWidgets.QWidget(tbWidget)
        self.tbWidget_2.setMinimumSize(QtCore.QSize(0, 40))
        self.tbWidget_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.tbWidget_2.setStyleSheet("QWidget#tbWidget_2{\n"
"    background-color:rgb(12, 11, 16);\n"
"}")
        self.tbWidget_2.setObjectName("tbWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tbWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tbLabel_7 = MovableLabel(self.tbWidget_2)
        self.tbLabel_7.setMinimumSize(QtCore.QSize(25, 40))
        self.tbLabel_7.setMaximumSize(QtCore.QSize(25, 40))
        self.tbLabel_7.setText("")
        self.tbLabel_7.setObjectName("tbLabel_7")
        self.horizontalLayout_2.addWidget(self.tbLabel_7)
        self.tbWidget_5 = QtWidgets.QWidget(self.tbWidget_2)
        self.tbWidget_5.setMinimumSize(QtCore.QSize(0, 40))
        self.tbWidget_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.tbWidget_5.setObjectName("tbWidget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tbWidget_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tbLabel_6 = MovableLabel(self.tbWidget_5)
        self.tbLabel_6.setMinimumSize(QtCore.QSize(0, 5))
        self.tbLabel_6.setMaximumSize(QtCore.QSize(16777215, 5))
        self.tbLabel_6.setText("")
        self.tbLabel_6.setObjectName("tbLabel_6")
        self.verticalLayout_3.addWidget(self.tbLabel_6)
        self.tbWidget_6 = QtWidgets.QWidget(self.tbWidget_5)
        self.tbWidget_6.setObjectName("tbWidget_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tbWidget_6)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3.addWidget(self.tbWidget_6)
        self.horizontalLayout_2.addWidget(self.tbWidget_5)
        self.tbLabel_5 = MovableLabel(self.tbWidget_2)
        self.tbLabel_5.setMinimumSize(QtCore.QSize(15, 40))
        self.tbLabel_5.setMaximumSize(QtCore.QSize(15, 40))
        self.tbLabel_5.setText("")
        self.tbLabel_5.setObjectName("tbLabel_5")
        self.horizontalLayout_2.addWidget(self.tbLabel_5)
        self.tbWidget_4 = QtWidgets.QWidget(self.tbWidget_2)
        self.tbWidget_4.setMinimumSize(QtCore.QSize(30, 40))
        self.tbWidget_4.setMaximumSize(QtCore.QSize(30, 40))
        self.tbWidget_4.setStyleSheet("QPushButton{\n"
"    background-color:rgba(0, 0, 0, 0);\n"
"    color:rgb(255, 255, 255);\n"
"    font-size:17px;\n"
"    font-family:dripicons-v2;\n"
"    padding-top:3px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(144, 144, 144, 30);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.tbWidget_4.setObjectName("tbWidget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tbWidget_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tbLabel_3 = MovableLabel(self.tbWidget_4)
        self.tbLabel_3.setMinimumSize(QtCore.QSize(0, 7))
        self.tbLabel_3.setMaximumSize(QtCore.QSize(16777215, 7))
        self.tbLabel_3.setText("")
        self.tbLabel_3.setObjectName("tbLabel_3")
        self.verticalLayout_2.addWidget(self.tbLabel_3)
        self.tbPushButton_4 = QtWidgets.QPushButton(self.tbWidget_4)
        self.tbPushButton_4.setMinimumSize(QtCore.QSize(30, 30))
        self.tbPushButton_4.setMaximumSize(QtCore.QSize(30, 30))
        self.tbPushButton_4.setObjectName("tbPushButton_4")
        self.verticalLayout_2.addWidget(self.tbPushButton_4)
        self.tbLabel_4 = MovableLabel(self.tbWidget_4)
        self.tbLabel_4.setMinimumSize(QtCore.QSize(0, 3))
        self.tbLabel_4.setMaximumSize(QtCore.QSize(16777215, 3))
        self.tbLabel_4.setText("")
        self.tbLabel_4.setObjectName("tbLabel_4")
        self.verticalLayout_2.addWidget(self.tbLabel_4)
        self.horizontalLayout_2.addWidget(self.tbWidget_4)
        self.tbLabel_2 = MovableLabel(self.tbWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbLabel_2.sizePolicy().hasHeightForWidth())
        self.tbLabel_2.setSizePolicy(sizePolicy)
        self.tbLabel_2.setMinimumSize(QtCore.QSize(50, 40))
        self.tbLabel_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.tbLabel_2.setText("")
        self.tbLabel_2.setObjectName("tbLabel_2")
        self.horizontalLayout_2.addWidget(self.tbLabel_2)
        self.tbWidget_3 = QtWidgets.QWidget(self.tbWidget_2)
        self.tbWidget_3.setMinimumSize(QtCore.QSize(90, 40))
        self.tbWidget_3.setMaximumSize(QtCore.QSize(90, 40))
        self.tbWidget_3.setStyleSheet("QPushButton{\n"
"    background-color:rgba(0, 0, 0, 0);\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius:1px;\n"
"    font-size:18px;\n"
"    font-family:dripicons-v2;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(49, 48, 53);\n"
"}\n"
"QPushButton#tbPushButton_3:hover{\n"
"    background-color:rgb(232, 17, 35);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.tbWidget_3.setObjectName("tbWidget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.tbWidget_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.tbPushButton_3 = QtWidgets.QPushButton(self.tbWidget_3)
        self.tbPushButton_3.setMinimumSize(QtCore.QSize(30, 30))
        self.tbPushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        self.tbPushButton_3.setObjectName("tbPushButton_3")
        self.gridLayout.addWidget(self.tbPushButton_3, 0, 2, 1, 1)
        self.tbPushButton = QtWidgets.QPushButton(self.tbWidget_3)
        self.tbPushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.tbPushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.tbPushButton.setObjectName("tbPushButton")
        self.gridLayout.addWidget(self.tbPushButton, 0, 0, 1, 1)
        self.tbPushButton_2 = QtWidgets.QPushButton(self.tbWidget_3)
        self.tbPushButton_2.setMinimumSize(QtCore.QSize(30, 30))
        self.tbPushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        self.tbPushButton_2.setStyleSheet("font-size:13px;")
        self.tbPushButton_2.setCheckable(True)
        self.tbPushButton_2.setObjectName("tbPushButton_2")
        self.gridLayout.addWidget(self.tbPushButton_2, 0, 1, 1, 1)
        self.tbLabel = MovableLabel(self.tbWidget_3)
        self.tbLabel.setMinimumSize(QtCore.QSize(0, 10))
        self.tbLabel.setMaximumSize(QtCore.QSize(16777215, 10))
        self.tbLabel.setText("")
        self.tbLabel.setObjectName("tbLabel")
        self.gridLayout.addWidget(self.tbLabel, 1, 0, 1, 3)
        self.horizontalLayout_2.addWidget(self.tbWidget_3)
        self.verticalLayout.addWidget(self.tbWidget_2)

        self.retranslateUi(tbWidget)
        QtCore.QMetaObject.connectSlotsByName(tbWidget)

    def retranslateUi(self, tbWidget):
        _translate = QtCore.QCoreApplication.translate
        tbWidget.setWindowTitle(_translate("tbWidget", "Form"))
        self.tbPushButton_4.setText(_translate("tbWidget", ""))
        self.tbPushButton_3.setText(_translate("tbWidget", "9"))
        self.tbPushButton.setText(_translate("tbWidget", ""))
        self.tbPushButton_2.setText(_translate("tbWidget", ""))
from components.movableLabel import MovableLabel
