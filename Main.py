from unicodedata import name
from PyQt5.QtWidgets import QApplication
from app import MainWindow
from PyQt5.QtGui import QIcon
import qdarkstyle
import sys

darkstyle = False

if __name__ == "__main__":
	app = QApplication(sys.argv)

	if darkstyle:
		app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
	else:
		app.setStyleSheet("")

	app.setApplicationName("Souvlaki Browser")
	app.setWindowIcon(QIcon("images/logo.png"))

	main = MainWindow()
	main.show()
	app.exec_()