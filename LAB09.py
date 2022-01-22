banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2,
                   0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]

dict_denominations = {0.01: 0,
                      0.02: 0,
                      0.05: 0,
                      0.1: 0,
                      0.2: 0,
                      0.5: 0,
                      1: 0,
                      2: 0,
                      5: 0,
                      10: 0,
                      20: 0,
                      50: 0,
                      100: 0,
                      200: 0,
                      500: 0
                      }

dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1

dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2

dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

for key in dict_denominations:
    print("Denominate: {} - amount {}".format(key, dict_denominations[key]))

for key in dict_denominations:
    print(f"Denominate: {key} - amount {dict_denominations[key]}")

for k in sorted(dict_denominations.keys()):
    print("Denominate: {0:6.2f} - amount {1:3}".format(k, dict_denominations[k]))
