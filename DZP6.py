# Счастливый билет, когда сумма трех первых чисел равна трем последним

print("Введите номер счастливого билета 6 знаков:")
s=input()
s=int(s)

x1=s % 10
print(x1)

y1=int(s / 10) % 10
print(y1)

z1=int(s/100) % 10
print(z1)

Summ1=x1+y1+z1
print(Summ1)

x2=int(s/100000)
print(x2)

y2=int(s/10000)%10
print(y2)

z2=int(s/1000)%10
print(z2)

Summ2=x2+y2+z2
print(Summ2)

if Summ1==Summ2:
    print("Этот билет счастливый!")

else:
    print("Этот билет несчастливый")

