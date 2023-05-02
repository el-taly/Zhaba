# Задано число n вывести все степени 2 меньше числа n

print("Введите число n:")
n=int(input())

q=0
m=2

for i in range(n):
    if q != 1:
        m = m ** i
        if m<=n:
            print (m)
            m=2
        else:
                q=1
    else:
        i=n