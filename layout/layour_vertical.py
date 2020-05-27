"""" Простое приветствие на PyQt"""

import sys
# без sys нам не описать момент выхода из приложения
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget


app = QApplication(sys.argv)
#sys  argv дает возможность принимать аргументы из командной строк
#можно оставить скобки пустыми, если нам это не нужно

window = QWidget() #создаем окно

window.setWindowTitle("Горизонтальное расположение")
layout = QVBoxLayout()
layout.addWidget(QLabel("сверху"))
layout.addWidget(QPushButton("по центру"))
layout.addWidget(QPushButton("Снизу"))
window.setLayout(layout)
window.show()
#окно показали, а цикл выполнения не вызвали

#запускаем event loop
sys.exit(app.exec())
