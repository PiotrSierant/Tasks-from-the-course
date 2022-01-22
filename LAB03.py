price = 123
bonus = 23
bonus_granted = True

price = price - bonus if bonus_granted else price

print(price)


rating = 5

print('very good' if rating == 5 else 'good' if rating == 4 else 'weak')