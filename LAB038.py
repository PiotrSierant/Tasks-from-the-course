products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 2)]
customers = ['Customer {}'.format(i) for i in range(1, 5)]
 
def Generator(products, promotions, customers):
    for i in products:
        for j in promotions:
            for k in customers:
                yield("{} - {} - {}".format(i, j ,k))

for c in Generator(products, promotions, customers):
    print(c)