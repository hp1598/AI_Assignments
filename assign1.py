# -*- coding: utf-8 -*-
"""assign1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EFL6TwsAm2Vgqy4ydj1DXSI6UnP1a-5c
"""

#question1

import pandas as pd
a=[{'keys':'shangai', 'values':17.8},{'keys':'istanbul', 'values':13.3},{'keys':'karachi','values':13.0},{'keys':'mumbai', 'values':12.5}]
population=pd.DataFrame(a)

print(population)



#question2

import pandas as pd
animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3,4,2,8,2,4], 'rabbits': [2, 3, 3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}
print(animals['dogs'])


print(animals['dogs'][3])


print(animals['fish'])

#question3

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a) - len(b))

#question4

tuple_a = 3, 4
tuple_b = (3, 4)

print(tuple_a == tuple_b)
print(tuple_a[1])

#question5

names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))