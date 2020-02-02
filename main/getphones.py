from ddbb.CNMEmployeesCaller import CNMEmployeesCaller
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from Logic.Employees_List import *


URL = "https://intranet.imb-cnm.csic.es/intranet/"
USER = 'dsanchez'
PASSWORD = 'mtx.23'
EMPLOYEES_FILE_PATH = 'E:\\software development\\getPhones\\persistence\\data\\'
EMPLOYEES_FILE_NAME = 'EmployeesData.xlsx'

driver = webdriver.Chrome()
cnmEmployeesCaller = CNMEmployeesCaller()
el = Employees_List()
cnmEmployeesCaller.doLogin(driver,URL,USER,PASSWORD)
cnmEmployeesCaller.goToPersonalListPage(driver)
visiblePersons_Records = cnmEmployeesCaller.getWebVisiblePersons_Records(driver)

print(visiblePersons_Records)

el.emptyDataSource(EMPLOYEES_FILE_PATH, EMPLOYEES_FILE_NAME)

print("Excel limpiado")

for record in visiblePersons_Records:
    recordData = cnmEmployeesCaller.getRecordData(driver, record)
    print(recordData)
    e = EmployeeData.createFromTuple(recordData)
    el.newEmployee(e)
    el.insertEmployeeInDataSource(EMPLOYEES_FILE_PATH, EMPLOYEES_FILE_NAME,e)
