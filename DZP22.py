#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 2 неупорядоченных набора целых чисел, выдать все те числа, которые встрчаются в обоих наборах без повторений


print("Введите длину массива А: ")
n=int(input())
print("Введите элементы массива А:")
i=0
list_1=[]

for i in range(n):
    list_1.append(int(input())) 
print("massiv A: ", list_1)


print("Введите длину массива В: ")
m=int(input())

print("Введите элементы массива В:")
i=0
list_2=[]

for i in range(m):
    list_2.append(int(input()))
    
print("massiv B: ", list_2)

rez = []

for i in list_1:
    for j in list_2:
        if i == j:
            print(i)
            rez.append(i)

print(rez)
