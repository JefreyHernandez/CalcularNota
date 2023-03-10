import sys
import menuFunctions as mF
import notesFunctions as nF
import calcFunctions as cF
import menus

user_selections = []
menuPosition = 0
try:
    while 0 <= menuPosition < len(menus.menus):
        optionSelected = mF.spawnMenu(menuPosition, menus.titles[menuPosition])
        if optionSelected == len(menus.menus[menuPosition]):
            try:
                user_selections.pop()
                menuPosition -= 1
            except:
                sys.exit(0)
        else:
            user_selections.append(optionSelected)
            menuPosition += 1


    calcOption, signatureOption = nF.optionSelection(user_selections)

    match user_selections[2]:
        case 1:
            if user_selections[1] == 1:
                cF.calcM01()
            elif user_selections[1] == 2:
                mF.spawnUFMenu(signatureOption)
                selectedUF = int(input(f"\nOpción? : "))
                match selectedUF:
                    case 1:
                        nota, lessnote = cF.calcUF1M01()
                        print(f'\nNota UF1 M01 : {nota}')
                        if lessnote:
                            nF.printLessnote()
                    case 2:
                        nota, lessnote = cF.calcUF2M01()
                        print(f'\nNota UF2 M01 : {nota}')
                        if lessnote:
                            nF.printLessnote()
                    case 3:
                        pass
                    case 4:
                        pass
                    case _:
                        nF.printPermitedUFs()
        case 2:
            pass
        case 3:
            if user_selections[1] == 1:
                pass
            elif user_selections[1] == 2:
                mF.spawnUFMenu(signatureOption)
                selectedUF = int(input(f"\nOpción? : "))
                match selectedUF:
                    case 1:
                        nota, lessnote = cF.calcUF1M03()
                        print(f'\nNota UF1 M03 : {nota}')
                        if lessnote:
                            nF.printLessnote()
                    case 2:
                        pass
                    case 3:
                        pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            if user_selections[1] == 1:
                pass
            elif user_selections[1] == 2:
                mF.spawnUFMenu(signatureOption)
                selectedUF = int(input(f"\nOpción? : "))
                match selectedUF:
                    case 1:
                        nota = cF.calcUF1M07()
                        print(f'Nota UF1 M07 : {nota}')
                    case 2:
                        nota = cF.calcUF2M07()
                        print(f'Nota UF2 M07 : {nota}')
                    case 3:
                        pass
        case 8:
            pass
        case 9:
            pass
        case 10:
            pass
        case 11:
            pass
        case 12:
            pass
        case 13:
            pass
except:
    sys.exit(1)