# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 17:51:43 2026

@author: egors
"""

# %%

from random import randint


rand_list = []

for _ in range(10):
    rand_list.append(randint(0, 10))

print(rand_list)

sum = 0

for num in rand_list:
    if(num%2 == 0):
        sum+=num;

print(sum)

# %%