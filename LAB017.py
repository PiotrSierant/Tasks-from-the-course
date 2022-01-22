from os import path


def cal(amount, *rooms):
    amount_metr = sum(rooms)
    lengthrooms = len(rooms)
    paint = amount * lengthrooms * amount_metr

    return print('Amount od paint needed: {} l'.format(paint))


rooms = [20, 30, 40, 50]
cal(0.2, *rooms)
cal(0.2, 20, 30, 40)


def log_it(*args):
    myfile = r'C:\Users\dzd07\Desktop\Python\data.txt'
    with open(myfile, 'a', encoding='UTF-8') as file:
        for line in args:
            file.write(line)
            file.write(", ")

        file.write("\n")


log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')
