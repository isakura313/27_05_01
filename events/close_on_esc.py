import sys
from PyQt5.QtCore import  Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Example(QWidget):
    """Просто тренировочный класс для создания выходна на esc"""
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QLabel("press esc to escape", self)
        btn.move(30, 50)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Обработчик событий")

        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_1:
            self.close()

# if __name__ == "__main__":
    #определяет, исполняется ли именно этот файл
    #или он используется в качестве модуля
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec())
