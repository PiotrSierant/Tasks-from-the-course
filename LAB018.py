def double(x):
    return 2 * x


def square(x):
    return x**2


def negative(x):
    return -x


def div2(x):
    return x/2


def generate_values(func, x):
    results = []
    for value in x:
        results.append(func(value))

    return results


x_table = list(range(11))
print(generate_values(double, x_table))
print(generate_values(square, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))


'''
number = 10

transformations = [double, square, negative, div2]

tmp_return_value = number

print('Starting transformations')
for transformation in transformations:

    tmp_return_value = transformation(tmp_return_value)
    print('{}: temporal result is {}'.format(
        transformation.__name__, tmp_return_value))
'''
