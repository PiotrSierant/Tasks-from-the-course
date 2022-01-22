cake_01 = {
    'taste': 'vanilia',
    'glaze': 'chocolade',
    'text': 'Happy Brithday',
    'weight': 0.7
}

cake_02 = {
    'taste': 'tee',
    'glaze': 'lemon',
    'text': 'Happy Python Coding',
    'weight': 1.3
}

lista = [cake_01, cake_02]


def show_cake_info(cake):
    return print('{} cake with {} glaze with text "{}" of {} kg'.format(
        cake['taste'], cake['glaze'], cake['text'], cake['weight']))

# print(show_cake_info(cake_01))
# print(show_cake_info(cake_02))

for cake in lista:
    show_cake_info(cake)