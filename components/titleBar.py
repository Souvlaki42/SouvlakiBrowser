from PyQt6 import QtWidgets
from components.titleBarUi import Ui_tbWidget
from components.movableLabel import MovableLabel

class TitleBar(QtWidgets.QWidget, Ui_tbWidget):
    def __init__(self, parent = None):
        super(TitleBar, self).__init__(parent = parent)
        self.setupUi(self)
        self.parent = parent
        MovableLabel.mainWindow = self.parent

        self.tbPushButton.clicked.connect(lambda: self.parent.showMinimized())
        self.tbPushButton_2.clicked.connect(lambda: self.winShowMaximized())
        self.tbPushButton_3.clicked.connect(lambda: self.parent.close())

    def winShowMaximized(self):
        if self.tbPushButton_2.isChecked():
            self.parent.showMaximized()
            self.tbPushButton_2.setText(";")
        else:
            self.parent.showNormal()
            self.tbPushButton_2.setText("")

    def insertTab(self, widget):
        self.horizontalLayout.addWidget(widget)
