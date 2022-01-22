options = ['load data', 'export data', 'analyze & predict']
choice = 'x'

def DisplayOptions(list):
    number = 0
    a = 0

    for _ in list:
        print(number, '. ', list[a], sep="")
        number += 1
        a += 1

    choice = input('Select option above or press enter to exit:')
    return str(choice)

while choice:
    choice = DisplayOptions(options)
    if len(choice) > 0:
        try:
            choice_num = int(choice)
            if choice_num >= 0 and choice_num < len(options):
                if choice_num == 1 or choice_num == 2 or choice_num == 0:
                    print('An option is selected', choice_num)
            else:
                print('The number given is wrong\n')

        except:
            print('Please enter a number\n')
    
    else:
        print('The program has finished running\n')