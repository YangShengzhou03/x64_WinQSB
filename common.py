import os
import sys

from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices


def open_reading():
    QDesktopServices.openUrl(QUrl('https://blog.csdn.net/Yang_shengzhou/article/details/142312570'))


def load_stylesheet(filename):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, 'resources', 'stylesheet', filename)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"文件 {filename} 未找到。"


def get_resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path).replace(os.sep, '/')
