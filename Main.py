from cProfile import label
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QTabWidget, QStatusBar, QToolBar, QAction, QShortcut, QLineEdit, QMessageBox, QApplication, QLabel
from PyQt5.QtGui import QKeySequence, QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
import sys
import os
os.system('cls' if os.name == 'nt' else 'clear')

class MainWindow(QMainWindow):

	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)

		self.tabs = QTabWidget()

		self.tabs.setDocumentMode(True)

		self.homepage = "https://google.com"

		self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)

		self.tabs.currentChanged.connect(self.current_tab_changed)

		self.tabs.setTabsClosable(True)

		self.tabs.tabCloseRequested.connect(self.close_current_tab)

		self.setCentralWidget(self.tabs)

		self.status = QStatusBar()

		self.setStatusBar(self.status)

		self.navtb = QToolBar("Navigation")

		self.addToolBar(self.navtb)

		back_btn = QAction("BACK", self)
		back_btn.setStatusTip("Back to previous page")
		back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
		self.navtb.addAction(back_btn)
		back_short = QShortcut(QKeySequence("Alt+Left"), self)
		back_short.activated.connect(lambda: self.tabs.currentWidget().back())

		next_btn = QAction("FORWARD", self)
		next_btn.setStatusTip("Forward to next page")
		next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
		self.navtb.addAction(next_btn)
		next_short = QShortcut(QKeySequence("Alt+Right"), self)
		next_short.activated.connect(lambda: self.tabs.currentWidget().forward())

		reload_btn = QAction("RELOAD", self)
		reload_btn.setStatusTip("Reload page")
		reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
		self.navtb.addAction(reload_btn)
		reload_short = QShortcut(QKeySequence("F5"), self)
		reload_short.activated.connect(lambda: self.tabs.currentWidget().reload())

		stop_btn = QAction("STOP", self)
		stop_btn.setStatusTip("Stop loading current page")
		stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
		self.navtb.addAction(stop_btn)
		stop_short = QShortcut(QKeySequence("Alt+ESC"), self)
		stop_short.activated.connect(lambda: self.tabs.currentWidget().stop())

		home_btn = QAction("HOME", self)
		home_btn.setStatusTip("Go home")
		home_btn.triggered.connect(self.navigate_home)
		self.navtb.addAction(home_btn)
		home_short = QShortcut(QKeySequence("Alt+Home"), self)
		home_short.activated.connect(self.navigate_home)

		sethome_btn = QAction("SETHOME", self)
		sethome_btn.setStatusTip("Set homepage as current url")
		# sethome_btn.triggered.connect(self.sethome())
		self.navtb.addAction(sethome_btn)

		ssl_btn = QAction("SSL", self)
		ssl_btn.setStatusTip("Page information")
		ssl_btn.triggered.connect(self.ssl_check)
		self.navtb.addAction(ssl_btn)

		self.urlbar = QLineEdit()

		self.urlbar.returnPressed.connect(self.navigate_to_url)

		self.navtb.addWidget(self.urlbar)

		empty1_lbl = QLabel("       ",self)
		self.navtb.addWidget(empty1_lbl)

		self.add_new_tab(QUrl(self.homepage), 'Homepage')

		self.show()

		self.setWindowTitle("Souvlaki Browser")

	def sethome(self):
		url = self.urlbar.text
		self.homepage = url

	def add_new_tab(self, qurl = None, label ="Blank"):

		if qurl is None:

			qurl = QUrl(self.homepage)

		browser = QWebEngineView()
		browser.settings().setAttribute(
            QWebEngineSettings.FullScreenSupportEnabled, True
        )

		browser.setUrl(qurl)

		i = self.tabs.addTab(browser, label)
		self.tabs.setCurrentIndex(i)

		browser.urlChanged.connect(lambda qurl, browser = browser:
								self.update_urlbar(qurl, browser))

		browser.page().profile().downloadRequested.connect(self._downloadRequested)

		browser.page().fullScreenRequested.connect(lambda request, browser = browser: self.handle_fullscreen_requested(request))

		browser.loadFinished.connect(lambda _, i = i, browser = browser:
									self.tabs.setTabText(i, browser.page().title()))

		browser.loadFinished.connect(lambda _, i = i, browser = browser:self.tabs.setTabIcon(i, browser.page().icon()))


	def tab_open_doubleclick(self, i):

		if i == -1:
			self.add_new_tab()
        
	def ssl_check(self):
		q = QUrl(self.urlbar.text())
		if q.scheme() == "http":
			QMessageBox.warning(self, "Security Information", "This website is insecure")
		if q.scheme() == "https":
			QMessageBox.information(self, "Security Information", "This website is secure")

	def handle_fullscreen_requested(self, request):
		request.accept()
		if request.toggleOn():
			self.showFullScreen()
			self.statusBar().hide()
			self.navtb.hide()
			self.tabs.tabBar().hide()
		else:
			self.showNormal()
			self.statusBar().show()
			self.navtb.show()
			self.tabs.tabBar().show()

	def _downloadRequested(self,item):
		item.accept()

	def current_tab_changed(self, i):

		qurl = self.tabs.currentWidget().url()

		self.update_urlbar(qurl, self.tabs.currentWidget())

		self.update_title(self.tabs.currentWidget())

	def close_current_tab(self, i):

		if self.tabs.count() < 2:
			return

		self.tabs.removeTab(i)

	def update_title(self, browser):

		if browser != self.tabs.currentWidget():
			return

		title = self.tabs.currentWidget().page().title()

	def navigate_home(self):

		self.tabs.currentWidget().setUrl(QUrl(self.homepage))

	def navigate_to_url(self):

		q = QUrl(self.urlbar.text())

		if q.scheme() == "":

			q.setScheme("http")

		self.tabs.currentWidget().setUrl(q)

	def update_urlbar(self, q, browser = None):

		if browser != self.tabs.currentWidget():

			return

		self.urlbar.setText(q.toString())

		self.urlbar.setCursorPosition(0)

app = QApplication(sys.argv)

app.setApplicationName("Souvlaki Browser")

app.setWindowIcon(QIcon("icon.png"))

window = MainWindow()

app.exec_()