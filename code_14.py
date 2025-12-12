#Зададние 1
while True:
    try:
        a = input('Ввод: ')
        a = int(a)
    except ValueError:
        print(a, '- не число. Повторите ввод.')
    else:
        break
for i in range(a + 1):
    print(i, end=" ")
print(end=" \n")

#Зададние 2

any_list = [4, 3.2, 16, 9, 13.5, 67]
for i, v in enumerate(any_list):
    try:
        print(v, "/", i, '=', v/i)
    except ZeroDivisionError:
        print(f"Деление на 0! Элемент: {any_list[0]}")

#Зададние 3
massiv = []
while len(massiv) < 5:
    try:
        y = int(input("Ввод:"))
        massiv.append(y)
    except ValueError:
        continue
print(f"Числа в списке: {massiv}")
