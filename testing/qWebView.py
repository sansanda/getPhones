import sys

sys.path.append(r"E:\repos\GUIS-con-Python-3\Ejercicios")
from Ejercicios.qWebView.QWebView_ui import *
from PyQt5.QtWidgets import QMainWindow, QStatusBar, QLabel, QDialog, QWidget

from bs4 import BeautifulSoup
import requests

class MyForm(QDialog):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.boton_cargar.clicked.connect(self.cargar)

    def cargar(self):
        self.ui.pagina_web.stop()
        self.ui.pagina_web.setUrl(QtCore.QUrl(self.ui.direccion.text()))
        try:
            self.ui.pagina_web.load()
        except:
            print('Excepcion')

def main():
    app = QtWidgets.QApplication(sys.argv)
    mf = MyForm()
    mf.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()