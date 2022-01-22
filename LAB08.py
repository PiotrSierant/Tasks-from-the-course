projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

# for pro, nam in zip(projects, leaders):
# print('The leader of', pro, "is", nam)

# for pro, nam, date in zip(projects, leaders, dates):
# print('The leader of', pro, "started", date, "is", nam)
patrz = enumerate(zip(projects, leaders, dates))

for number, (p, n, d) in patrz:
    print(number + 1, p, n, d)

for i, (p,l,d) in enumerate(zip(projects, leaders, dates)):
    print('{} - The leader of "{}" started {} is {}'.format(i+1,p,d,l))