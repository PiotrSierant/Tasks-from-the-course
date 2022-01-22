import itertools
import math

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

for a in itertools.permutations(notes, 4):
    print(a)

#liczenie silni (z modułu math - factorial)
print("4-notes melody, notes cannot repeat - it is variation without repeating - there are {} possibilities".format(math.factorial(len(notes))/math.factorial(len(notes) - 4)))

for a in itertools.product(notes, repeat =4):
    print(a)

print("4-notes melody - notes can repeat - it is variation with repeating - there are {} possibilities".format(pow(len(notes), 4)))
