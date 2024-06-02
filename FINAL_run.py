"""FINAL_run.py.

install/update dependencies if needed
"""
import subprocess
import sys


def install(package):
    """Installs latest version of easyGUI if not already installed"""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install('easygui')
