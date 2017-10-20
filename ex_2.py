#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data3 = ['a', 'A', 'B', 'b']
data4 = ['a', 'A', 2, 6, 2, 'B', 'b']

for i in Unique(data1):  # со списком из чисел
    print(i, end=', ')
print()
for i in Unique(data2):  # c генератором чисел
    print(i, end=', ')
print()
for i in Unique(data3):  # cо списком строк, не игнорируя регистр
    print(i, end=', ')
print()
for i in Unique(data3, ignore_case=True):  # cо списком строк, игнорируя регистр
    print(i, end=', ')
print()
for i in Unique(data4, ignore_case=True):  # cо смешанным списком строк и чисел, не игнорируя регистр
    print(i, end=', ')
