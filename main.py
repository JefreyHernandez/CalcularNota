import menuFunctions as mF

#The last digit of the menus, is the ID of the menu, its equal to the choosen number

mainMenu = ('UF', 'Modulo', 'Total', 'Salir', 0)
moduloMenu = ('M01 [Sistemas]', 'M02 [BBDD]', 'M03 [Programación]', 'M04 [Marcas]', 'M05 [Maquinas]', 'M07 [Redes]', 'M12 [FOL]', 'M13 [EIE]', 'Salir', 2)
ufMenu = (moduloMenu[:-1], 1)
menus = (mainMenu, moduloMenu, ufMenu)

mF.printOptions(mainMenu[:-1])
choosen = int(input("\nOption? : "))
menuChoosen = mF.detectMenu(menus, choosen)
while 1 <= choosen <= len(menuChoosen[:-1]):
    mF.printOptions(menuChoosen[:-1], mainMenu[choosen - 1])
    choosen = int(input("\nOption? : "))
    if choosen == len(menuChoosen[:-1]):
        menuChoosen = mainMenu
