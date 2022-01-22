import time
import sys


class Combinations:
    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers

    def __getitem__(self, item):
        if item >= len(self.products) * len(self.promotions) * len(self.customers):
            raise StopIteration

        else:
            pos_product = (
                item // (len(self.promotions) * len(self.customers)))
            item = (item % (len(self.promotions) * len(self.customers)))
            pos_promotions = (item // len(self.customers))
            item = item % len(self.customers)
            pos_customers = item

            return "{}, {}, {}".format(self.products[pos_product], self.promotions[pos_promotions], self.customers[pos_customers])


products = ["Product {}".format(i) for i in range(1, 5)]
print(products)

promotions = ["Promotion {}".format(i) for i in range(1, 2)]
print(promotions)

customers = ['Customer {}'.format(i) for i in range(1, 5)]
print(customers)

combinations = Combinations(products, promotions, customers)

# for i in range(0, 30):
#print(i, combinations[i])

# for c in combinations:
# pass

#print('RAM: {}'.format(sys.getsizeof(combinations)))

combinations2 = iter(combinations)

for i in combinations2:
    print(i)