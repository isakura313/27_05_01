import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout
import random

def greeting():
    """ slot function"""
    if msg.text():
        msg.setText("")
    else:
        msg.setText(str(random.randint(0, 10)))

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Сигналы и слоты")
layout = QVBoxLayout()

btn = QPushButton("привет")
btn.clicked.connect(greeting)

layout.addWidget(btn)
msg = QLabel('')

layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())