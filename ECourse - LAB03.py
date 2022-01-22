# wyrażenia listowe
#lista = [10] * 20
# print(lista)

# kolekcje
#napis = 'abrakadabra'*7
# print(napis)

#lista2 = [10 for i in range(10)]
# print(lista2)

# lista [wyrazenia for element in kolekcja]
#lista3 = [litera for litera in 'Piotr Hello']
# print(lista3)

#lista4 = [int(liczba) for liczba in '0123456789']
# print(lista4)

#lista5 = [int(liczba) for liczba in input('Podaj liczby po spacjach: ').split()]
# print(lista5)

#x,y = [int(liczba) for liczba in input('Podaj liczby:').split()]
#print(f'To jest x: {x}, To jest y: {y}')

#slownik = {x: x*x for x in range(11)}
# print(slownik)

#lista = {y: [x for x in range(3)] for y in range(10)}
# print(lista)

#lista2 = [x.lower() for x in "Pioter"]
# print(lista2)

#lista3 = [x+y for x, y in ([2, 2],[3, 3])]
# print(lista3)

lista4 = [x+y for x, y in ([a, a+1] for a in range(50))]
print(lista4)

parzyste = [x*x for x in range(20) if x % 2 == 0]
print(parzyste)

napis = 'Piotr Sierant telefone +48666111666'
lista = [int(znak) for znak in napis if znak.isdigit()]
print(lista)
