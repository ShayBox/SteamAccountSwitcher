from pathlib import Path
from PySide6.QtWidgets import QApplication
from steamaccountswitcher.dialog import Dialog
import logging, os, signal, subprocess, sys

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)


def main() -> None:
    logging.info("Forking process to run in background")
    subprocess.Popen(["steamswitcher-gui"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def dev() -> None:
    logging.info("Converting .ui files to .py files")
    os.chdir("steamaccountswitcher/ui")
    for path in Path().glob("*.ui"):
        ui = path.name
        py = path.name.replace(".ui", ".py")
        logging.info(f"Generating {py} from {ui}")
        os.system(f"pyside6-uic {ui} -o {py}")

    logging.info("Running main()")
    gui()


def gui() -> None:
    logging.info("Registering SIGINT handler")
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    logging.info("Initializing QApplication and QDialog")
    app = QApplication()
    Dialog()

    logging.info("Executing QApplication")
    sys.exit(app.exec())
