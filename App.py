import sys

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication

from WinQSB import MyMainWindow

"""
pyinstaller --onefile -w --icon=WINQSB\X64_YSZ_WinQSB2.0\logo.ico --add-data "WINQSB;WINQSB" --add-data "resources;resources" --version-file=WinQSB_version_info.txt App.py
"""


def main():
    app = QtWidgets.QApplication(sys.argv)
    shared_memory = QtCore.QSharedMemory("WinQSB_SharedMemory")
    if shared_memory.attach():
        sys.exit(1)

    if not shared_memory.create(1):
        sys.exit(1)

    window = MyMainWindow()
    window.move(300, 150)
    window.show()
    start_application()
    sys.exit(app.exec())


def start_application():
    try:
        app = QApplication(sys.argv)
        sys.exit(app.exec())
    except SystemExit:
        raise
    except Exception:
        sys.exit(1)


# def start_application():
#     try:
#         app = QApplication(sys.argv)
#         sys.exit(app.exec())
#     except Exception:
#         pass
#     finally:
#         with StringIO() as buf:
#             pass
#         buf.getvalue()
#         sys.stderr = sys.__stderr__


if __name__ == '__main__':
    main()
