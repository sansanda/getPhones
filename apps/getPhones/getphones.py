import sys

from PyQt5 import QtWidgets

from Logic.Employees_List import Employees_List
from Logic.Filter.TextFilter import TextFilter
from uis.Mostrador_FichasPersona import Mostrador_FichasPersona

EMPLOYEES_FILE_PATH = '..\\persistence\\data\\'
EMPLOYEES_IMAGES_FOLDER = 'employees_images\\'
EMPLOYEES_FILE_NAME = 'EmployeesData.xlsx'

thresholdTime = 360 #360 horas = 15 dias x 24 horas/dia

def main():


    #Creamos la ui que va a servir para mostrar las fichas de los empleados
    app = QtWidgets.QApplication(sys.argv)
    mw = Mostrador_FichasPersona()


    #fase de carga de datos de los empleados desde el excel
    employeesList = Employees_List(EMPLOYEES_FILE_PATH,EMPLOYEES_FILE_NAME)
    employeesList.loadEmployeesDataFromSource(None)
    #fase de filtrado de los datos de los empleados segun la lista de nombre dada por los parametros de entrada
    textList = sys.argv[1:]
    myFilter = TextFilter(textList, caseSensitiveOption=False, andOption=False, wholeWordOption=False)
    filteredEmployeesList = employeesList.filterEmployees(myFilter)


    for employee in filteredEmployeesList:

        mw.addNewFichaPersona(EMPLOYEES_FILE_PATH + EMPLOYEES_IMAGES_FOLDER + employee['nombre'] + '.png', (employee['nombre'], employee['nombre'], employee['despacho'], employee['telefono']), employee['telefono'])

    mw.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()