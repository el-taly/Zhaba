#! /usr/bin/env python
# -*- coding: utf-8 -*-


print("Введите длину массива: ")
n=int(input())

print("Введите элементы массива:")
i=0
list_1=[]

for i in range(n):
    list_1.append(int(input()))
    
print("Массив А: ", list_1)

X=int(input("Введите число X: "))

m=1
d=3001
y=1


for i in list_1:
    m = abs(X-i)
    
    if m < d:
        d = m
        y = i
        

print("Самый близкий по величине элемент: ", y)



