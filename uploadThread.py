import time

import crcmod
import math
import datetime
import serial
import binascii
import os
import re
from collections import OrderedDict
import serial.tools.list_ports
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSettings, QThread, pyqtSlot, pyqtSignal
from uploadUi import Ui_uploadBin


class mainWindowUi(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.read_path = ""
        self.settings = QSettings("./uploadConfig.ini", QSettings.IniFormat)
        self.ui = Ui_uploadBin()
        self.ui.setupUi(self)
        self.serial = None
        self.i_com = 0
        self.com = ""
        self.port = 512000
        self.send_interval = 10
        self.send_pack_len = 4096

        self.ui.pushButton_enum_com.clicked.connect(self.enum_com)
        self.ui.pushButton_link_com.clicked.connect(self.link_com)
        self.ui.pushButton_choose_file_path.clicked.connect(self.choose_file_path)
        self.ui.pushButton_send.clicked.connect(self.send_thread)
        self.ui.pushButton_set_param.clicked.connect(self.set_send_interval_pack_len)
        self.i_send_thread = 0
        self.myThread = my_thread()
        self.ui.pushButton_receive.clicked.connect(self.receive_thread)
        self.myReceiveThread = my_receive_thread()
        self.i_receive_thread = 0

        self.myThread.send_end.connect(self.deal_with_send_end)
        self.myThread.send_text_signal.connect(self.print_str)
        self.myThread.send_progressbar_value.connect(self.update_progressBar)

        self.myReceiveThread.receive_end.connect(self.deal_with_receive_end)
        self.myReceiveThread.receive_text_signal.connect(self.print_receive_str)

        self.ui.pushButton_emit_send.clicked.connect(self.emit_send)

        self.read_settings()
        self.enum_com()

    def init_settings(self):
        self.settings.setValue("CONFIG/READ_PATH", "C://tanway")
        self.settings.setValue("CONFIG/INTERVAL", "50")
        self.settings.setValue("CONFIG/PACK_LEN", "4096")
        self.settings.setValue("CONFIG/PORT", "512000")
        self.settings.setValue("FILENAME/C2301", "C2301_BOOT_Ver_1_0_1.BIN")
        self.settings.setValue("FILENAME/C2302", "C2302_BOOT_Ver_1_0_1.BIN")
        self.settings.setValue("FILENAME/FOC", "FOC_BOOT_Ver_1_0_1.BIN")
        self.settings.setValue("FILENAME/TempoA4", "image.ub")

    def read_settings(self):
        if not os.path.exists("./uploadConfig.ini"):
            self.print_str("创建初始化配置文件: " + self.settings.fileName())
            self.init_settings()
        try:
            self.read_path = self.settings.value("CONFIG/READ_PATH")
            self.send_interval = int(self.settings.value("CONFIG/INTERVAL"))
            self.send_pack_len = int(self.settings.value("CONFIG/PACK_LEN"))
            self.port = int(self.settings.value("CONFIG/PORT"))
            self.myThread.interval = self.send_interval / 1000
            self.myThread.pack_len = self.send_pack_len
            self.ui.lineEdit_file_path.setText(self.read_path)
            self.ui.lineEdit_interval.setText(str(self.send_interval))
            self.ui.lineEdit_pack_len.setText(str(self.send_pack_len))
            self.ui.lineEdit_port.setText(str(self.port))
            #  读配置
            all_keys = self.settings.allKeys()
            filename_dict = OrderedDict()
            for key in all_keys:
                if key.startswith("FILENAME/"):
                    filename = key.replace(" ", "").split('/')
                    value = self.settings.value(key)
                    filename_dict.update({filename[-1]: value})
            self.myThread.filename_dict = filename_dict

        except Exception as e:
            self.print_str("读取参数不存在，重新生成配置文件")
            self.init_settings()
            self.read_settings()

    def write_settings(self):
        self.settings.setValue("CONFIG/READ_PATH", self.read_path)
        self.settings.setValue("CONFIG/INTERVAL", str(self.send_interval))
        self.settings.setValue("CONFIG/PACK_LEN", str(self.send_pack_len))
        self.settings.setValue("CONFIG/PORT", str(self.port))

    def set_send_interval_pack_len(self):
        self.send_interval = int(self.ui.lineEdit_interval.text())
        self.myThread.interval = self.send_interval / 1000
        self.send_pack_len = int(self.ui.lineEdit_pack_len.text())
        self.myThread.pack_len = int(self.send_pack_len)
        self.port = int(self.ui.lineEdit_port.text())
        self.print_str("设置发送时间间隔为：" + str(self.myThread.interval) + "s")
        self.print_str("设置发送每帧数据长度为：" + str(self.myThread.pack_len) + "s")

    def enum_com(self):
        comList = list(serial.tools.list_ports.comports())

        if len(comList) != 0:
            self.ui.comboBox_com.clear()
            for i in comList:
                self.ui.comboBox_com.addItem(str(i.device))
            self.print_str("当前端口为 " + str(comList[0].device))
        else:
            self.ui.comboBox_com.setCurrentIndex(-1)
            self.print_str("无法找到端口")

    def set_com(self):
        com_data = self.ui.comboBox_com.currentText()
        self.print_str("当前端口为 " + str(com_data))
        self.com = com_data

    def link_com(self):
        self.set_com()
        if self.i_com == 0:
            try:
                self.serial = serial.Serial(self.com, self.port, timeout=1)
                if self.serial.is_open:
                    self.myThread.serial = self.serial
                    self.myReceiveThread.serial = self.serial
                    self.i_com = 1
                    self.print_str("串口连接成功")
                    self.ui.pushButton_link_com.setText("取消连接")
            except Exception as e:
                self.print_str("串口连接失败")
                self.print_str(str(e))
        else:
            if self.serial and self.serial.isOpen():
                self.serial.close()
                self.myThread.serial = None
                self.myReceiveThread.serial = None
                self.ui.pushButton_link_com.setText("连接串口")
                self.print_str("串口已断开连接")
                self.i_com = 0

    def choose_file_path(self):
        file_dialog = QFileDialog(self)
        # file_path, _ = file_dialog.getOpenFileNames(self, "选择上传文件", "", "Binary Files (*.bin)")
        file_path = file_dialog.getExistingDirectory(None, "选择文件夹", "/")
        if file_path:
            self.read_path = file_path
            self.ui.lineEdit_file_path.setText(file_path)
            str1 = "选择的烧录文件路径为：" + file_path
            self.print_str(str1)

    def send_thread(self):
        if self.i_send_thread == 0:
            if self.read_path is None:
                self.print_str("请选择文件路径")
                return
            if not os.path.exists(self.read_path):
                self.print_str("该路径文件不存在")
                return
            self.myThread.path = self.read_path
            self.ui.plainTextEdit_send.clear()
            self.ui.pushButton_send.setText("停止上传")
            self.control_send(1, 0)
            self.i_send_thread = 1
            self.myThread.i_send_thread = 1
            self.myThread.start()
        else:
            self.ui.pushButton_send.setText("烧录文件发送")
            self.control_send(1, 1)
            self.i_send_thread = 0
            self.myThread.i_send_thread = 0
            self.myThread.terminate()
            self.myThread.wait()
            self.myThread.quit()

    def control_send(self, control, status):
        if control == 0:
            self.ui.groupBox_burn.setEnabled(status)
            # self.ui.pushButton_send.setEnabled(status)
        else:
            self.ui.groupBox_debug.setEnabled(status)
            # self.ui.pushButton_emit_send.setEnabled(status)
            # self.ui.plainTextEdit_emit_send.setEnabled(status)

    @pyqtSlot(int)
    def update_progressBar(self, value):
        self.ui.progressBar.setValue(value)

    @pyqtSlot()
    def deal_with_send_end(self):
        self.ui.pushButton_send.setText("烧录文件发送")
        self.control_send(1, 1)
        self.i_send_thread = 0
        self.myThread.i_send_thread = 0
        self.myThread.terminate()
        self.myThread.wait()
        self.myThread.quit()

    def receive_thread(self):
        if self.i_receive_thread == 0:
            self.myThread.path, self.myThread.name = os.path.split(self.read_path)
            self.ui.pushButton_receive.setText("停止接收")
            self.myReceiveThread.start()
            self.i_receive_thread = 1
            self.myReceiveThread.i_receive_thread = 1
        else:
            self.myReceiveThread.i_receive_thread = 0
            self.ui.plainTextEdit_receive.clear()
            self.ui.pushButton_receive.setText("开始接收")
            self.myReceiveThread.terminate()
            self.myReceiveThread.wait()
            self.myReceiveThread.quit()
            self.i_receive_thread = 0

    @pyqtSlot()
    def deal_with_receive_end(self):
        self.myReceiveThread.i_receive_thread = 0
        self.ui.pushButton_receive.setText("开始接收")
        self.ui.pushButton_receive.setEnabled(1)
        self.myReceiveThread.terminate()
        self.myReceiveThread.wait()
        self.myReceiveThread.quit()
        self.i_receive_thread = 0

    def emit_send(self):
        if self.serial is None:
            self.print_str("串口尚未连接")
            return

        def is_hex_string(s):
            return bool(re.match(r'^[0-9a-fA-F]+$', s))

        self.control_send(0, 0)
        data = str(self.ui.plainTextEdit_emit_send.toPlainText())
        data = data.replace(" ", "").replace("\n", "")
        if data != "":
            if len(data) % 2 != 0:
                data = "0" + data

            if is_hex_string(data):
                str1 = "发：" + str(data)
                data = binascii.a2b_hex(data)
                self.serial.write(data)
                self.print_receive_str(str1)
            else:
                self.print_receive_str("发送数据有错")
        self.ui.plainTextEdit_emit_send.clear()
        self.control_send(0, 1)

    @pyqtSlot(str)
    def print_str(self, text):
        currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.ui.plainTextEdit_send.appendPlainText(currentTime + " " + str(text))

    @pyqtSlot(str)
    def print_receive_str(self, text):
        currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.ui.plainTextEdit_receive.appendPlainText(currentTime + " " + str(text))

    def closeEvent(self, event):
        self.write_settings()


class my_thread(QThread):
    send_end = pyqtSignal()
    send_text_signal = pyqtSignal(str)
    send_progressbar_value = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.serial = None
        self.name = None
        self.path = None
        self.filename_dict = {}
        self.file_list = []
        self.frame_head = bytes([0xBB])
        self.head_info = None
        self.frame_version = 0
        self.interval = 0.05
        self.i_send_thread = 0
        self.pack_len = 4096

    def calculate_crc(self, data):
        crc32 = crcmod.predefined.Crc('crc-32')
        crc32.update(data)
        crc_value = crc32.crcValue
        return crc_value

    def read_bin(self, file_path_name):
        with open(file_path_name, "rb") as f:
            data = f.read()
        return data

    def deal_with_bin(self, file_path_name, frame_version, frame_file_no):
        frame_info = []
        frame_header = bytes([0xAA])
        frame_end = bytes([0x16])

        file_data = self.read_bin(file_path_name)
        file_len = len(file_data)
        if file_len == 0:
            return frame_info

        pack_len = self.pack_len
        pack_num = math.floor(file_len / pack_len)
        last_pack_len = file_len % pack_len

        for i in range(pack_num):
            data_len = pack_len.to_bytes(2, 'big')
            idx = i
            frame_no = (idx + 1).to_bytes(4, 'big')
            tmp_data = file_data[idx * pack_len: idx * pack_len + pack_len]
            crc = self.calculate_crc(tmp_data).to_bytes(4, 'big')
            data = frame_header + frame_version + frame_file_no + data_len + frame_no + tmp_data + crc + frame_end
            frame_info.append(data)

        if last_pack_len != 0:
            data_len = last_pack_len.to_bytes(2, 'big')
            frame_no = (pack_num + 1).to_bytes(4, 'big')
            tmp_data = file_data[pack_num * pack_len:]
            crc = self.calculate_crc(tmp_data).to_bytes(4, 'big')
            data = frame_header + frame_version + frame_file_no + data_len + frame_no + tmp_data + crc + frame_end
            frame_info.append(data)

        return frame_info

    def determine_file_name(self, file_path, filename_dict):
        pathname = file_path.split("/")[-1].upper()
        idx = 0
        file_list = []
        frame_version = bytes([0x00])
        for key, value in filename_dict.items():
            model_name = key.upper()
            idx = idx + 1
            if model_name in pathname:
                self.send_text_signal.emit("预烧录文件名：" + value)
                file_list = (value.split("&"))
                frame_version = idx.to_bytes(1, 'big')
                break

        return file_list, frame_version

    def run(self):
        if self.serial is None:
            self.send_text_signal.emit("串口尚未连接")
            self.send_end.emit()
            return
        self.send_text_signal.emit("串口通讯成功")

        self.file_list, self.frame_version = self.determine_file_name(self.path, self.filename_dict)

        if self.frame_version == bytes([0x00]) or len(self.file_list) == 0:
            self.send_text_signal.emit("请检查烧录文件路径和配置文件")
            self.send_end.emit()
            return

        all_file_dict = {}
        for item in os.listdir(self.path):
            item_path = os.path.join(self.path, item)
            if os.path.isfile(item_path):
                all_file_dict[item] = item_path

        upload_file_path = [(all_file_dict[file_name], 1 + idx) for idx, file_name in enumerate(self.file_list) if
                            file_name in all_file_dict]

        if len(upload_file_path) == 0:
            self.send_text_signal.emit("请检查烧录文件路径和配置文件")
            self.send_end.emit()
            return

        for i in range(len(upload_file_path)):
            file_no = upload_file_path[i][1].to_bytes(1, 'big')
            send_head_info = self.frame_head + self.frame_version + file_no
            self.serial.write(send_head_info)
            time.sleep(self.interval)

            file_path_name = upload_file_path[i][0]
            str1 = "即将烧录文件: " + str(upload_file_path[i][1]) + " , " + file_path_name.split('\\')[-1]
            self.send_text_signal.emit(str1)
            frame_info = self.deal_with_bin(file_path_name, self.frame_version, file_no)
            if len(frame_info) == 0:
                self.send_text_signal.emit("烧录文件异常，请检查: " + file_path_name)
                self.send_end.emit()
                return

            for j in range(len(frame_info)):
                self.serial.write(frame_info[j])
                if self.serial.in_waiting > 0:
                    value = self.serial.readline()
                    data = ''.join('{:02x}'.format(byte) for byte in value).upper()
                    if data in "0B0C0B0C":
                        str1 = "发送数据校验错误：" + data
                        self.send_text_signal.emit(str1)
                        self.i_send_thread = 0
                tmp_value = int((100 * (j+1) / len(frame_info)))
                self.send_progressbar_value.emit(tmp_value)
                time.sleep(self.interval)
                if self.i_send_thread == 0:
                    self.send_text_signal.emit("停止发送串口数据")
                    self.send_end.emit()
                    return
        self.send_text_signal.emit("**发送串口数据完成**")
        self.send_end.emit()


class my_receive_thread(QThread):
    receive_end = pyqtSignal()
    receive_text_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.serial = None
        self.i_receive_thread = 0

    def run(self):
        if self.serial is None:
            self.receive_text_signal.emit("串口尚未连接")
            self.receive_end.emit()
            return

        self.receive_text_signal.emit("开始读取串口数据")
        while self.i_receive_thread:
            if self.serial.in_waiting > 0:
                data = ''.join('{:02x}'.format(byte) for byte in self.serial.readline()).upper()
                str1 = "收：" + str(data)
                self.receive_text_signal.emit(str1)

        self.receive_text_signal.emit("读取串口数据结束")
        self.send_end.emit()
