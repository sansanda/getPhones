"""

Creating a Laser Jobs Book to store all the laser jobs

David SAnchez Sanchez


"""

from Logic.Filter.IFilter import IFilter

from Data.Excel_Utilities.ExcelUtils_OpenpyxlBased import loadEmployeesFromExcel
from Data.Excel_Utilities.ExcelUtils_OpenpyxlBased import insertRowInExcel
from Data.Excel_Utilities.ExcelUtils_OpenpyxlBased import deleteRowInExcel

from Logic.EmployeeData import EmployeeData

class Employees_List(list):

    def __init__(self):
        list.__init__(self)

    def filterEmployees(self, IFilter):
        if not IFilter: return self
        employeesFiltered = list()
        for employee in self:
            if IFilter.satisfies(employee):
                employeesFiltered.append(employee)
        return employeesFiltered

    # Job CRUD

    # newEmployee data as dictionary
    def newEmployee(self, employeeData):

        if self.existEmployee(employeeData['nombre']) == -1:
            self.append(employeeData)
        else:
            raise Exception('The employee with name=' + employeeData['nombre'] + ' already exists!!!!')

    # return employee as dictionary with name equals to employeeName

    def getEmployee(self, employeeName):
        employeeIndex = self.existEmployee(employeeName)
        if not employeeIndex == -1:
            return self[employeeIndex]
        else:
            raise Exception('The employee with name=' + employeeName + ' already exists!!!!')

    # updatedEmployeeData as dictionary
    def updateEmployee(self, updatedEmployeeData):
        self.deleteEmployee(updatedEmployeeData)
        self.newEmployee(updatedEmployeeData)

    # delete employee indicated by employeeName
    def deleteEmployee(self, employeeName):
        employeeIndex = self.existEmployee(employeeName)
        if not employeeIndex == -1:
            del self[employeeIndex]
        else:
            raise Exception('The employee with name=' + employeeName + ' already exists!!!!')

    def deleteAllEmployees(self):
        self.clear()

    # employeeName is an string
    # return True if the name of the employee exists. False otherwise
    def existEmployee(self, employeeName):
        employeeIndex = -1
        for index in range(len(self)):
            if self[index]['nombre'] == employeeName:
                employeeIndex = index
                break
        return employeeIndex

    def loadEmployeesDataFromSource(self, employeesDataFilepath, employeesDataFilename, filter):
        self.deleteAllEmployees()
        loadEmployeesFromExcel(self, employeesDataFilepath, employeesDataFilename)
        filteredEmployees = (self.filterEmployees(filter))
        filteredEmployees.sort(key=lambda k: k['nombre'])
        filteredEmployees_Count = len(filteredEmployees)
        return filteredEmployees, filteredEmployees_Count

    def updateEmployeesDataSource(self, employeesDataFilepath, employeesDataFilename, updatedEmployeeData, deleteEmployee=False):
        if deleteEmployee == False:
            insertRowInExcel(updatedEmployeeData, employeesDataFilepath, employeesDataFilename)
        elif deleteEmployee == True:
            deleteRowInExcel(updatedEmployeeData, employeesDataFilepath, employeesDataFilename)

def main():
    el = Employees_List()
    ed = EmployeeData('david','de','2g1','desplñ,l','661290548','dsabcsiuh@gmail.com','mifoto')
    el.loadEmployeesDataFromSource('E:\\repos\\getPhones\\persistence\\data\\', 'EmployeesData.xlsx', None)
    print(el)

if __name__ == "__main__":
    main()