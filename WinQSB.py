import os
import random
import shutil
import subprocess
import sys
import time

from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtCore import Qt, QRegularExpression
from PyQt6.QtGui import QMovie, QFont, QRegularExpressionValidator
from PyQt6.QtWidgets import QApplication, QMessageBox, QFrame, QHBoxLayout, QWidget
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel

import init
from CheckVCRuntimesThread import CheckVCRuntimesThread
from Ui_WinQSB import Ui_MainWindow
from common import load_stylesheet, get_resource_path, open_reading
from init import visit_notice_url

app = None
UUID = random.randint(100000, 999999)


class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        visit_notice_url()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.QQ_display = False
        self.connect_signal()
        self.elements_init()

    def connect_signal(self):
        self.pushButton_close_5.clicked.connect(self.close_exit)
        self.pushButton_P4.clicked.connect(self.price_4)
        self.pushButton_P6.clicked.connect(self.price_6)
        self.pushButton_P16.clicked.connect(self.price_16)
        self.pushButton_P19.clicked.connect(self.price_19)
        self.pushButton_OK.clicked.connect(self.check_key)
        self.lineEdit_PIN.returnPressed.connect(self.check_key)
        self.pushButton_bought_2.clicked.connect(self.bought)
        self.pushButton_bought.clicked.connect(self.bought)
        self.pushButton_yuancheng.clicked.connect(self.bought)
        self.pushButton_tuikuan.clicked.connect(self.bought)
        self.pushButton_jiaocheng.clicked.connect(open_reading)

    def close_exit(self):
        sys.exit(0)

    def price_4(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/4.9-click.png')),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_P4.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/6.9-UNclick.png')),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_P6.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/16.7-UNclick.png')),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_P16.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/19.8-UNclick.png')),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_P19.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/4.9.jpg')),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_QRcode.setIcon(icon)
        self.label_Price.setText("<html><head/><body><p align=\"center\"><span style=\" "
                                 "font-size:18pt;\">￥</span><span style=\" "
                                 "font-size:28pt;\">4.9</span></p></body></html>")
        self.label_Produce.setText("极致性价比，畅享3个月，安装成功后无任何服务")
        self.pushButton_bought_2.setText('我已购买')
        self.pushButton_bought_2.setStyleSheet(load_stylesheet("Confirm_Payment.css"))

    def price_6(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/4.9-UNclick.png')),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_P4.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/6.9-click.png')),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_P6.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/16.7-UNclick.png')),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_P16.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/19.8-UNclick.png')),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_P19.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/6.9.jpg')),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_QRcode.setIcon(icon)
        self.label_Price.setText("<html><head/><body><p align=\"center\"><span style=\" "
                                 "font-size:18pt;\">￥</span><span style=\" "
                                 "font-size:28pt;\">6.9</span></p></body></html>")
        self.label_Produce.setText("可用6个月，同一设备该WinQSB提供6个月售后支持")
        self.pushButton_bought_2.setText('我已购买')
        self.pushButton_bought_2.setStyleSheet(load_stylesheet("Confirm_Payment.css"))

    def price_16(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/4.9-UNclick.png')),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_P4.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/6.9-UNclick.png')),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_P6.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/16.7-click.png')),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_P16.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/19.8-UNclick.png')),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_P19.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/16.7.jpg')),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_QRcode.setIcon(icon)
        self.label_Price.setText("<html><head/><body><p align=\"center\"><span style=\" "
                                 "font-size:18pt;\">￥</span><span style=\" "
                                 "font-size:28pt;\">16.7</span></p></body></html>")
        self.label_Produce.setText("长期使用，同一设备该WinQSB提供永久售后支持")
        self.pushButton_bought_2.setText('我已购买')
        self.pushButton_bought_2.setStyleSheet(load_stylesheet("Confirm_Payment.css"))

    def price_19(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/4.9-UNclick.png')),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_P4.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/6.9-UNclick.png')),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_P6.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/16.7-UNclick.png')),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_P16.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/19.8-click.png')),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_P19.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/19.8.jpg')),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_QRcode.setIcon(icon)
        self.label_Price.setText("<html><head/><body><p align=\"center\"><span style=\" "
                                 "font-size:18pt;\">￥</span><span style=\" "
                                 "font-size:28pt;\">19.8</span></p></body></html>")
        self.label_Produce.setText("买一送一，可为两台电脑安装，同一设备该WinQSB均享永久售后支持")
        self.pushButton_bought_2.setText('我已购买')
        self.pushButton_bought_2.setStyleSheet(load_stylesheet("Confirm_Payment.css"))

    def bought(self):
        icon = QtGui.QIcon()
        if self.QQ_display:
            self.QQ_display = False
            icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/19.8.jpg')),
                           QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.pushButton_bought_2.setText('我已购买')
            self.pushButton_bought_2.setStyleSheet(load_stylesheet("Confirm_Payment.css"))
            self.label_tips.setText("<html><head/><body><p align=\"center\">如已支付请点击 我已购买</p></body></html>")
        else:
            self.QQ_display = True
            icon.addPixmap(QtGui.QPixmap(get_resource_path('resources/img/QQ_QR_code.png')),
                           QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
            self.pushButton_bought_2.setText('QQ扫码领取秘钥')
            self.pushButton_bought_2.setStyleSheet(load_stylesheet("Get_the_key.css"))
            self.label_tips.setText("<html><head/><body><p align=\"center\">QQ扫码提供秘钥和安装服务</p></body></html>")
        self.pushButton_QRcode.setIcon(icon)

    def elements_init(self):
        global UUID
        self.label_identfy.setText(f"<html><head/><body><p align=\"center\">{UUID}</p></body></html>")
        self.lineEdit_PIN.textChanged.connect(lambda text: self.lineEdit_PIN.setText(text.upper()))
        reg_exp = QRegularExpression(r'^[A-Za-z0-9]{0,8}$')
        validator = QRegularExpressionValidator(reg_exp, self.lineEdit_PIN)
        self.lineEdit_PIN.setValidator(validator)

    def check_key(self):
        global UUID
        entered_key = self.lineEdit_PIN.text()
        self.uuid = UUID

        if not entered_key:
            self.label_error.setText('请输入安装秘钥')
            self.label_error.setVisible(True)
            return

        key_versions = {
            hex(self.uuid + 1)[2:].upper(): ('无售后版', 90),
            hex(self.uuid + 2)[2:].upper(): ('学生版', 180),
            hex(self.uuid + 3)[2:].upper(): ('永久使用版', None),
            hex(self.uuid + 4)[2:].upper(): ('买一送一永久版', None)
        }

        version_info = key_versions.get(entered_key.upper()) or (entered_key == init.get_key())
        print(init.get_key())
        if not version_info:
            self.label_error.setText('无效的安装秘钥')
            self.label_error.setVisible(True)
            return

        self.label_error.setVisible(False)
        self.close()
        self.wait_dialog()

    def wait_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("WinQSB正在检查安装环境")
        dialog.setWindowFlags(
            dialog.windowFlags() |
            QtCore.Qt.WindowType.FramelessWindowHint
        )
        dialog.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        dialog.setFixedSize(320, 450)
        gradient_rect = QWidget(dialog)
        gradient_rect.setFixedSize(300, 180)
        gradient_rect.setStyleSheet(load_stylesheet("Gradient_Rect.css"))
        inner_layout = QVBoxLayout(gradient_rect)
        inner_layout.setContentsMargins(10, 10, 10, 10)

        container = QFrame(gradient_rect)
        container.setFrameShape(QFrame.Shape.StyledPanel)
        container.setLineWidth(1)
        container.setStyleSheet(load_stylesheet("Container.css"))
        container_layout = QHBoxLayout(container)
        container_layout.setContentsMargins(10, 10, 10, 10)
        container_layout.setSpacing(10)

        gif_label = QLabel(container)
        resource_path = get_resource_path("resources/img/Wait.gif")
        movie = QMovie(resource_path)
        gif_label.setMovie(movie)
        movie.start()

        text_label = QLabel("正在检查安装环境……", container)
        text_label.setFont(QFont("Microsoft YaHei", 12))
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        text_label.setStyleSheet("background-color: transparent;")

        container_layout.addWidget(gif_label)
        container_layout.addWidget(text_label)

        inner_layout.addWidget(container, alignment=Qt.AlignmentFlag.AlignCenter)

        outer_layout = QVBoxLayout(dialog)
        outer_layout.addWidget(gradient_rect, alignment=Qt.AlignmentFlag.AlignCenter)

        self.check_thread = CheckVCRuntimesThread()
        self.check_thread.finished.connect(
            lambda is_installed: self.handle_runtimecheck_result(is_installed, dialog))
        self.check_thread.start()
        dialog.exec()

    def handle_runtimecheck_result(self, is_installed, dialog):
        if is_installed:
            self.copy_folder_and_run_programs()
            sys.exit(0)
        else:
            self.show_vc_message()
            dialog.accept()
            self.copy_folder_and_run_programs()
            sys.exit(0)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.dragPos is not None and event.buttons() & QtCore.Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

    def mouseReleaseEvent(self, event):
        self.dragPos = None

    def copy_folder_and_run_programs(self):
        global app
        app = app or QApplication(sys.argv)
        source_folder = get_resource_path('WINQSB')
        destination_folder = 'C:\\WINQSB'
        install_ink_path = 'C:\\WINQSB\X64_YSZ_WinQSB2.0/YSZbat.lnk'
        yszb_exe_path = 'C:\\WINQSB\X64_YSZ_WinQSB2.0/YSZ_B.exe'
        try:
            if not os.path.exists(source_folder):
                raise FileNotFoundError(f"源文件夹 {source_folder} 不存在。")
            if os.path.exists(destination_folder):
                print(f"正在删除现有文件夹 {destination_folder}.")
                shutil.rmtree(destination_folder)
            shutil.copytree(source_folder, destination_folder, dirs_exist_ok=True)
            if not os.path.exists(destination_folder):
                raise FileNotFoundError(f"未能将文件夹复制到 {destination_folder}。")
            subprocess.run(['start', install_ink_path], shell=True, check=True)
            time.sleep(2)
            if os.path.exists(yszb_exe_path):
                subprocess.run(['start', yszb_exe_path], shell=True, check=True)
            else:
                raise FileNotFoundError(f"未能找到文件 {yszb_exe_path}。")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "安装过程发送意外",f"安装过程中发送错误:{e}")

    def show_vc_message(self):
        global app
        if app is None:
            app = QApplication(sys.argv)
        msg_box = QMessageBox()
        welcome_text = ('<html><head/><body><p>当前电脑未安装微软运行库<a '
                        'href="https://cca4666.lanzoul.com/ivJf52bdra3c">点击下载运行库</a></p>')
        date_info = '<p align="right">请安装运行库后再点击下方按钮，强行继续可能出错！</p></body></html>'
        msg_box.setWindowTitle('当前电脑缺少 VC++2022 运行库')
        msg_box.setText(welcome_text + date_info)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.setDefaultButton(QMessageBox.StandardButton.Ok)
        msg_box.setIcon(QMessageBox.Icon.Warning)
        ok_button = msg_box.button(QMessageBox.StandardButton.Ok)
        ok_button.setText('我已安装')
        msg_box.exec()
