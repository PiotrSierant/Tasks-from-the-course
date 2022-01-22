def amount_color(listcolor, amount=1):
    return listcolor[:amount]


colors = ["red", "orange", "green", "violet", "blue", "yellow"]

print(amount_color(colors, amount=3))

for i in range(1, len(colors)+1):
    print(amount_color(colors, i))

x = 'Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli. '

print(x[x.index('(')+1:x.index(')')+1])
