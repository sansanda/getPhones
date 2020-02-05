
from Logic.Employees_List import Employees_List
from Logic.Filter.TextFilter import TextFilter

EMPLOYEES_FILE_PATH = '..\\persistence\\data\\'
EMPLOYEES_IMAGES_FOLDER = 'employees_images\\'
EMPLOYEES_FILE_NAME = 'EmployeesData.xlsx'

thresholdTime = 360 #360 horas = 15 dias x 24 horas/dia

def main():

    el = Employees_List(EMPLOYEES_FILE_PATH,EMPLOYEES_FILE_NAME)
    el.loadEmployeesDataFromSource(None)
    print(el)

    myFilter = TextFilter("David", caseSensitiveOption=False, andOption=False, wholeWordOption=False)
    print(el.filterEmployees(myFilter))

if __name__ == "__main__":
    main()