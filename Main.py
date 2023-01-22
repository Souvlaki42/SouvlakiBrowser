from PyQt5.QtWidgets import QApplication
from modules.app import MainWindow
from modules.config import jsonParser
from PyQt5.QtGui import QIcon
import sys, ctypes, qdarkstyle

if __name__ == "__main__":
	app = QApplication(sys.argv)

	darkstyle = jsonParser.read_key("darkmode")

	if darkstyle:
		app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
	else:
		app.setStyleSheet("")

	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("souvlaki.browser.main")

	app.setApplicationName("Souvlaki Browser")
	app.setWindowIcon(QIcon("assets/images/logo.png"))

	main = MainWindow()
	main.show()
	app.exec_()
