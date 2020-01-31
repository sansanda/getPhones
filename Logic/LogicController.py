"""

Creating a Logic Controller to control the logic part of the Laser Job Logbook

David Sanchez Sanchez


"""
from tkinter import messagebox

from Logic.Employees_List import Employees_List
from Logic.DesignPatterns.ObserverPattern import Publisher
from Logic.Filter.TextFilter import TextFilter

from threading import Timer

import json
import os

class LogicController(Publisher):


    def __init__(self, configFilePath, configFileName, defaultLaserJobsFilePath, defaultLaserJobsFileName):
        Publisher.__init__(self)
        self.guiController = None
        self.laserJobsBook = Employees_List()
        self.configFilenamePath = configFilePath
        self.configFilename = configFileName

        self.laserJobsFilepath, self.laserJobsFilename = self.loadLaserJobsFileLocation(self.configFilenamePath+self.configFilename)
        self.laserJobsFilepath = os.path.abspath(self.laserJobsFilepath ) + '/'
        self.defaultLaserJobsFilePath =  os.path.abspath(defaultLaserJobsFilePath ) + '/'
        self.defaultLaserJobsFileName = defaultLaserJobsFileName

        self.existsLaserJobsFile, self.existsConfigFile = self.checkExistenceOfNeededFiles(self.laserJobsFilepath + self.laserJobsFilename,
                                                                                           self.configFilenamePath + self.configFilename)

        if not self.existsConfigFile:
            messagebox.showerror("Config File not found!!!!!",
                                 "Please check that the config.json file is in the ./persistence/config/ folder !!!!!")
            os.system(exit(-1))

        self.filter = self.loadFilter(self.configFilenamePath + self.configFilename)

        if not self.existsLaserJobsFile:
            #delay = 1000
            #AuxiliarWindows.showProcessInfoWindow(delay, "Laser Jobs File not found!!!!!","Please, now proceding to use an empty default Laser Jobs File!!!!!")

            self.laserJobsFilepath = self.defaultLaserJobsFilePath
            self.laserJobsFilename = self.defaultLaserJobsFileName

        self.updateConfigFile(self.configFilenamePath,self.configFilename)

    def setGuiController(self,guicontroller):
        self.guiController = guicontroller
        self.guiController.setLogicController(self)
        #add the main window as observer
        self.addObserver(self.guiController.actualWindow)

    def getGuiController(self):
        return self.guiController

    def loadFilter(self, configFilename):
        with open(configFilename) as f:
            data = json.load(f)
        return TextFilter(
            [''],
            data['textFilterOptions']['caseSensitive'],
            data['textFilterOptions']['and'],
            data['textFilterOptions']['wholeWord']
        )

    def loadLaserJobsFileLocation(self, configFilename):
        with open(configFilename) as f:
            data = json.load(f)
        return data['laserJobsFileLocation']['laserJobsFilePath'],data['laserJobsFileLocation']['laserJobsFileName']

    def loadJobsFromSource(self, laserJobsFilepath, laserJobsFilename, filter):
        jobsData = self.laserJobsBook.loadEmployeesDataFromSource(laserJobsFilepath, laserJobsFilename, filter)

        jobs, nVectorJobs, nRasterJobs, nCombinedJobs = jobsData[0:4]
        self.notify((jobs, nVectorJobs, nRasterJobs, nCombinedJobs, self.laserJobsFilepath+self.laserJobsFilename))

    def checkExistenceOfNeededFiles(self, laserJobsFileLocation, configFilenameLocation):
        return os.path.exists(laserJobsFileLocation), os.path.exists(configFilenameLocation)

    def newJob(self,laserJob):
        try:
            jobId = self.laserJobsBook.getFirstFreeId()
            laserJob['jobId'] = jobId
            self.laserJobsBook.updateEmployeesDataSource(self.laserJobsFilepath, self.laserJobsFilename, laserJob)
            self.loadJobsFromSource(self.laserJobsFilepath,self.laserJobsFilename,self.filter)

        except PermissionError as pe:
            messagebox.showerror("Excel opened!!!!!", "The excel file must be closed if you want to add new jobs!!!!!")

        except Exception as inst:
            raise(inst)

    def editJob(self,jobId):
        print('Editing job...')
        pass

    def deleteJob(self,jobId):

        try:
            jobData = self.laserJobsBook.getEmployee(jobId) #jobData is a dict
            self.laserJobsBook.updateEmployeesDataSource(self.laserJobsFilepath, self.laserJobsFilename, jobData, deleteEmployee=True)
            self.loadJobsFromSource(self.laserJobsFilepath, self.laserJobsFilename, self.filter)

        except PermissionError as pe:
            messagebox.showerror("Excel opened!!!!!", "The excel file must be closed if you want to add new jobs!!!!!")

        except Exception as inst:
            raise (inst)

    def getJob(self, jobId):
        return self.laserJobsBook.getEmployee(jobId)

    def updateJob(self,updatedJobData):
        #self.laserJobsBook.updateJob(updatedJobData)
        self.laserJobsBook.updateEmployeesDataSource(self.laserJobsFilepath, self.laserJobsFilename, updatedJobData)
        self.loadJobsFromSource(self.laserJobsFilepath, self.laserJobsFilename, self.filter)

    def updateTextFilterList(self,sv):
        self.filter.textList = str.split(sv,';')
        self.loadJobsFromSource(self.laserJobsFilepath, self.laserJobsFilename, self.filter)

    def updateTextFilterOptions(self, cs_option, and_option, wholeword_option):
        self.filter.caseSensitiveOption = cs_option
        self.filter.andOption = and_option
        self.filter.wholeWordOption = wholeword_option
        self.updateConfigFile(self.configFilenamePath, self.configFilename)
        self.loadJobsFromSource(self.laserJobsFilepath, self.laserJobsFilename, self.filter)

    def updateLaserJobsFileLocation(self, laserJobsFilepath, laserJobsFilename):
        self.laserJobsFilepath = laserJobsFilepath
        self.laserJobsFilename = laserJobsFilename
        self.updateConfigFile(self.configFilenamePath,self.configFilename)
        self.loadJobsFromSource(self.laserJobsFilepath, self.laserJobsFilename, self.filter)

    def updateConfigFile(self, configFilenamePath, configFilename):

        # save changes to file
        configData = dict()
        configData['textFilterOptions'] = self.filter.getTextFilterOptions()
        configData['laserJobsFileLocation'] = {'laserJobsFilePath':self.laserJobsFilepath,'laserJobsFileName':self.laserJobsFilename}

        with open(configFilenamePath + configFilename, 'w') as f:
            json.dump(configData, f)

    def start(self):

        delay = 1000
        # first time we load the laser jobs
        # we give time to guicontroller for creating the main window before load the laser jobs
        t = Timer(delay/1000, self.loadJobsFromSource, [self.laserJobsFilepath, self.laserJobsFilename, self.filter])
        t.start()
        #the line below will execute inmediatly after the t.start()
        self.guiController.start()
