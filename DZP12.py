# 2 натуральных числа X и  Y (X,Y <= 1000) X+Y=S X*Y=P

x = int(input('Введите первое число X от 1 до 1000 '))
y = int(input('Введите второе число Y от 1 до 1000 '))

S = x + y
P = x * y
Q = 0
for i in range(1001):
    if Q != 1:
        for j in range(1001):
            if Q != 1:
                if i * j == P and i + j == S:
                        print(P, S, i, j)
                        Q = 1
            else:
                j = 1001
        else:
            i = 1001
