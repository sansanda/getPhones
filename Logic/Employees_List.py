"""

Creating a Laser Jobs Book to store all the laser jobs

David SAnchez Sanchez


"""

from Logic.Filter.IFilter import IFilter

from Data.Excel_Utilities.ExcelUtils_OpenpyxlBased import loadEmployeesFromExcel
from Data.Excel_Utilities.ExcelUtils_OpenpyxlBased import insertRowInExcel
from Data.Excel_Utilities.ExcelUtils_OpenpyxlBased import deleteRowInExcel
from Data.Excel_Utilities.ExcelUtils_OpenpyxlBased import deleteAllRows


from Logic.EmployeeData import EmployeeData

class Employees_List(list):

    def __init__(self, employeesDataFilePath, employeesDataFileName):
        list.__init__(self)
        self.employeesDataFilePath = employeesDataFilePath
        self.employeesDataFileName = employeesDataFileName

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

    def loadEmployeesDataFromSource(self, filter):
        self.deleteAllEmployees()
        loadEmployeesFromExcel(self, self.employeesDataFilePath, self.employeesDataFileName)
        filteredEmployees = (self.filterEmployees(filter))
        filteredEmployees.sort(key=lambda k: k['nombre'])
        filteredEmployees_Count = len(filteredEmployees)
        return filteredEmployees, filteredEmployees_Count

    def updateEmployeesDataSource(self, updatedEmployeeData, deleteEmployee=False):
        if self.existEmployee(updatedEmployeeData['nombre']):
            deleteRowInExcel(updatedEmployeeData, self.employeesDataFilePath, self.employeesDataFileName)
        if deleteEmployee == False:
            insertRowInExcel(updatedEmployeeData, self.employeesDataFilePath, self.employeesDataFileName)

    def emptyDataSource(self):
        deleteAllRows(self.employeesDataFilePath, self.employeesDataFileName)

    def insertEmployeeInDataSource(self,  employeeData):
        insertRowInExcel(employeeData, self.employeesDataFilePath, self.employeesDataFileName)

def main():
    el = Employees_List()
    ed = EmployeeData('Pepe2','de','2g1','desplñ,l','661290548','dsabcsiuh@gmail.com','mifoto')
    ed2 = EmployeeData('Pepe', 'dede', '2g1', 'desplñ,l', '661290548', 'dsabcsiuh@gmail.com', 'mifoto')
    el.loadEmployeesDataFromSource('E:\\software development\\getPhones\\persistence\\data\\', 'EmployeesData.xlsx', None)
    print(el)
    el.newEmployee(ed)
    print(el)
    #el.updateEmployeesDataSource('E:\\software development\\getPhones\\persistence\\data\\', 'EmployeesData.xlsx',ed2)
    print(el)



if __name__ == "__main__":
    main()