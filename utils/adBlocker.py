from PyQt5 import QtWebEngineCore
from adblockparser import AdblockRules

with open("filters.txt", "r", -1, "utf-8") as f:
    raw_rules = f.readlines()
    rules = AdblockRules(raw_rules)

class AdBlocker(QtWebEngineCore.QWebEngineUrlRequestInterceptor):
    def interceptRequest(self, info):
        url = info.requestUrl().toString()
        if rules.should_block(url):
            print("Blocking URL:", url)
            info.block(True)
        else:
            print("Allowing URL:", url)