# Los porcentajes estan puestos directamente para operar
# EJ : 0.1 = 10%

import menus
import sys
def optionSelection(userInputList):
    calculateName = menus.calculateMenu[userInputList[1] - 1]
    signatureName = menus.signaturas[userInputList[2] - 1]
    return calculateName, signatureName
def printPermitedNotes():
    print('El resultado no esta entre las notas permitidas [0 - 10]')
def getUFNotes(NUFS):
    UFNotesList = []
    for UF in range(NUFS):
        note = int(input(f'Nota de la UF{UF} : '))
        if 0 <= note <= 10:
            UFNotesList.append(note)
        else:
            printPermitedNotes()
            sys.exit(1)
    return UFNotesList
def insertPP(NPPs):
    ppList = []
    for Npp in range(1, NPPs + 1):
        try:
            pp = float(input(f'Nota PP{Npp}? : '))
            if 0 <= pp <= 10:
                ppList.append(pp)
            else:
                sys.exit(1)
        except ValueError as pptype2:
            try:
                pp = str(pptype2).split("'")
                pp = pp[1].split("/")
                divisor = int(pp[0])
                divident = int(pp[1])
                pp = divisor / divident * 10
                if 0 <= pp <= 10:
                    ppList.append(pp)
                else:
                    printPermitedNotes()
                    sys.exit(1)
            except:
                sys.exit(1)
    return ppList
def insertTEST(NTests):
    testList = []
    for Ntest in range(1, NTests + 1):
        try:
            pp = float(input(f'Nota test {Ntest} UF2? : '))
            testList.append(pp)
        except ValueError as testtype2:
            try:
                test = str(testtype2).split("'")
                test = test[1].split("/")
                divisor = int(test[0])
                divident = int(test[1])
                test = divisor / divident * 10
                if 0 <= test <= 10:
                    testList.append(test)
                else:
                    printPermitedNotes()
                    sys.exit(1)
            except:
                sys.exit(1)
    return testList
def detectLessnote(noteList, minimumNote):
    for note in noteList:
        if note < minimumNote:
            return True
    return False


