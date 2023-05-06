#! /usr/bin/env python
# -*- coding: utf-8 -*-

# заполнить массив элементами арифметической прогрессии

print("Введите первый элемент: ")
a=int(input())

print("Введите длину массива А: ")
n=int(input())

print("Введите шаг арифметической прогрессии А: ")
l=int(input())

list_1=[]

for i in range(1, n+1):
    list_1.append(a + (i-1)*l)
print(list_1)