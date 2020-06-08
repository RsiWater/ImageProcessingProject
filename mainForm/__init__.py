from PyQt5 import QtWidgets, uic
import os
path = os.getcwd()
qtCreatorFile = path + os.sep + "UI" + os.sep + "untitled.ui"  # 設計好的ui檔案路徑
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)   # 讀入用Qt Designer設計的GUI layout

class MainUi(QtWidgets.QMainWindow, Ui_MainWindow):  # Python的多重繼承 MainUi 繼承自兩個類別
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        