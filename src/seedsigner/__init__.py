import os
import json
import gettext

# set locale
_settings_json = "/mnt/microsd/settings.json" if os.uname()[1] == "seedsigner-os" else "settings.json"
_lang = "en"
if os.path.exists(_settings_json):
    with open(_settings_json) as settings_file:
        _dict = json.load(settings_file)
        _lang = _dict["language"]

_localedir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'locales/')
_translations = gettext.translation('seedsigner', localedir=_localedir, fallback=True, languages=[_lang])
_translations.install()
_ = _translations.gettext

os.environ["LANG"] = _lang
print(f"Language: {_lang}")
