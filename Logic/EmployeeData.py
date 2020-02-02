class EmployeeData(dict):

    keys = ['nombre', 'departamento', 'grupo', 'despacho', 'telefono', 'mail', 'foto']

    def __init__(self,nombre,departamento,grupo,despacho,telefono,mail,foto):
        self['nombre'] = nombre
        self['departamento'] = departamento
        self['grupo'] = grupo
        self['despacho'] = despacho
        self['telefono'] = telefono
        self['mail'] = mail
        self['foto'] = foto

    def containsText(self, text, wholeWord, caseSensitive):

        matched = False

        textToFind = str(text)
        if not caseSensitive:
            textToFind = str.upper(textToFind)

        for data in EmployeeData.getDataAsList(self):
            dataSource = str(data)
            if not caseSensitive:
                dataSource = str.upper(dataSource)

            if wholeWord:
                if dataSource == textToFind:
                    matched = True
                    break
            else:
                if not (dataSource.find(textToFind) == -1):
                    matched = True
                    break

        return matched

    @classmethod
    def getDataAsList(cls, employeeData):

        employeeDataAsList = list()
        for key in cls.keys:
            employeeDataAsList.append(employeeData[key])

        return employeeDataAsList

    @classmethod
    def createFromDict(cls, employeeDataAsDict):

        return EmployeeData(employeeDataAsDict['nombre'],
                            employeeDataAsDict['departamento'],
                            employeeDataAsDict['grupo'],
                            employeeDataAsDict['despacho'],
                            employeeDataAsDict['telefono'],
                            employeeDataAsDict['mail'],
                            employeeDataAsDict['foto'])

    @classmethod
    def createFromTuple(cls, employeeDataAsTuple):

        return EmployeeData(employeeDataAsTuple[0],
                            employeeDataAsTuple[1],
                            employeeDataAsTuple[2],
                            employeeDataAsTuple[3],
                            employeeDataAsTuple[4],
                            employeeDataAsTuple[5],
                            employeeDataAsTuple[6])

def main():
    ed = EmployeeData('david','de','2g1','desplñ,l','661290548','dsabcsiuh@gmail.com','mifoto')
    print(ed)
    print(ed.containsText('Dav',False,True))


if __name__ == "__main__":
    main()