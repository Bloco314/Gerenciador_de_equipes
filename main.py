import sys
from PyQt5.QtWidgets import QApplication
from Boundary import Tela_inicial
from Entity import criaDB

app = QApplication(sys.argv)
initer = criaDB()
tl = Tela_inicial()
app.exec()
