from PyQt6 import QtWidgets
from components.titleBarUi import Ui_tbWidget

class TitleBar(QtWidgets.QWidget, Ui_tbWidget):
    def __init__(self, parent = None):
        super(TitleBar, self).__init__(parent = parent)
        self.setupUi(self)
        self.parent = parent

    def insertTab(self, widget):
        self.horizontalLayout.addWidget(widget)
