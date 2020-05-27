"""" Простое приветствие на PyQt"""

import sys
# без sys нам не описать момент выхода из приложения
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget


app = QApplication(sys.argv)
#sys  argv дает возможность принимать аргументы из командной строк
#можно оставить скобки пустыми, если нам это не нужно

window = QWidget() #создаем окно

window.setWindowTitle("Расположение в гридах")
layout = QGridLayout()


layout.addWidget(QLabel("слева"), 0, 0)
#добавляется второй опциональный аргумент, 1 - ряд, в котором он располагается, второй у нас это позиция в ряду
layout.addWidget(QPushButton("по центру"), 1, 1)
layout.addWidget(QPushButton("Справа"), 2, 2)
window.setLayout(layout)
window.show()
#окно показали, а цикл выполнения не вызвали

#запускаем event loop
sys.exit(app.exec())
