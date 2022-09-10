from PyQt5.QtWidgets import QMainWindow, QTabWidget, QStatusBar, QAction, QShortcut, QToolBar, QLabel, QLineEdit, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtGui import QKeySequence, QIcon
from modules.downloading import DownloadManager
from PyQt5.QtCore import QUrl
from modules.settings import Settings
from config import jsonParser
import sys

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()

		self.homepage = jsonParser.read_key("homepage")
		self.linkpreview = jsonParser.read_key("linkpreview")

		self.showMaximized()

		self.tabs = QTabWidget()

		self.tabs.setDocumentMode(True)

		self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)

		self.tabs.currentChanged.connect(self.current_tab_changed)

		self.tabs.setTabsClosable(True)

		self.tabs.tabCloseRequested.connect(self.close_current_tab)

		self.setCentralWidget(self.tabs)

		self.status = QStatusBar()

		self.setStatusBar(self.status)

		self.navtb = QToolBar("Navigation")

		self.addToolBar(self.navtb)

		self.navtb.setMovable(False)

		back_btn = QAction(QIcon("assets/back.png"), "Back", self)
		back_btn.setStatusTip("Back to previous page")
		back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
		self.navtb.addAction(back_btn)
		back_short = QShortcut(QKeySequence("Alt+Left"), self)
		back_short.activated.connect(lambda: self.tabs.currentWidget().back())

		next_btn = QAction(QIcon("assets/next.png"), "Forward", self)
		next_btn.setStatusTip("Forward to next page")
		next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
		self.navtb.addAction(next_btn)
		next_short = QShortcut(QKeySequence("Alt+Right"), self)
		next_short.activated.connect(lambda: self.tabs.currentWidget().forward())

		reload_btn = QAction(QIcon("assets/rotate-right.png"), "Reload", self)
		reload_btn.setStatusTip("Reload page")
		reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
		self.navtb.addAction(reload_btn)
		reload_short = QShortcut(QKeySequence("F5"), self)
		reload_short.activated.connect(lambda: self.tabs.currentWidget().reload())

		stop_btn = QAction(QIcon("assets/cross.png"), "Stop", self)
		stop_btn.setStatusTip("Stop loading current page")
		stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
		self.navtb.addAction(stop_btn)
		stop_short = QShortcut(QKeySequence("Alt+ESC"), self)
		stop_short.activated.connect(lambda: self.tabs.currentWidget().stop())

		home_btn = QAction(QIcon("assets/home.png"), "Home", self)
		home_btn.setStatusTip("Go home")
		home_btn.triggered.connect(self.navigate_home)
		self.navtb.addAction(home_btn)
		home_short = QShortcut(QKeySequence("Alt+Home"), self)
		home_short.activated.connect(self.navigate_home)

		self.ssl_btn = QAction()
		self.ssl_btn.setStatusTip("SSL/TLS Info")
		self.ssl_btn.setIcon(QIcon("assets/unlock.png"))
		self.navtb.addAction(self.ssl_btn)

		empty3_lbl = QLabel("  ",self)
		self.navtb.addWidget(empty3_lbl)

		self.urlbar = QLineEdit()
		self.urlbar.setStyleSheet("QLineEdit { border-radius: 10px;}")

		self.urlbar.returnPressed.connect(self.navigate_to_url)

		self.navtb.addWidget(self.urlbar)

		empty4_lbl = QLabel("  ",self)
		self.navtb.addWidget(empty4_lbl)

		newwindow_btn = QAction(QIcon("assets/browser.png"), "New Window", self)
		newwindow_btn.setStatusTip("Open new window")
		newwindow_btn.triggered.connect(lambda:MainWindow())
		self.navtb.addAction(newwindow_btn)
		newwindow_short = QShortcut(QKeySequence("Ctrl+N"), self)
		newwindow_short.activated.connect(lambda:MainWindow())

		source_btn = QAction(QIcon("assets/stats.png"), "Source", self)
		source_btn.setStatusTip("View page source")
		source_btn.triggered.connect(lambda:self.tabs.currentWidget().setUrl(QUrl(source())))
		self.navtb.addAction(source_btn)
		source_short = QShortcut(QKeySequence("Ctrl+U"), self)
		source_short.activated.connect(lambda:self.tabs.currentWidget().setUrl(QUrl(source())))

		settings_btn = QAction(QIcon("assets/settings.png"), "Settings", self)
		settings_btn.setToolTip("Open browser settings window")
		settings_btn.triggered.connect(self.open_settings)
		self.navtb.addAction(settings_btn)
		settings_short = QShortcut(QKeySequence("Alt+P"), self)
		settings_short.activated.connect(self.open_settings)

		newtab_short = QShortcut(QKeySequence("Ctrl+T"), self)
		newtab_short.activated.connect(lambda:self.add_new_tab(QUrl(self.homepage), 'Homepage'))
		closetab_short = QShortcut(QKeySequence("Ctrl+W"), self)
		closetab_short.activated.connect(lambda:self.close_current_tab(self.tabs.currentIndex()))


		def source():
			source = "view-source:"
			url = str(self.urlbar.text())
			r = source + url
			t = str(r)
			return t

		self.add_new_tab(QUrl(self.homepage), 'Homepage')

		self.setWindowTitle("Souvlaki Browser")

	def sethome(self, url, homepage):
		homepage = url

	def add_new_tab(self, qurl = None, label = "Blank"):

		if qurl is None:

			qurl = QUrl(self.homepage)

		browser = QWebEngineView()
		browser.settings().setAttribute(
			QWebEngineSettings.FullScreenSupportEnabled, True
		)
		browser.settings().setAttribute(
			QWebEngineSettings.JavascriptCanOpenWindows, True
		)

		browser.setUrl(qurl)

		i = self.tabs.addTab(browser, label)
		self.tabs.setCurrentIndex(i)
		self.tabs.setTabIcon(i, browser.icon())
		browser.iconChanged.connect(lambda icon, browser=browser: self.update_icon(browser, icon))

		browser.urlChanged.connect(lambda qurl, browser = browser:
								self.update_urlbar(qurl, browser))

		browser.page().profile().downloadRequested.connect(self._downloadRequested)

		if self.linkpreview:
			browser.page().linkHovered.connect(self.status.showMessage)

		browser.page().fullScreenRequested.connect(lambda request, browser = browser: self.handle_fullscreen_requested(request))

		browser.loadFinished.connect(lambda _, i = i, browser = browser:
									self.tabs.setTabText(i, browser.page().title()))

	def update_icon(self, browser, icon):
		index = self.tabs.indexOf(browser)
		self.tabs.setTabIcon(index, icon)


	def tab_open_doubleclick(self, i):

		if i == -1:
			self.add_new_tab()

	def open_settings(self):
		self.settingswindow = QWidget()
		self.settings = Settings()
		self.settings.setupUi(self.settingswindow)
		self.settingswindow.show()

	def closeEvent(self, event):
		if hasattr(self, "settings"):
			jsonParser.write_key("homepage", self.settings.hometext.property("text"))
			jsonParser.write_key("darkmode", self.settings.darkcheck.property("checked"))
			jsonParser.write_key("linkpreview", self.settings.linkpreviewcheck.property("checked"))
		sys.exit()

	def handle_fullscreen_requested(self, request):
		request.accept()
		if request.toggleOn():
			self.showFullScreen()
			self.statusBar().hide()
			self.navtb.hide()
			self.tabs.tabBar().hide()
		else:
			self.showMaximized()
			self.statusBar().show()
			self.navtb.show()
			self.tabs.tabBar().show()

	def _downloadRequested(self, item):
		item.accept()
		self.downloadwindow = QWidget()
		self.downloadManager = DownloadManager()
		self.downloadManager.setupUi(self.downloadwindow)
		self.downloadManager.progressBar.setProperty("value", 0)
		self.downloadManager.label.text = item.downloadFileName()
		self.downloadwindow.show()

	def current_tab_changed(self, i):

		qurl = self.tabs.currentWidget().url()

		self.update_urlbar(qurl, self.tabs.currentWidget())

		self.update_title(self.tabs.currentWidget())

	def close_current_tab(self, i):
		if self.tabs.count() < 2:
			self.close()
			return
		page = self.tabs.widget(i)
		self.tabs.removeTab(i)
		page.deleteLater()

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

		if q.scheme() == 'https':
			# Secure padlock icon
			self.ssl_btn.setStatusTip("Secure Connection")
			self.ssl_btn.setIcon(QIcon("assets/lock.png"))

		else:
			# Insecure padlock icon
			self.ssl_btn.setStatusTip("Insecure Connection")
			self.ssl_btn.setIcon(QIcon("assets/unlock.png"))
