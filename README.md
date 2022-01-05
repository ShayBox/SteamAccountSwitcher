# SteamAccountSwitcher

Qt Steam account switcher for linux

![](screenshot.png)

[AUR](https://aur.archlinux.org/packages/steamaccountswitcher-git)

### Build & Install
`killall` is a required runtime dependency
```
git clone https://github.com/ShayBox/SteamAccountSwitcher.git
cd SteamAccountSwitcher
poetry build
pip install --user dist/*.tar.gz

steamswitcher
```

### Development
`poetry` is a required build dependency (build tool)
```
git clone https://github.com/ShayBox/SteamAccountSwitcher.git
cd SteamAccountSwitcher
poetry env use <python3 executable>

poetry run steamswitcher-dev
```

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