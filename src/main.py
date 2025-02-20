from __future__ import annotations
import sys
from argparse import ArgumentParser, RawTextHelpFormatter

from PySide6.QtWebEngineCore import QWebEngineProfile, QWebEngineSettings, qWebEngineChromiumVersion
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import QCoreApplication, QLoggingCategory, QUrl

from components.browser import Browser
from lib.config import Config

if __name__ == "__main__":
  print(f"Chromium Version: {qWebEngineChromiumVersion()}")

  parser = ArgumentParser(description=Config["APP_NAME"],
                          formatter_class=RawTextHelpFormatter)
  parser.add_argument("--single-process", "-s", action="store_true",
                      help="Run in single process mode (trouble shooting)")
  parser.add_argument("url", type=str, nargs="?", help="URL")
  args = parser.parse_args()

  QCoreApplication.setOrganizationName(Config["AUTHOR"])

  app_args = sys.argv
  if args.single_process:
    app_args.extend(["--webEngineArgs", "--single-process"])
  app = QApplication(app_args)
  app.setWindowIcon(QIcon(Config["APP_LOGO"]))
  QLoggingCategory.setFilterRules("qt.webenginecontext.debug=true")

  s = QWebEngineProfile.defaultProfile().settings()
  s.setAttribute(QWebEngineSettings.WebAttribute.PluginsEnabled, True)
  s.setAttribute(QWebEngineSettings.WebAttribute.DnsPrefetchEnabled, True)

  browser = Browser()
  window = browser.create_hidden_window()

  url = QUrl.fromUserInput(args.url) if args.url else QUrl(Config["START_PAGE"])
  window.tab_widget().set_url(url)
  window.show()
  sys.exit(app.exec())
