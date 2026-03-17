# SeedSigner localization (experiment)

This branch includes seedsigner localization experiment. As an example, I added Korean localization updates, but other foreign languages can also be added later.

Language can be changed in Settings/Advanced/Langugage setting and the settings will be stored in settings.json which is default setting file of seedsigner.

![Image of Settings](img/loc/settings-en.jpg)

New menu "Language" will be shown in Advanced settings:

![Image of Advanced Settings](img/loc/settings-en-adv.jpg)

Language change will require system rebooting and its warning message will be shown as below. (Since the Language setting will be stored in Settings.json file in SD card, if Persistent Settings option is disabled, it will show 'Persistent required' warning screen and will go back to Advanced Settings screen.)

![Image of Reboot Required](img/loc/settings-en-reboot-req.jpg)

![Image of Language Setting](img/loc/settings-en-lang.jpg)

If language is changed, Reboot/PowerOff screen will be shown without Back button: 

![Image of Reboot](img/loc/settings-en-reboot.jpg)


### Localization approach
This localization experiment is using GNU gettext API and its localization files are located under src/seedsigner/locales/ folder.

I wanted to minimize the code changes and achieve localization simultaneously, which led me to make a trade-off by giving up the runtime Language setting. So when language is changed, system reboot is required.

### How to localize other language
In order to localize other languages, typically one can follow the steps below:
1. Create a new folder for the language under in src/seedsigner/locales/{LANG}/LC_MESSAGES. 
For example, to add Spanish, create a folder named src/seedsigner/locales/es/LC_MESSAGES. 
2. Copy src/seedsigner/locales/seedsigner.pot to LC_MESSAGES folder and rename it to seedsigner.po.
3. Edit seedsigner.po file and translate text. It will be easier if you use .po edit tool such as Poedit. Poedit will compile .po file to .mo file when saved.
4. If you need to add other fonts for foreign language, add them to src/seedsigner/resources/fonts and update get_locale_font() in src/seedsigner/gui/components.py.


# Korean version of SeedSigner

As a localization example, there is a Korean translation in src/seedsigner/locales/ko/LC_MESSAGES folder. 

Here are some UI samples of Korean localization.

Main Menu:
![Image of Korean Home](img/loc/home-ko.jpg)

Settings:
![Image of Korean Settings](img/loc/settings-ko.jpg)

Settings/Advanced:
![Image of Korean Advanced Settings](img/loc/settings-ko-adv.jpg)

Reboot required: 
![Image of Korean Reboot Required](img/loc/settings-ko-reboot-req.jpg)

Language setting:
![Image of Korean Language Setting](img/loc/settings-ko-lang.jpg)

![Image of Korean Reboot](img/loc/settings-ko-reboot.jpg)

