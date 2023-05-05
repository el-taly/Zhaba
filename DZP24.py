#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Нахождение максимального кол-ва ягод черники, собранных с 3-ех кустов


print("Введите кол-во кустов черники: ")
n=int(input())
print("Введите кол-во черники на каждом кусте:")
i=0
list_1=[]

for i in range(n):
    list_1.append(int(input()))
print("Черника на кустах", list_1)

list_1 = list_1 + list_1[ : 2]
m=0
for i in range(1, n-1):
    
    m=max(m, list_1[i] + list_1[i+1] + list_1[i+2])
    
    
print(m)


