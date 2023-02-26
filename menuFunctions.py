import menus
def spawnMenu(position, title = 'Main'):
    quantity = 30
    print(title.center(quantity, '-'))
    counter = 1
    for option in menus.menus[position]:
        print(f'{counter} · {option}')
        counter += 1
    return int(input(f'\nOpción? : '))
def spawnUFMenu(signature):
    quantity = 30
    title = 'Select UF'
    print(title.center(quantity, '-'))
    for uf in range(1, menus.signaturas[signature] + 1):
        print(f'{uf} · UF{uf}')