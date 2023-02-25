import menus
def optionSelection(userInputList):
    calculateName = menus.calculateMenu[userInputList[1] - 1]
    signatureName = menus.signaturas[userInputList[2] - 1]
    return calculateName, signatureName

def calcUF1M01():
    notesRA1 = []
    notesRA2 = []
    NPRACTISES = 7
    PERCENTPPRA1 = 0.1
    PERCENTPPRA2 = 0.25
    for Nnote in range(1, NPRACTISES + 1):
        pp = float(input(f'Nota PP{Nnote}? : '))
        if Nnote < 5:
            notesRA1.append(pp * PERCENTPPRA1)
        else:
            notesRA2.append(pp * PERCENTPPRA2)
    test = float(input('Nota del test UF1? : '))
    RA1 = (sum(notesRA1) + (test * 0.5)) * 0.5
    RA2 = (sum(notesRA2) + (test * 0.5)) * 0.5

    total = round(RA1 + RA2, 2)
    print(total)
    return total

calcUF1M01()
