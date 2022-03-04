# Built-in modules
import faulthandler
import logging
import signal
import subprocess
import sys

# Third-party modules
import click
from qtpy.QtWidgets import QApplication

# Local modules
from steamaccountswitcher.dialog import MainWindow


@click.command()
@click.option("-v", "--verbose", is_flag=True, help="Enable verbose mode")
@click.option("-b", "--background", is_flag=True, help="Run in background")
def main(verbose: bool = False, background: bool = False) -> None:
    logging.basicConfig(level=logging.DEBUG if verbose else logging.WARNING)

    if background:
        logging.debug("Running in background")
        subprocess.Popen(["steamswitcher"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        exit(0)

    logging.debug("Enabled built-in python fault handler for segfaults")
    faulthandler.enable()

    logging.info("Registering SIGINT handler")
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    logging.info("Initializing QApplication and QDialog")
    app = QApplication(sys.argv)
    MainWindow()

    logging.info("Executing QApplication")
    sys.exit(app.exec())
