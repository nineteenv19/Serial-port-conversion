# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uploadUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_uploadBin(object):
    def setupUi(self, uploadBin):
        uploadBin.setObjectName("uploadBin")
        uploadBin.resize(750, 850)
        uploadBin.setMinimumSize(QtCore.QSize(750, 850))
        uploadBin.setStyleSheet("QLineEdit { border: none; }\n"
"QPlainTextEdit{border: none; }")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(uploadBin)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_burn = QtWidgets.QGroupBox(uploadBin)
        self.groupBox_burn.setObjectName("groupBox_burn")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_burn)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_pack_len = QtWidgets.QLineEdit(self.groupBox_burn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_pack_len.sizePolicy().hasHeightForWidth())
        self.lineEdit_pack_len.setSizePolicy(sizePolicy)
        self.lineEdit_pack_len.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_pack_len.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pack_len.setObjectName("lineEdit_pack_len")
        self.gridLayout_2.addWidget(self.lineEdit_pack_len, 2, 4, 1, 1)
        self.lineEdit_interval = QtWidgets.QLineEdit(self.groupBox_burn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_interval.sizePolicy().hasHeightForWidth())
        self.lineEdit_interval.setSizePolicy(sizePolicy)
        self.lineEdit_interval.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_interval.setObjectName("lineEdit_interval")
        self.gridLayout_2.addWidget(self.lineEdit_interval, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_burn)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.plainTextEdit_send = QtWidgets.QPlainTextEdit(self.groupBox_burn)
        self.plainTextEdit_send.setReadOnly(True)
        self.plainTextEdit_send.setObjectName("plainTextEdit_send")
        self.gridLayout_2.addWidget(self.plainTextEdit_send, 5, 0, 1, 9)
        self.label_3 = QtWidgets.QLabel(self.groupBox_burn)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_burn)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 9)
        self.label_6 = QtWidgets.QLabel(self.groupBox_burn)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 3, 1, 1)
        self.pushButton_send = QtWidgets.QPushButton(self.groupBox_burn)
        self.pushButton_send.setObjectName("pushButton_send")
        self.gridLayout_2.addWidget(self.pushButton_send, 3, 6, 1, 3)
        self.label_7 = QtWidgets.QLabel(self.groupBox_burn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 5, 1, 1)
        self.pushButton_enum_com = QtWidgets.QPushButton(self.groupBox_burn)
        self.pushButton_enum_com.setObjectName("pushButton_enum_com")
        self.gridLayout_2.addWidget(self.pushButton_enum_com, 3, 0, 1, 1)
        self.pushButton_set_param = QtWidgets.QPushButton(self.groupBox_burn)
        self.pushButton_set_param.setObjectName("pushButton_set_param")
        self.gridLayout_2.addWidget(self.pushButton_set_param, 2, 8, 1, 1)
        self.lineEdit_port = QtWidgets.QLineEdit(self.groupBox_burn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_port.sizePolicy().hasHeightForWidth())
        self.lineEdit_port.setSizePolicy(sizePolicy)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.gridLayout_2.addWidget(self.lineEdit_port, 2, 6, 1, 2)
        self.lineEdit_file_path = QtWidgets.QLineEdit(self.groupBox_burn)
        self.lineEdit_file_path.setObjectName("lineEdit_file_path")
        self.gridLayout_2.addWidget(self.lineEdit_file_path, 0, 2, 2, 7)
        self.pushButton_choose_file_path = QtWidgets.QPushButton(self.groupBox_burn)
        self.pushButton_choose_file_path.setObjectName("pushButton_choose_file_path")
        self.gridLayout_2.addWidget(self.pushButton_choose_file_path, 0, 0, 2, 2)
        self.comboBox_com = QtWidgets.QComboBox(self.groupBox_burn)
        self.comboBox_com.setObjectName("comboBox_com")
        self.gridLayout_2.addWidget(self.comboBox_com, 3, 1, 1, 3)
        self.pushButton_link_com = QtWidgets.QPushButton(self.groupBox_burn)
        self.pushButton_link_com.setObjectName("pushButton_link_com")
        self.gridLayout_2.addWidget(self.pushButton_link_com, 3, 4, 1, 2)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(4, 1)
        self.gridLayout_2.setColumnStretch(6, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_burn)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout_2.addWidget(self.groupBox_burn)
        self.groupBox_debug = QtWidgets.QGroupBox(uploadBin)
        self.groupBox_debug.setObjectName("groupBox_debug")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_debug)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit_receive = QtWidgets.QPlainTextEdit(self.groupBox_debug)
        self.plainTextEdit_receive.setReadOnly(True)
        self.plainTextEdit_receive.setObjectName("plainTextEdit_receive")
        self.gridLayout.addWidget(self.plainTextEdit_receive, 3, 0, 1, 3)
        self.plainTextEdit_emit_send = QtWidgets.QPlainTextEdit(self.groupBox_debug)
        self.plainTextEdit_emit_send.setObjectName("plainTextEdit_emit_send")
        self.gridLayout.addWidget(self.plainTextEdit_emit_send, 1, 0, 1, 3)
        self.pushButton_emit_send = QtWidgets.QPushButton(self.groupBox_debug)
        self.pushButton_emit_send.setObjectName("pushButton_emit_send")
        self.gridLayout.addWidget(self.pushButton_emit_send, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_debug)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.groupBox_debug)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 2)
        self.pushButton_receive = QtWidgets.QPushButton(self.groupBox_debug)
        self.pushButton_receive.setObjectName("pushButton_receive")
        self.gridLayout.addWidget(self.pushButton_receive, 2, 2, 1, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.groupBox_debug)
        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(1, 3)

        self.retranslateUi(uploadBin)
        QtCore.QMetaObject.connectSlotsByName(uploadBin)

    def retranslateUi(self, uploadBin):
        _translate = QtCore.QCoreApplication.translate
        uploadBin.setWindowTitle(_translate("uploadBin", "Form"))
        self.groupBox_burn.setTitle(_translate("uploadBin", "烧录区域"))
        self.label_5.setText(_translate("uploadBin", "发送间隔时间"))
        self.label_3.setText(_translate("uploadBin", "ms"))
        self.label_2.setText(_translate("uploadBin", "消息发送提示区域"))
        self.label_6.setText(_translate("uploadBin", "发送数据包长度"))
        self.pushButton_send.setText(_translate("uploadBin", "烧录文件发送"))
        self.label_7.setText(_translate("uploadBin", "波特率"))
        self.pushButton_enum_com.setText(_translate("uploadBin", "枚举串口"))
        self.pushButton_set_param.setText(_translate("uploadBin", "参数确认"))
        self.pushButton_choose_file_path.setText(_translate("uploadBin", "选择文件路径"))
        self.pushButton_link_com.setText(_translate("uploadBin", "连接串口"))
        self.groupBox_debug.setTitle(_translate("uploadBin", "调试区域"))
        self.pushButton_emit_send.setText(_translate("uploadBin", "单次触发发送"))
        self.label_4.setText(_translate("uploadBin", "消息发送区域"))
        self.label.setText(_translate("uploadBin", "接收打印区域"))
        self.pushButton_receive.setText(_translate("uploadBin", "开始接收"))
