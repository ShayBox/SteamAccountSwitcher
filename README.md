# SteamAccountSwitcher

Qt Steam account switcher

![](screenshot.png)

[AUR](https://aur.archlinux.org/packages/steamaccountswitcher-git)

#### Build & Install
```
git clone https://github.com/ShayBox/SteamAccountSwitcher.git
cd SteamAccountSwitcher
poetry build
pip install --user dist/*.tar.gz

steamswitcher
```

#### Development
```
git clone https://github.com/ShayBox/SteamAccountSwitcher.git
cd SteamAccountSwitcher
poetry env use <python3 executable>

poetry run steamswitcher-dev
```