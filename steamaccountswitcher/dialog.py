from PySide6.QtCore import QSettings
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QMenu, QSystemTrayIcon
from steamaccountswitcher.ui.dialog import Ui_Dialog
import logging, os, re, subprocess


class Dialog(QDialog, Ui_Dialog):
    def __init__(self) -> None:
        super().__init__()

        logging.info("Setting up Dialog UI")
        self.setupUi(self)

        logging.info("Initializing QSettings")
        self.settings = QSettings("ShayBox", "SteamAccountSwitcher")

        logging.info("Setting window icon")
        self.set_window_icon()

        logging.info("Populating accounts")
        self.populate_accounts()

        logging.info("Initializing QSystemTrayIcon")
        self.init_tray()

        logging.info("Connecting buttons")
        self.connect_buttons()

        logging.info("Showing QSystemTrayIcon")
        self.tray.show()

    def set_window_icon(self) -> None:
        icon = self.settings.value("icon", None)
        icon = QIcon(icon) if isinstance(icon, QIcon) else QIcon.fromTheme(icon)
        if icon:
            self.setWindowIcon(icon)

    def populate_accounts(self) -> None:
        # Clear accounts in-case of a cancel repopulation
        self.accountsBox.clear()

        # Populate accounts from settings
        accounts = self.settings.value("accounts", [])
        accounts = accounts if isinstance(accounts, list) else []
        for account in accounts:
            logging.info(f"Adding account {account}")
            self.accountsBox.addItem(account)

        # Select the previously selected account
        account = self.settings.value("account", "")
        self.accountsBox.setCurrentText(account)

    def init_tray(self) -> None:
        self.tray = QSystemTrayIcon(self.windowIcon(), self)
        self.menu = QMenu()
        self.tray.activated.connect(self.show)
        self.menu.addAction("Show", self.show)
        self.menu.addSeparator()
        self.menu.addSection("Accounts")

        def login(account: str) -> None:
            self.accountsBox.setCurrentText(account)
            self.loginButton.click()

        for i in range(self.accountsBox.count()):
            account = self.accountsBox.itemText(i)
            self.menu.addAction(account, lambda: login(account))

        self.menu.addSeparator()
        self.menu.addAction("Quit", self.close)
        self.tray.setContextMenu(self.menu)
        self.tray.setToolTip("Steam Account Switcher")

    def connect_buttons(self) -> None:
        self.addButton.clicked.connect(self.action_add_account)
        self.removeButton.clicked.connect(self.action_remove_account)
        self.loginButton.clicked.connect(self.action_login_account)

    def action_add_account(self) -> None:
        account = self.accountEdit.text()
        if account:
            logging.info(f"Adding account {account}")
            self.accountsBox.addItem(account)
            self.accountEdit.clear()

    def action_remove_account(self) -> None:
        account = self.accountsBox.currentText()
        if account:
            logging.info(f"Removing account {account}")
            self.accountsBox.removeItem(self.accountsBox.currentIndex())

    def action_login_account(self) -> None:
        logging.info("Logging in")

        logging.info("Killing steam")
        kill_cmd = "killall --quiet --wait steam"
        kill_cmd = self.settings.value("kill", kill_cmd)
        os.system(kill_cmd)

        registry = os.path.expanduser("~") + "/.steam/registry.vdf"
        registry = self.settings.value("registry", registry)
        logging.info(f"Modifying registry {registry}")
        with open(registry, "r+") as f:
            txt = self.accountsBox.currentText()
            exp = '("AutoLoginUser"[	| ]+")\w+(")'
            sub = f"\g<1>{txt}\g<2>"
            text = f.read()
            text = re.sub(exp, sub, text, flags=re.MULTILINE)
            f.seek(0)
            f.write(text)
            f.truncate()

        logging.info("Launching steam")
        steam_cmd = "steam"
        steam_cmd = self.settings.value("steam", steam_cmd)
        subprocess.Popen([steam_cmd], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        self.accept()

    def accept(self) -> None:
        logging.info("Saving accounts")
        self.settings.setValue(
            "accounts",
            [self.accountsBox.itemText(i) for i in range(self.accountsBox.count())],
        )
        self.settings.setValue("account", self.accountsBox.currentText())
        self.hide()

    def reject(self) -> None:
        logging.info("Cancelling, repopulating accounts")
        self.populate_accounts()
        self.hide()
