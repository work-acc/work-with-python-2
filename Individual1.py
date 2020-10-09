n = int(input("Введите, сколько кВт/ч клиент израсходовал: "))
if n <= 250:
    y = 7 * n
elif n > 250 and n <= 300:
        y = 17 * n
else:
        y = 20 * n
print(f"y = {y}")
