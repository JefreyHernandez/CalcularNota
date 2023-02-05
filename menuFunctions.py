def printOptions(list, menuName = 'Main'):
    TIMES = 30
    number = 1
    optionSeparator = '·'
    menubarSeparator = "-"

    print(f'\n{menuName.center(TIMES, menubarSeparator)}')
    for option in list:
        print(f"\t{number} {optionSeparator} {option}")
        number += 1

def detectMenu(menus, id):
    for menu in menus:
        if menu[-1] == id:
            return menu