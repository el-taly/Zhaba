
print("Количество журавликов равно:")
s=input()
s=int(s)
if s % 6 == 0:

    p=int(s/6)
    k=int(s/3*2)

    print(p, p, p*4)
else:
    print("Такого кол-ва журавликов быть не может!")