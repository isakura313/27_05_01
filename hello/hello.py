"""" Простое приветствие на PyQt"""

import sys
# без sys нам не описать момент выхода из приложения
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget


app = QApplication(sys.argv)
#sys  argv дает возможность принимать аргументы из командной строк
#можно оставить скобки пустыми, если нам это не нужно

window = QWidget() #создаем окно

window.setWindowTitle("First APP")

window.setGeometry(90, 90, 500, 500)
#x,y где у нас окно появится, 300x300  -размер окна по горизонтали/вертикали
window.move(60, 15)
#двигаемся по X и по Y - где у нас будет отрисовка виджета
helloMsg = QLabel('<h1>  привет это Ozon </h1>', parent=window)
# helloMsg.resize(300,300)
helloMsg.move(60, 15)
window.move(60, 50)
helloSecond = QLabel('<h2>  как дела </h2>', parent=window)
helloSecond.move(60, 50)
#двигаемся обратно
#нам нужно показать окно
window.show()
#окно показали, а цикл выполнения не вызвали

#запускаем event loop
sys.exit(app.exec())
