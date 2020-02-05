from Data.miner.CNMEmployeesDataMiner import CNMEmployeesDataMiner
from selenium import webdriver
from Logic.Employees_List import *


class EmployeesDataMiner():

    def __init__(self, url, user, password, employeesDataFilePath, employeesDataFileName, employeesImagesFolder):
        self.url = url
        self.user = user
        self.password = password
        self.employeesFilePath = employeesDataFilePath
        self.employeesFileName = employeesDataFileName
        self.employeesImagesFolder = employeesImagesFolder

    def recoverEmployeesData(self):

        driver = webdriver.Chrome()
        cnmEmployeesDataMiner = CNMEmployeesDataMiner(self.url, self.user, self.password, self.employeesFilePath,self.employeesFileName,self.employeesImagesFolder)
        el = Employees_List(self.employeesFilePath,self.employeesFileName)
        cnmEmployeesDataMiner.doLogin(driver)
        cnmEmployeesDataMiner.goToPersonalListPage(driver)
        visiblePersons_Records = cnmEmployeesDataMiner.getWebVisiblePersons_Records(driver)

        print(visiblePersons_Records)

        el.emptyDataSource()

        print("Excel limpiado")


        for record in visiblePersons_Records:
            recordData = cnmEmployeesDataMiner.getRecordData(driver, record)
            print(recordData)
            e = EmployeeData.createFromTuple(recordData)
            el.newEmployee(e)
            el.insertEmployeeInDataSource(e)

