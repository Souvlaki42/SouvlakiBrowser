from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWebEngineCore import QWebEnginePage, QWebEngineSettings
from PyQt6.QtWebEngineWidgets import QWebEngineView
from components.downloader import DownloadManager
from components.webPageUi import Ui_wpWidget
import os, subprocess, math

from PyQt6 import QtWebEngineCore
from adblockparser import AdblockRules
from typing import Optional

SETTINGS = QWebEngineSettings.WebAttribute

class AdBlocker(QtWebEngineCore.QWebEngineUrlRequestInterceptor):
		def __init__(self, parent: Optional[QtCore.QObject] = None):
			super().__init__(parent)
			with open("filters.txt", "r", -1, "utf-8") as f:
				raw_rules = f.readlines()
				self.rules = AdblockRules(raw_rules)

		def interceptRequest(self, info):
			url = info.requestUrl().toString()
			if self.rules.should_block(url):
					print("Blocking URL:", url)
					info.block(True)
			else:
					print("Allowing URL:", url)		


class WebPage(QtWidgets.QWidget, Ui_wpWidget):
	def __init__(self, tab = None, tBar = None, main = None, parent = None):
		super(WebPage, self).__init__(parent = parent)
		self.setupUi(self)

		self.webEngineView = QWebEngineView()
		self.webEngineView.page().setBackgroundColor(QtGui.QColor(45, 45, 45, 255))
		self.webEngineView.setObjectName("webEngineView")
		self.verticalLayout_3.addWidget(self.webEngineView)

		self.tab = tab
		self.tBar = tBar
		self.main = main
		self.url = "https://google.com"

		self.wpLineEdit.returnPressed.connect(self.load)
		self.wpPushButton.clicked.connect(self.backward)
		self.wpPushButton_2.clicked.connect(self.forward)
		self.wpPushButton_3.clicked.connect(self.reloadStop)
		self.wpPushButton_4.clicked.connect(lambda: self.load(self.url))

		self.webEngineView.page().fullScreenRequested.connect(lambda request: self.fullscreenRequested(request))
		self.webEngineView.loadFinished.connect(self.loadFinished)
		self.webEngineView.urlChanged.connect(self.urlChanged)
		self.webEngineView.iconChanged.connect(lambda icon: self.iconChanged(icon))
		self.webEngineView.loadStarted.connect(lambda: self.wpPushButton_3.setText("9"))
		self.webEngineView.loadFinished.connect(lambda: self.wpPushButton_3.setText("Z"))
		self.webEngineView.page().profile().downloadRequested.connect(self.downloadRequested)
		self.webEngineView.page().profile().setUrlRequestInterceptor(AdBlocker())

		self.load(self.url)

		self.webEngineView.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
		self.webEngineView.customContextMenuRequested.connect(self.contextMenu)

		self.webEngineView.settings().setAttribute(SETTINGS.FullScreenSupportEnabled, True)
		self.webEngineView.settings().setAttribute(SETTINGS.JavascriptCanOpenWindows, True)
		self.webEngineView.settings().setAttribute(SETTINGS.PluginsEnabled, True)
		self.webEngineView.settings().setAttribute(SETTINGS.JavascriptEnabled, True)
		self.webEngineView.settings().setAttribute(SETTINGS.ScreenCaptureEnabled, True)
		self.webEngineView.settings().setAttribute(SETTINGS.LocalContentCanAccessRemoteUrls, True)
		self.webEngineView.settings().setAttribute(SETTINGS.AllowRunningInsecureContent, True)
		self.webEngineView.settings().setAttribute(SETTINGS.AllowGeolocationOnInsecureOrigins, True)
		self.webEngineView.settings().setAttribute(SETTINGS.AllowWindowActivationFromJavaScript, True)
		self.webEngineView.settings().setAttribute(SETTINGS.ShowScrollBars, True)
		self.webEngineView.settings().setAttribute(SETTINGS.WebGLEnabled, True)
		self.webEngineView.settings().setAttribute(SETTINGS.Accelerated2dCanvasEnabled, True)
		self.webEngineView.settings().setAttribute(SETTINGS.TouchIconsEnabled, True)
		self.webEngineView.settings().setAttribute(SETTINGS.AutoLoadIconsForPage, True)
		self.webEngineView.settings().setAttribute(SETTINGS.JavascriptCanAccessClipboard, True)
		self.webEngineView.settings().setAttribute(SETTINGS.JavascriptCanPaste, True)
		self.webEngineView.settings().setAttribute(SETTINGS.WebRTCPublicInterfacesOnly, True)
		self.webEngineView.settings().setAttribute(SETTINGS.Accelerated2dCanvasEnabled, True)
		self.webEngineView.settings().setAttribute(SETTINGS.LocalStorageEnabled, True)
		self.webEngineView.settings().setAttribute(SETTINGS.AutoLoadImages, True)

	def fullscreenRequested(self, request):
		request.accept()
		if request.toggleOn():
			self.wasMaximized = self.main.isMaximized()
			self.showFullScreen()
			self.wpWidget_3.hide()
			self.tBar.hide()
			self.main.showMaximized()
		else:
			self.showMaximized()
			self.wpWidget_3.show()
			self.tBar.show()
			if self.wasMaximized:
				self.main.showMaximized()
			else:
				self.main.showNormal()

	def contextActions(self):
		backAction = QtGui.QAction("Back", self)
		backSequence = QtGui.QKeySequence("Alt+Left")
		backShort = QtGui.QShortcut(backSequence, self)
		backAction.setShortcut(backSequence)
		backAction.triggered.connect(self.backward)
		backShort.activated.connect(self.backward)
		backAction.setShortcutVisibleInContextMenu(True)

		forwardAction = QtGui.QAction("Forward", self)
		forwardSequence = QtGui.QKeySequence("Alt+Right")
		forwardShort = QtGui.QShortcut(forwardSequence, self)
		forwardAction.setShortcut(forwardSequence)
		forwardAction.triggered.connect(self.forward)
		forwardShort.activated.connect(self.forward)
		forwardAction.setShortcutVisibleInContextMenu(True)

		reloadAction = QtGui.QAction("Reload", self)
		reloadSequence = QtGui.QKeySequence("f5")
		reloadShort = QtGui.QShortcut(reloadSequence, self)
		reloadAction.setShortcut(reloadSequence)
		reloadAction.triggered.connect(self.reloadStop)
		reloadShort.activated.connect(self.reloadStop)
		reloadAction.setShortcutVisibleInContextMenu(True)

		sourceAction = QtGui.QAction("Source", self)
		sourceSequence = QtGui.QKeySequence("Ctrl+U")
		sourceShort = QtGui.QShortcut(sourceSequence, self)
		sourceAction.setShortcut(sourceSequence)
		sourceAction.triggered.connect(lambda: self.main.source())
		sourceShort.activated.connect(lambda: self.main.source())
		sourceAction.setShortcutVisibleInContextMenu(True)

		inspectAction = QtGui.QAction("Inspect", self)
		inspectSequence = QtGui.QKeySequence("f12")
		inspectShort = QtGui.QShortcut(inspectSequence, self)
		inspectAction.setShortcut(inspectSequence)
		inspectAction.triggered.connect(self.inspect)
		inspectShort.activated.connect(self.inspect)
		inspectAction.setShortcutVisibleInContextMenu(True)

		return {"back": backAction, "forward": forwardAction, "reload": reloadAction, "source": sourceAction, "inspect": inspectAction}

	def contextMenu(self, event):
		context_menu = QtWidgets.QMenu(self)
		context_menu.addAction(self.contextActions()["back"])
		context_menu.addAction(self.contextActions()["forward"])
		context_menu.addAction(self.contextActions()["reload"])
		context_menu.addSeparator()
		context_menu.addAction(self.contextActions()["source"])
		context_menu.addSeparator()
		context_menu.addAction(self.contextActions()["inspect"])
		context_menu.exec(self.mapToGlobal(self.mapFromGlobal(QtGui.QCursor.pos())))

	def iconChanged(self, icon):
		if icon.isNull():
			icon = QtGui.QIcon("icon.ico")
		self.tab.tabIcon.setIcon(icon)

	def urlChanged(self):
		self.wpLineEdit.setText(self.webEngineView.page().url().toString())

	def loadFinished(self):
		self.tab.tabLabel.setText(self.webEngineView.page().title())

	def load(self, url = None):
		if url == None: urlObj = QtCore.QUrl.fromUserInput(self.wpLineEdit.text())
		else: urlObj = QtCore.QUrl(url)
		if not urlObj.isValid(): return
		else: self.webEngineView.load(urlObj)

	def backward(self):
		self.webEngineView.page().triggerAction(QWebEnginePage.Back)

	def forward(self):
		self.webEngineView.page().triggerAction(QWebEnginePage.Forward)

	def reloadStop(self):
		if self.wpPushButton_3.text() == "Z":
			self.webEngineView.page().triggerAction(QWebEnginePage.Reload)
		if self.wpPushButton_3.text() == "9":
			self.webEngineView.page().triggerAction(QWebEnginePage.Stop)

	def inspect(self):
		DEBUG_PORT = "5588"
		DEBUG_URL = "http://127.0.0.1:%s" % DEBUG_PORT
		os.environ["QTWEBENGINE_REMOTE_DEBUGGING"] = DEBUG_PORT
		self.inspector = QWebEngineView()
		self.inspector.setWindowTitle(f"DevTools - {self.wpLineEdit.text()}")
		self.inspector.setWindowIcon(QtGui.QIcon("icon.ico"))
		self.inspector.load(QtCore.QUrl(DEBUG_URL))
		self.webEngineView.page().setDevToolsPage(self.inspector.page())
		self.inspector.show()

	def calculateDownloadPercentage(self, received_bytes, total_bytes):
		percentage = received_bytes / total_bytes * 100
		return int(math.trunc(percentage))
	
	def downloadRequested(self, item):
		self.DownloadManager = QtWidgets.QWidget()
		self.downloadUi = DownloadManager()
		self.downloadUi.setupUi(self.DownloadManager)
		self.DownloadManager.show()
		self.download_timer = QtCore.QTimer()
		self.downloadUi.filenameText.setText(item.suggestedFileName())
		self.download_timer.timeout.connect(lambda: self.download_loop(item))
		self.download_timer.setInterval(1000)
		item.accept()
		self.download_timer.start()
		self.downloadUi.folderBtn.clicked.connect(lambda: self.folder_btn_exec(item.downloadDirectory()))

	def folder_btn_exec(self, download_dir):
		subprocess.Popen(f'explorer "{download_dir}"')
		self.DownloadManager.close()

	def download_loop(self, item):
		if item.isFinished() and self.downloadUi.progressBar.value() == 100:
			self.downloadUi.folderBtn.setEnabled(True)
			self.download_timer.stop()
		else:
			self.downloadUi.progressBar.setValue(self.calculateDownloadPercentage(item.receivedBytes(), item.totalBytes()))

	