#! /usr/bin/env python
# -*- coding: utf-8 -*-

dict_eng = {1: 'aeioulnstr', 2: 'dg',3: 'bcmp', 4: 'fhvwy', 5: 'k', 8: 'jx', 10: 'qz'}



print('Введите слово: ')

list_1=input()

z = [k for letter in list_1 for k,v in dict_eng.items() if letter in v]

print(sum(z))