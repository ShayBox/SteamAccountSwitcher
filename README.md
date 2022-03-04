# SteamAccountSwitcher

Qt 5/6 Steam account switcher for linux

![Screenshot](screenshot.png)

[AUR](https://aur.archlinux.org/packages/steamaccountswitcher-git)

#### Installation
Requirements:
- [Python] 3.7 or later
- PyQt5 or PyQt6
```
$ pip install --user pyqt5
$ pip install --user git+https://github.com/shaybox/steamaccountswitcher.git

$ steamswitcher
```

### Development
Requirements:
- [Python] 3.7 or later
- [Poetry] via pip
- [PyQt5] or [PyQt6]
```
git clone https://github.com/ShayBox/SteamAccountSwitcher.git
cd SteamAccountSwitcher
poetry env use <python3 executable>

$ poetry run steamswitcher
```

#### Usage
There's icon and desktop entry files in the `data` directory.  
Run the command `steamswitcher -b` to start the tray icon.  
Run the command `steamswitcher --help` to see the command line options.

### Configuration
SteamAccountSwitcher uses [QSettings](https://doc.qt.io/qt-6/qsettings.html#locations-where-application-settings-are-stored)  
The default location for the config is `~/.config/ShayBox/SteamAccountSwitcher.conf`  
This is generated after you click Save in the main dialog window  

#### Example config:
```
[General]
account=account1
accounts=account1, account2
; Additional settings that don't get populated by default
icon=steam
kill=killall --quiet --wait steam
registry=/home/<user>/.steam/registry.vdf
steam=steam
```
`icon` is the icon used, uses QIcon then QIcon.fromTheme  
`kill` is the command used to kill steam  
`registry` is the location to steams registry.vdf, must be a full path  
`steam` is the steam executable that is launched  

[Python]: https://python.org
[Poetry]: https://python-poetry.org
[PyQt5]: https://pypi.org/project/PyQt5
[PyQt6]: https://pypi.org/project/PyQt6