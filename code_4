#ПРАКТИЧЕСКАЯ 4
#_______________1
#1.1
num = int(input("Введите целое число: "))
if num < 0:
    result = -num
elif num == 0:
    result = 1
else:
    result = num
print(result)

#1.2
text = input("Введите строку: ")
dot = False
comma = False

for i in text:
    if i == '.':
        dot = True
    if i == ',':
        comma = True

if dot or comma == True:
    print(True)
else:
    print(False)

#1.3
num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))

div1 = num1 % 3 == 0
div2 = num2 % 3 == 0

if div1 and div2:
    print(True)
elif div1 or div2:
    print("Одно число делится на 3")
else:
    print(False)
#_______________2
#2.1
x = int(input("Введите число: "))
y = "*" * x 
if x > 100:
    print("*")
elif x < 0:
    print()
else:
    print(y)
#2.2
x = input("Введите первую строку: ")
y = input("Введите вторую строку: ")
if x == y:
    print(True)
else:
    print(False)

#2.3
r = int(input("Введите значение красного: "))
b = int(input("Введите значение голубого: "))
g = int(input("Введите значение зеленого: "))
if r == 0 and g == 0 and b == 0:
    print("Черный цвет")
elif r == 255 and g == 255 and b == 255:
    print("Белый цвет")
elif r == 255 and g == 0 and b == 0:
    print("Красный цвет")
elif r == 0 and g == 255 and b == 0:
    print("Зеленый цвет")
elif r == 0 and g == 0 and b == 255:
    print("Голубой цвет")
else:
    print("Нет цвета")
#_______________3
#3.1
a = int(input("Введите число:"))
if a > 0:
    print(a-1, a, a+1)
else:
    a = 1
    print(a-1, a, a+1)
#3.2
text = input("Введите имя файла с расширением: ")

if ".doc" in text:
    print("Word file")
elif ".py" in text:
    print("Python file")
elif ".txt" in text:
    print("Text file")
else:
    print("Неизвестное расширение")

#3.3
a = int(input("Введите первую сторону:"))
b = int(input("Введите вторую сторону:"))
c = int(input("Введите третью сторону:"))
if a == b == c:
    print("Равносторонний")
elif a != b != c:
    print("Разносторонний")
else:
    print("Равнобедренный")
#_______________4
#4.1
text = 'important information in one line'
letter = input("Введите букву: ")

found = False
for i in text:
    if i == letter:
        found = True
        break
print(found)
#4.2
a = int(input("Введите первое целое число:"))
b = int(input("Введите второе целое число:"))
if a != b:
    print("Прямоугольник")
    c = a*b
    print("Площадь:", c)
else:
    print("Квадрат")
    c = a*b
    print("Площадь:", c)
#4.3
print("Как дела?")
say = input("Отвечай:")

if say == "Хорошо" or say == "Нормально" or say == "Отлично":
    print(":)")
elif say == "Плохо" or say == "Не хорошо" or say == "..." or say == "Ужасно":
    print(":(")
else:
    print("0_0")
#_______________5
#5.1
a = int(input("Введи первое целое число:"))
b = int(input("Введи второе целое число:"))
if a > b:
    print(a**b)
elif b > a:
    print(b**a)
else:
    print(a+b)
#5.2
new_massange = "Hello! How are you"
you = input("Ваш ответ:")
if new_massange[0] == you[0]:
    print(True)
else:
    print(False)
#5.3
a = int(input("Длина для первого:"))
b = int(input("Длина для второго:"))
if a > b:
    print("Первый отрезок длиннее на", a - b)
elif b > a:
    print("Второй отрезок длинне на", b - a)
else:
    print("Они равны")
#_______________6
#6.1
text = input("Введите строку:")
if text[0] == text[-1]:
    print(True)
else:
    print(False)
#6.2
a = int(input("Введите число:"))
if a % 2 == 0:
    print(a**2)
elif a % 3 == 0:
    print(a**3)
else:
    print(a * 100)
#6.3
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
if a < 0 and b < 0:
    print(False)
elif a > 0 and b > 0:
    print(True)
elif a < 0 and b > 0:
    a += 1000
    print(a, b)
else:
    b += 1000
    print(a, b)
#_______________7
