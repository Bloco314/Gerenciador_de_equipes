from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QAbstractTableModel


class Tabela(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(Tabela, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])
