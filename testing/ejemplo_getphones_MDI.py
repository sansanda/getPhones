from testing.ejemplo_FichaPersona import *
from PyQt5.QtWidgets import QMainWindow, QMdiSubWindow, \
    QDesktopWidget, QMdiArea


class Ventana_Principal(QMainWindow):
    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent)
        self.num_ventanas = 0
        self.setWindowTitle('Ejemplo de aplicacio MDI para getphones')
        self.setGeometry(0,0,800,600)
        self.centraEnPantalla()

        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)

    #personPhoto_FilePath is a string
    #personData is a tuple: #(name, surname, ubication, phone ext)
    #personExtension is a string
    def addNewFichaPersona(self, personPhoto_FilePath, personData, personExtension):

        fichaPersona = Ficha_Persona()
        fichaPersona.setPersonPhoto(personPhoto_FilePath)
        fichaPersona.setPersonData(personData)
        fichaPersona.setPersonPhonenumber(personExtension)

        subventana = QMdiSubWindow()
        subventana.setWidget(fichaPersona)
        subventana.setWindowTitle('Subventana nº {}'.format(self.num_ventanas))
        self.mdi_area.addSubWindow(subventana)
        subventana.show()
        self.mdi_area.tileSubWindows()

    def centraEnPantalla(self):
        resolucion_pantalla = QDesktopWidget().screenGeometry()
        self.move(int(resolucion_pantalla.width()/2 - self.frameSize().width()/2),int(resolucion_pantalla.height()/2 - self.frameSize().height()/2))




def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = Ventana_Principal()
    mw.addNewFichaPersona('../photos/033.JPG', ('vvvvvv','bbbbbbbbbbb','nnnnnnnn','nmmmmmmmm'), '2216')
    mw.addNewFichaPersona('../photos/030.JPG', ('vvvvvv', 'bbbbbbbbbbb', 'nnnnnnnn', 'nmmmmmmmm'), '2216')
    mw.addNewFichaPersona('../photos/034.JPG', ('vvvvvv', 'bbbbbbbbbbb', 'nnnnnnnn', 'nmmmmmmmm'), '2216')

    mw.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()