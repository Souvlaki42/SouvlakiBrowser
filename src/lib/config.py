from typing import TypedDict

BASE_PATH = "src/assets/"
APP_NAME = "Souvlaki Browser"


class ConfigDict(TypedDict):
  APP_LOGO: str
  DIALOG_ERROR: str
  EDIT_CLEAR: str
  GO_BOTTOM: str
  GO_NEXT: str
  GO_PREVIOUS: str
  NINJA_LOGO: str
  PROCESS_STOP: str
  TEXT_HTML: str
  VIEW_REFRESH: str
  APP_NAME: str
  APP_NAME_LOWER: str
  START_PAGE: str
  AUTHOR: str
  SEARCH_ENGINE: str


Config: ConfigDict = {
  "APP_LOGO": f"{BASE_PATH}app-logo.png",
  "DIALOG_ERROR": f"{BASE_PATH}dialog-error.png",
  "EDIT_CLEAR": f"{BASE_PATH}edit-clear.png",
  "GO_BOTTOM": f"{BASE_PATH}go-bottom.png",
  "GO_NEXT": f"{BASE_PATH}go-next.png",
  "GO_PREVIOUS": f"{BASE_PATH}go-previous.png",
  "NINJA_LOGO": f"{BASE_PATH}ninja-logo.png",
  "PROCESS_STOP": f"{BASE_PATH}process-stop.png",
  "TEXT_HTML": f"{BASE_PATH}text-html.png",
  "VIEW_REFRESH": f"{BASE_PATH}view-refresh.png",
  "APP_NAME": APP_NAME,
  "APP_NAME_LOWER": APP_NAME.lower().replace(" ", "-"),
  "START_PAGE": "https://duckduckgo.com",
  "AUTHOR": "Souvlaki42",
}
