from PyQt5.QtWidgets import QApplication
from uploadThread import mainWindowUi
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainUi = mainWindowUi()
    mainUi.setWindowIcon(QIcon("1.ico"))
    mainUi.setWindowTitle("烧录文件_V1.0")
    mainUi.show()

    sys.exit(app.exec())
