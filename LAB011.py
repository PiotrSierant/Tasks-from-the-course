import math
from typing import Counter

argument_list = []

i = 0
counter = 0
while counter < 100:
    argument_list.append(round(i, 2))
    i += (0.1)
    counter += 1

formula = input("Please enter a formula, use 'x' as t5he argument: ")

for x in argument_list:
    print("{0:3.1f} {1:6.2f}".format(x, eval(formula)))