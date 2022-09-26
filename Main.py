from PyQt5.QtWidgets import QApplication
from modules.app import MainWindow
from config import jsonParser
from PyQt5.QtGui import QIcon
import qdarkstyle
import sys, ctypes

darkstyle = jsonParser.read_key("darkmode")

def main_func():
	
	app = QApplication(sys.argv)

	if darkstyle:
		app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
	else:
		app.setStyleSheet("")

	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("souvlaki.browser.main")

	app.setApplicationName("Souvlaki Browser")
	app.setWindowIcon(QIcon("assets/logo.png"))

	main = MainWindow()
	main.show()
	app.exec_()
	

if __name__ == "__main__":
	main_func()
