def printOptions(list, menuName = 'Main'):
    TIMES = 30
    number = 1
    optionSeparator = '·'
    menubarSeparator = "-"

    print(f'\n{menuName.center(TIMES, menubarSeparator)}')
    for option in list:
        print(f"\t{number} {optionSeparator} {option}")
        number += 1