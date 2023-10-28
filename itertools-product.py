from itertools import product

list1 = [1, 2, 3]
list2 = ['A', 'B', 'C']

for item1, item2 in product(list1, list2):
    print(f"item1: {item1}, item2: {item2}")
