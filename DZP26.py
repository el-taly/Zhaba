#! /usr/bin/env python
# -*- coding: utf-8 -*-

# На вход подается 2 числа Аи В, а возводит в целую степень В с помощью рекурсии

def grad(a, exp):
    if exp == 1:
        return a
    else:
        return (a*grad(a, exp-1))

print('Введите число А" ')
a = int(input())

print('Введите В - степень числа А" ')
exp = int(input())
print("Itog: ", grad(a, exp))


