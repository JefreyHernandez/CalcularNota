import sys
import menuFunctions
import notesFunctions
import menus

user_selections = []
menuPosition = 0

while 0 <= menuPosition < len(menus.menus):
    optionSelected = menuFunctions.spawnMenu(menuPosition, menus.titles[menuPosition])
    if optionSelected == len(menus.menus[menuPosition]):
        try:
            user_selections.pop()
            menuPosition -= 1
        except:
            sys.exit(0)
    else:
        user_selections.append(optionSelected)
        menuPosition += 1

calcOption, signatureOption = notesFunctions.optionSelection(user_selections)
print(calcOption)
print(signatureOption)
