import math
import time

formulas_list = [
    "abs(x**3 - x**0.5)",
    "abs(math.sin(x) * x**2)"
]

argument_list = []

for i in range(10000):
    argument_list.append(i/10)

for formula in formulas_list:
    results_list = []
    print('Formula: {}'.format(formula))

    start = time.perf_counter()

    for x in argument_list:
        results_list.append(eval(formula))
    
    stop = time.perf_counter()
    print('name: {} min: {} max: {} time: {}'.format(formula, min(results_list), max(results_list), (stop - start))) 

for formula in formulas_list:
    results_list = []
    print('Formula: {}'.format(formula))

    start = time.perf_counter()

    compiled_formula = compile(formula, formula, 'eval')

    for x in argument_list:
        results_list.append(eval(compiled_formula))
    
    stop = time.perf_counter()
    print('name: {} min: {} max: {} time: {}'.format(formula, min(results_list), max(results_list), (stop - start))) 