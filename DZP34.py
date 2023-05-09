#! /usr/bin/env python
# -*- coding: utf-8 -*-
# VinniPuh

def ritm(str):
    str =str.split()
    list_1 = []
    for word in str:
        summa = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                summa +=1
        list_1.append(summa)
    return len(list_1) == list_1.count(list_1[0])

str1 = 'пам-па-пам пам-па-пам'
if ritm(str1):
    print('Парам пам-пам')
else:
    print('Пам парам')


