from sys import argv
from itertools import product
from os import path

level = int(argv[1])

types = ['description', 'choice']

nums = list(product(range(2), repeat=level - 1))

for i in nums:
    st = ""
    for x in i:
        st += str(x)
    for text in types:
        filename = f'../text/{text}s/{text}{level}_{str(st)}.txt'
        if not path.exists(filename):
            file = open(filename, "w")
