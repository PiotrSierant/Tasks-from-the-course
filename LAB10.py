ports_start = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
               'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

ports_stop = ports_start


flying = ((a, b) for a in ports_start for b in ports_stop)
try:
    counter = 0
    for (start, stop) in flying:
        print("{} - {}".format(start, stop))
        counter += 1

except StopIteration:
    print("all value have been used")

print(counter)
'''
flying1 = ((a, b) for a in ports_start for b in ports_stop if a != b)
while True:
    try:
        print(next(flying1))
    except StopIteration:
        print("all value have been used")
        break


flying2 = ((a, b) for a in ports_start for b in ports_stop if a != b and a < b)
while True:
    try:
        print(next(flying2))
    except StopIteration:
        print("all value have been used")
        break
    '''
