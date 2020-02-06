from Logic.Filter.IFilter import IFilter
from Logic.EmployeeData import EmployeeData

class TextFilter(IFilter):

    #textList is a list of strings
    def __init__(self, textList, caseSensitiveOption=True, andOption=True, wholeWordOption=True):
        self.textList = textList
        self.caseSensitiveOption = caseSensitiveOption
        self.andOption = andOption
        self.wholeWordOption = wholeWordOption

    def satisfies(self, employeeData):

        if len(self.textList) == 1 and self.textList[0] == '' : return True

        if self.andOption:
            return self.__allTextAreInLaserJob(employeeData)
        else:
            return self.__atLeastOneTextIsInLaserJob(employeeData)

    def getName(self):
        return 'TextFilter'

    def getTextFilterOptions(self):
        textFilterOptions = dict()
        textFilterOptions['caseSensitive'] = self.caseSensitiveOption
        textFilterOptions['and'] = self.andOption
        textFilterOptions['wholeWord'] = self.wholeWordOption
        return textFilterOptions

    #auxiliar methods
    def __allTextAreInLaserJob(self, employeeData):
        for text in self.textList:
            if not EmployeeData.containsText(employeeData, text, self.wholeWordOption, self.caseSensitiveOption):
                return False
        return True


    def __atLeastOneTextIsInLaserJob(self, employeeData):
        for text in self.textList:
            if EmployeeData.containsText(employeeData, text, self.wholeWordOption, self.caseSensitiveOption):
                return True
        return False
