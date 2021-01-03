import random

print('кама-ножа-бумажа')


def gogogo():
    a = number()
    b = random.randint(1, 3)
    print(b)
    if a == 1 and b == 3:
        print('продул')
    elif a == 2 and b == 1:
        print('продул')
    elif a == 3 and b == 2:
        print('продул')
    elif a == b:
        print('ничья')
    else:
        print('вин')


def number():
    while True:
        getNumber = input()  # Ввод числа
        if getNumber == '1' or getNumber == '2' or getNumber == '3':
            c = int(getNumber)
            return c


game = True
while game is True:
    gogogo()
