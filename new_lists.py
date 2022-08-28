from typing import List
from functools import reduce

""" Write code that creates three new lists. Here are their contents:
Each number in the floats list is raised to the third power and rounded to three decimal places.
From the names list, only those names are taken that have at least five letters.
The product of all numbers is taken from the numbers list. """

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

print(list(map(lambda x: round(x ** 3, 3), floats)))
print(list(filter(lambda x: len(set(x)) >= 5, ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"])))
print(reduce(lambda prev, el: prev * el, [22, 33, 10, 6894, 11, 2, 1]))