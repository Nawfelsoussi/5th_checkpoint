#Write a program to sort a tuple by its float element.
#For example: list= [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
#Expected result: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
lists = [
    ('item1', '12.20'),
    ('item2', '15.10'),
    ('item3', '24.5')
]

def num(item):
    return float(item[1])

lists.sort(key=num, reverse=True)

print(lists)
#done
