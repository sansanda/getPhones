import sys

sys.path.append(r"E:\repos\GUIS-con-Python-3\Ejercicios")
from uis.FichaPersona_ui import *
from recursos.recursos_1_rc import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import *


class Ficha_Persona(QMainWindow):
    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent)
        self.ui = Ui_FichaPersona()
        self.ui.setupUi(self)

    #path is an String
    def setPersonPhoto(self, path):

        try:
            mi_imagen = QPixmap(path)
            mi_imagen = mi_imagen.scaled(150,150)
            self.ui.personPhotoL.setAlignment(QtCore.Qt.AlignCenter)
            self.ui.personPhotoL.setPixmap(mi_imagen)

        except:
            print("An exception occurred")

    #person data is a tuple with
    #(name, surname, ubication, phone ext)
    def setPersonData(self, personData):
        self.ui.personDataLW.addItem('Name: {}'.format(personData[0]))
        self.ui.personDataLW.addItem('Surname: {}'.format(personData[1]))
        self.ui.personDataLW.addItem('Ubication: {}'.format(personData[2]))
        self.ui.personDataLW.addItem('Ext: {}'.format(personData[3]))

    #phoneNumber is a String
    def setPersonPhonenumber(self, phoneNumber):
        self.ui.personPhoneL.setText(phoneNumber)

def main():
    app = QtWidgets.QApplication(sys.argv)
    fp = Ficha_Persona()
    fp.setPersonPhoto('./photos/033.JPG')
    fp.setPersonData(('vvvvvv','bbbbbbbbbbb','nnnnnnnn','nmmmmmmmm'))
    fp.setPersonPhonenumber('2216')
    fp.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()