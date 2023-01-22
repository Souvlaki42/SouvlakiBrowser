from PyQt5.QtWidgets import QMainWindow, QTabWidget, QStatusBar, QAction, QShortcut, QToolBar, QLabel, QLineEdit, QWidget, QMenu
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtGui import QKeySequence, QIcon, QCursor
from modules.downloader import DownloadManager
from PyQt5.QtCore import QUrl, Qt
from modules.settings import Settings
from modules.config import jsonParser

DEBUG_PORT = "5588"
DEBUG_URL = "http://127.0.0.1:%s" % DEBUG_PORT

import os, math, time
os.environ["QTWEBENGINE_REMOTE_DEBUGGING"] = DEBUG_PORT

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

		self.back_btn = QAction(QIcon("assets/images/back.png"), "Back", self)
		self.back_btn.setStatusTip("Go to the previous page")
		self.back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
		self.navtb.addAction(self.back_btn)
		back_sequence = QKeySequence("Alt+Left")
		back_short = QShortcut(back_sequence, self)
		back_short.activated.connect(lambda: self.tabs.currentWidget().back())
		self.back_btn.setShortcut(back_sequence)
		self.back_btn.setShortcutVisibleInContextMenu(True)

		self.next_btn = QAction(QIcon("assets/images/next.png"), "Forward", self)
		self.next_btn.setStatusTip("Go to the next page")
		self.next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
		self.navtb.addAction(self.next_btn)
		next_sequence = QKeySequence("Alt+Right")
		next_short = QShortcut(next_sequence, self)
		next_short.activated.connect(lambda: self.tabs.currentWidget().forward())
		self.next_btn.setShortcut(next_sequence)
		self.next_btn.setShortcutVisibleInContextMenu(True)

		self.reload_btn = QAction(QIcon("assets/images/rotate-right.png"), "Reload", self)
		self.reload_btn.setStatusTip("Reload page")
		self.reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
		self.navtb.addAction(self.reload_btn)
		reload_sequence = QKeySequence("F5")
		reload_short = QShortcut(reload_sequence, self)
		reload_short.activated.connect(lambda: self.tabs.currentWidget().reload())
		self.reload_btn.setShortcut(reload_sequence)
		self.reload_btn.setShortcutVisibleInContextMenu(True)

		self.stop_btn = QAction(QIcon("assets/images/cross.png"), "Stop", self)
		self.stop_btn.setStatusTip("Stop loading current page")
		self.stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
		self.navtb.addAction(self.stop_btn)
		stop_sequence = QKeySequence("Alt+ESC")
		stop_short = QShortcut(stop_sequence, self)
		stop_short.activated.connect(lambda: self.tabs.currentWidget().stop())
		self.stop_btn.setShortcut(stop_sequence)
		self.stop_btn.setShortcutVisibleInContextMenu(True)

		self.home_btn = QAction(QIcon("assets/images/home.png"), "Home", self)
		self.home_btn.setStatusTip("Go home")
		self.home_btn.triggered.connect(self.navigate_home)
		self.navtb.addAction(self.home_btn)
		home_short = QShortcut(QKeySequence("Alt+Home"), self)
		home_short.activated.connect(self.navigate_home)

		self.ssl_btn = QAction()
		self.ssl_btn.setStatusTip("SSL/TLS Info")
		self.ssl_btn.setIcon(QIcon("assets/images/unlock.png"))
		self.navtb.addAction(self.ssl_btn)

		empty3_lbl = QLabel("  ",self)
		self.navtb.addWidget(empty3_lbl)

		self.urlbar = QLineEdit()
		self.urlbar.setStyleSheet("QLineEdit { border-radius: 10%; height: 20%; padding: 0 5%; }")

		self.urlbar.returnPressed.connect(self.navigate_to_url)

		self.navtb.addWidget(self.urlbar)

		empty4_lbl = QLabel("  ",self)
		self.navtb.addWidget(empty4_lbl)
		self.inspector = QWebEngineView()

		self.newwindow_btn = QAction(QIcon("assets/images/browser.png"), "New Window", self)
		self.newwindow_btn.setStatusTip("Open new window")
		self.newwindow_btn.triggered.connect(lambda: MainWindow())
		self.navtb.addAction(self.newwindow_btn)
		newwindow_short = QShortcut(QKeySequence("Ctrl+N"), self)
		newwindow_short.activated.connect(lambda: MainWindow())

		self.source_btn = QAction(QIcon("assets/images/stats.png"), "View page source", self)
		self.source_btn.setStatusTip("View page source")
		self.source_btn.triggered.connect(lambda:self.tabs.currentWidget().setUrl(QUrl(self.source())))
		source_sequence = QKeySequence("Ctrl+U")
		source_short = QShortcut(source_sequence, self)
		source_short.activated.connect(lambda:self.tabs.currentWidget().setUrl(QUrl(self.source())))
		self.source_btn.setShortcut(source_sequence)
		self.source_btn.setShortcutVisibleInContextMenu(True)

		self.inspect_btn = QAction(QIcon("assets/images/stats.png"), "Inspect", self)
		self.inspect_btn.setStatusTip("Inspect Page")
		self.inspect_btn.triggered.connect(self.inspect)
		inspect_sequence = QKeySequence("F12")
		inspect_short = QShortcut(inspect_sequence, self)
		inspect_short.activated.connect(self.inspect)
		self.inspect_btn.setShortcut(inspect_sequence)
		self.inspect_btn.setShortcutVisibleInContextMenu(True)

		self.settings_btn = QAction(QIcon("assets/images/settings.png"), "Settings", self)
		self.settings_btn.setToolTip("Open browser settings window")
		self.settings_btn.triggered.connect(self.open_settings)
		self.navtb.addAction(self.settings_btn)
		settings_short = QShortcut(QKeySequence("Alt+P"), self)
		settings_short.activated.connect(self.open_settings)

		newtab_short = QShortcut(QKeySequence("Ctrl+T"), self)
		newtab_short.activated.connect(lambda:self.add_new_tab(QUrl(self.homepage), "Homepage"))
		closetab_short = QShortcut(QKeySequence("Ctrl+W"), self)
		closetab_short.activated.connect(lambda:self.close_current_tab(self.tabs.currentIndex()))

		self.add_new_tab()

		self.setWindowTitle("Souvlaki Browser")

	def inspect(self):
		self.inspector = QWebEngineView()
		self.inspector.load(QUrl(DEBUG_URL))
		self.browser.page().setDevToolsPage(self.inspector.page())
		self.inspector.show()

	def source(self):
		return f"view-source:{self.urlbar.text()}"

	def sethome(self, url, homepage):
		homepage = url

	def add_new_tab(self, label = None, url = None):

		if url is None:
			url = self.homepage

		qurl = QUrl(url)

		self.browser = QWebEngineView()
		self.browser.settings().setAttribute(
			QWebEngineSettings.FullScreenSupportEnabled, True
		)
		self.browser.settings().setAttribute(
			QWebEngineSettings.JavascriptCanOpenWindows, True
		)

		self.browser.setUrl(qurl)
		if label is None:
			label = "New Tab"
		i = self.tabs.addTab(self.browser, label)
		self.tabs.setCurrentIndex(i)
		self.tabs.setTabIcon(i, self.browser.icon())
		self.browser.iconChanged.connect(lambda icon, browser=self.browser: self.update_icon(browser, icon))

		self.browser.urlChanged.connect(lambda qurl, browser = self.browser: self.update_urlbar(qurl, browser))

		self.browser.page().profile().downloadRequested.connect(self._downloadRequested)

		if self.linkpreview:
			self.browser.page().linkHovered.connect(self.status.showMessage)

		self.browser.page().fullScreenRequested.connect(lambda request, browser = self.browser: self.handle_fullscreen_requested(request))

		self.browser.loadFinished.connect(lambda _, i = i: self.handleLoadFinished(i))

		self.browser.setContextMenuPolicy(Qt.CustomContextMenu)
		self.browser.customContextMenuRequested.connect(self.create_context_menu)
	
	def handleLoadFinished(self, i):
		self.tabs.setTabText(i, self.browser.page().title())

	def create_context_menu(self, event):
		context_menu = QMenu(self)

		context_menu.addAction(self.back_btn)
		context_menu.addAction(self.next_btn)
		context_menu.addAction(self.reload_btn)
		context_menu.addSeparator()
		context_menu.addAction(self.source_btn)
		context_menu.addSeparator()
		context_menu.addAction(self.inspect_btn)
	
		context_menu.exec_(self.mapToGlobal(self.mapFromGlobal(QCursor.pos())))

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
		self.close()

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

	def calculateDownloadPercentage(self, received_bytes, total_bytes):
		percentage = received_bytes / total_bytes * 100
		return int(math.trunc(percentage))

	def _downloadRequested(self, item):
		item.accept()
		self.download_manager = DownloadManager()
		self.download_manager.show()

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

		self.inspector.setWindowTitle(f"Web Inspector - {self.urlbar.text()}")

	def update_urlbar(self, q, browser = None):

		if browser != self.tabs.currentWidget():

			return

		self.urlbar.setText(q.toString())

		self.urlbar.setCursorPosition(0)

		if q.scheme() == "https":
			# Secure padlock icon
			self.ssl_btn.setStatusTip("Secure Connection")
			self.ssl_btn.setIcon(QIcon("assets/images/lock.png"))

		else:
			# Insecure padlock icon
			self.ssl_btn.setStatusTip("Insecure Connection")
			self.ssl_btn.setIcon(QIcon("assets/images/unlock.png"))
