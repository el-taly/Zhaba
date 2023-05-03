
print("Введите длину массива: ")
n=int(input())

print("Введите элементы массива:")
i=0
list_1=[]

for i in range(n):
    list_1.append(int(input()))
    
print("Массив А: ", list_1)

X=int(input("Введите число X: "))


m=0
for i in list_1:
    if (i == X):
        m=m+1
        print(m)
print("Число Х встречается: ", m, "раз")