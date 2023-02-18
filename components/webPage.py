######################################################
##  SihinaCode > Search YouTube for more tutorials  ##
######################################################
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView, QWebEngineSettings
from components.downloaderUi import Ui_DownloadManager
from components.webPageUi import Ui_wpWidget
import os, subprocess, math

from utils.downloadFolder import getDownloadFolder
from utils.downloadFolderOld import get_download_folder

class WebPage(QtWidgets.QWidget, Ui_wpWidget):
	def __init__(self, tab = None, tBar = None, main = None, parent = None):
		super(WebPage, self).__init__(parent = parent)
		self.setupUi(self)

		self.webEngineView = QWebEngineView()
		self.webEngineView.page().setBackgroundColor(QtGui.QColor(45, 45, 45, 255))
		self.webEngineView.setObjectName("webEngineView")
		self.verticalLayout_3.addWidget(self.webEngineView)

		self.wpLineEdit.returnPressed.connect(self.load)
		self.wpPushButton.clicked.connect(self.backward)
		self.wpPushButton_2.clicked.connect(self.forward)
		self.wpPushButton_3.clicked.connect(self.reloadStop)
		self.wpPushButton_4.clicked.connect(lambda: self.load("https://google.com"))

		self.tab = tab
		self.tBar = tBar
		self.main = main

		self.webEngineView.page().fullScreenRequested.connect(lambda request: self.fullscreenRequested(request))
		self.webEngineView.loadFinished.connect(self.loadFinished)
		self.webEngineView.urlChanged.connect(self.urlChanged)
		self.webEngineView.iconChanged.connect(lambda icon: self.iconChanged(icon))
		self.webEngineView.loadStarted.connect(lambda: self.wpPushButton_3.setText("9"))
		self.webEngineView.loadFinished.connect(lambda: self.wpPushButton_3.setText("Z"))
		self.webEngineView.page().profile().downloadRequested.connect(self.downloadRequested)

		self.load("https://google.com")
		# self.load("https://www.youtube.com/watch?v=ouEzZbj1BkQ")
		# self.load("https://chrome.com")
		# self.load("https://www.youtube.com/html5")

		self.webEngineView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
		self.webEngineView.customContextMenuRequested.connect(self.contextMenu)

		self.webEngineView.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
		self.webEngineView.settings().setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)
		self.webEngineView.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
		self.webEngineView.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
		# self.webEngineView.settings().setAttribute(QWebEngineSettings.FullViewportEnabled, True)
		self.webEngineView.settings().setAttribute(QWebEngineSettings.ScreenCaptureEnabled, True)
		self.webEngineView.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
		self.webEngineView.settings().setAttribute(QWebEngineSettings.AllowRunningInsecureContent, True)
		self.webEngineView.settings().setAttribute(QWebEngineSettings.AllowGeolocationOnInsecureOrigins, True)
		self.webEngineView.settings().setAttribute(QWebEngineSettings.AllowWindowActivationFromJavaScript, True)
		self.webEngineView.settings().setAttribute(QWebEngineSettings.ShowScrollBars, True)
		self.webEngineView.settings().setAttribute(QWebEngineSettings.WebGLEnabled, True)
		self.webEngineView.settings().setAttribute(QWebEngineSettings.Accelerated2dCanvasEnabled, True)
		self.webEngineView.settings().setAttribute(QWebEngineSettings.TouchIconsEnabled, True)
		self.webEngineView.settings().setAttribute(QWebEngineSettings.AutoLoadIconsForPage, True)
		# self.webEngineView.settings().setAttribute(QWebEngineSettings.AcceleratedVideoDecodeEnabled, True)
		# self.webEngineView.settings().setAttribute(QWebEngineSettings.HardwareAccelerationEnabled, True)
		self.webEngineView.settings().setAttribute(QWebEngineSettings.JavascriptCanAccessClipboard, True)
		self.webEngineView.settings().setAttribute(QWebEngineSettings.JavascriptCanPaste, True)
		# self.webEngineView.settings().setAttribute(QWebEngineSettings.UrlRequestInterceptorEnabled, True)
		self.webEngineView.settings().setAttribute(QWebEngineSettings.WebRTCPublicInterfacesOnly, True)
		self.webEngineView.settings().setAttribute(QWebEngineSettings.Accelerated2dCanvasEnabled, True)
		self.webEngineView.settings().setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
		self.webEngineView.settings().setAttribute(QWebEngineSettings.AutoLoadImages, True)

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
		backAction = QtWidgets.QAction("Back", self)
		backSequence = QtGui.QKeySequence("Alt+Left")
		backShort = QtWidgets.QShortcut(backSequence, self)
		backAction.setShortcut(backSequence)
		backAction.triggered.connect(self.backward)
		backShort.activated.connect(self.backward)
		backAction.setShortcutVisibleInContextMenu(True)

		forwardAction = QtWidgets.QAction("Forward", self)
		forwardSequence = QtGui.QKeySequence("Alt+Right")
		forwardShort = QtWidgets.QShortcut(forwardSequence, self)
		forwardAction.setShortcut(forwardSequence)
		forwardAction.triggered.connect(self.forward)
		forwardShort.activated.connect(self.forward)
		forwardAction.setShortcutVisibleInContextMenu(True)

		reloadAction = QtWidgets.QAction("Reload", self)
		reloadSequence = QtGui.QKeySequence("f5")
		reloadShort = QtWidgets.QShortcut(reloadSequence, self)
		reloadAction.setShortcut(reloadSequence)
		reloadAction.triggered.connect(self.reloadStop)
		reloadShort.activated.connect(self.reloadStop)
		reloadAction.setShortcutVisibleInContextMenu(True)

		sourceAction = QtWidgets.QAction("Source", self)
		sourceSequence = QtGui.QKeySequence("Ctrl+U")
		sourceShort = QtWidgets.QShortcut(sourceSequence, self)
		sourceAction.setShortcut(sourceSequence)
		sourceAction.triggered.connect(lambda: self.main.source())
		sourceShort.activated.connect(lambda: self.main.source())
		sourceAction.setShortcutVisibleInContextMenu(True)

		inspectAction = QtWidgets.QAction("Inspect", self)
		inspectSequence = QtGui.QKeySequence("f12")
		inspectShort = QtWidgets.QShortcut(inspectSequence, self)
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
		context_menu.exec_(self.mapToGlobal(self.mapFromGlobal(QtGui.QCursor.pos())))
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
		try:
			item.setDownloadDirectory(getDownloadFolder())
		except:
			item.setDownloadDirectory(get_download_folder())
		self.DownloadManager = QtWidgets.QWidget()
		self.downloadUi = Ui_DownloadManager()
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

	