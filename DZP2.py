
a=input("Введите трехзначное число: ")
a=int(a)
x=a % 10
print(x)

y=int(a / 10) % 10
print(y)

a=int(a/100)
print(a)

print(a, "+", y, "+", x, "=", a+y+x)

