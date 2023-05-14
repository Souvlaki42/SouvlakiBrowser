from PyQt5.QtWidgets import QApplication
from modules.app import MainWindow
from PyQt5.QtGui import QIcon
import sys, ctypes

if __name__ == "__main__":
	app = QApplication(sys.argv)

	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("souvlaki.browser.main")

	app.setApplicationName("Souvlaki Browser")
	app.setWindowIcon(QIcon("assets/images/logo.png"))

	main = MainWindow()
	main.show()
	app.exec_()
