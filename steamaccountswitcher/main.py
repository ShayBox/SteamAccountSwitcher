from pathlib import Path
from PySide6.QtWidgets import QApplication
from steamaccountswitcher.dialog import Dialog
import logging, os, signal, subprocess, sys

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)


def main() -> None:
    subprocess.Popen(["steamswitcher-gui"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def dev() -> None:
    os.chdir("steamaccountswitcher/ui")
    for path in Path().glob("*.ui"):
        ui = path.name
        py = path.name.replace(".ui", ".py")
        logging.info(f"Generating {py} from {ui}")
        os.system(f"pyside6-uic {ui} -o {py}")
    gui()


def gui() -> None:
    logging.info("Registering SIGINT handler")
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    logging.info("Initializing QApplication and QDialog")
    app = QApplication()
    dialog = Dialog()

    logging.info("Executing QApplication")
    sys.exit(app.exec())
