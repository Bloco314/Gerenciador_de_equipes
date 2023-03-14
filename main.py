import sys
from PyQt5.QtWidgets import QApplication
from Boundary import Tela_inicial
from Entity import ADMDB

app = QApplication(sys.argv)
initer = ADMDB()
tl = Tela_inicial()
app.exec()
