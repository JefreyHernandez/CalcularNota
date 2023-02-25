import menus
def spawnMenu(position, title = 'Main'):
    quantity = 30
    print(title.center(quantity, '-'))
    counter = 1
    for option in menus.menus[position]:
        print(f'{counter} {"·"} {option}')
        counter += 1
    return int(input(f'\nOpción? : '))