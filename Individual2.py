print('Есть ли четные числа?')
a, b, c = int(input("Введите a: ")), int(input("Введите b: ")), int(input("Введите с: "))
if (a + b) % 2 != 0:
    print('Да')
elif (b + c) % 2 != 0:
    print('Да')
elif (a + c) % 2 != 0:
    print('Да')
else:
    print('Нет')