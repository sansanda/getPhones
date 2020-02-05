
from Data.miner.employeesDataMiner import EmployeesDataMiner
import os
import time
from tkinter import messagebox

URL = "https://intranet.imb-cnm.csic.es/intranet/"
USER = 'dsanchez'
PASSWORD = 'mtx.23'
EMPLOYEES_FILE_PATH = '..\\persistence\\data\\'
EMPLOYEES_IMAGES_FOLDER = 'employees_images\\'
EMPLOYEES_FILE_NAME = 'EmployeesData.xlsx'

thresholdTime = 360 #360 horas = 15 dias x 24 horas/dia

def main():

    modificationTime = os.path.getmtime(EMPLOYEES_FILE_PATH+EMPLOYEES_FILE_NAME)
    #print(modificationTime)
    actualTime = time.time()
    #modificationTime = 1
    #print(actualTime)
    file_hoursOld = (actualTime-modificationTime)/3600
    #print(file_hoursOld)
    if file_hoursOld>thresholdTime:
        #messagebox.showinfo("Employees data is too old.", "Proceding to update the employees data.")
        edm = EmployeesDataMiner(URL,USER,PASSWORD,EMPLOYEES_FILE_PATH,EMPLOYEES_FILE_NAME,EMPLOYEES_IMAGES_FOLDER)
        edm.recoverEmployeesData()


if __name__ == "__main__":
    main()