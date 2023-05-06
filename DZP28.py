#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Рекурсивную функцию для сложения двух чисел

def summa(a, b):
    if b == 0:
        return a
    if b > 0:    
        return (summa(a+1, b-1))
    return (summa(a-1, b+1))

print('Введите число А" ')
a = int(input())

print('Введите число В" ')
b = int(input())

print("Itog: ", summa(a, b))


