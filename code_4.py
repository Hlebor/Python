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
#7.1
s = input("Введите строку:")
if s[-1] == "я" or s[-1] == "ю" or s[-1] == "е" or s[-1] == "и":
    print(True)
else:
    print(False)
#7.2
a = int(input("Введите 1 целое число:"))
b = int(input("Введите 2 целое число:"))
c = int(input("Введите 3 целое число:"))
if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or c + b <= a:
    print(False)
else:
    print(True)
#7.3
s = float(input("Введите число:"))
j = s%10
if j == 0:
    s **= 10
    print(s)
elif j == 1:
    s /= 3
    print(s)
elif j == 2:
    s /= 2
    print(s)
else:
    s **= 2
    print(s)
#_______________8
#8.1
passo = input("Введите пароль:")
if len(passo) < 8 or passo == "qwerty123":
    print(False)
else:
    print(True)
#8.2
pc_number = 777
a = int(input("Введите 1 число:"))
b = int(input("Введите 2 число:"))
if a < pc_number < b or b < pc_number < a:
    print(True)
else:
    print(False)
#8.3
lamp_1 = 0
lamp_2 = 0
answer = int(input("Какую лампочку зажечь?"))
if answer == 1:
    lamp_1 = 1
    print("Лампочка 1 зажжена:", lamp_1)
elif answer == 2:
    lamp_2 = 1
    print("Лампочка 2 зажжена:", lamp_2)
else:
    print("Обе лампочки не горят", lamp_1, lamp_2)
#_______________9
#9.1
switch_1 = False
switch_2 = False
print(switch_1, switch_2)
print("Включить?")
s = input()
if s == "да" or s == "Да":
    switch_1 = True
    switch_2 = True
print(switch_1, switch_2)
#9.2
a = int(input("Введите число:"))
if a >= 0 and a%2 == 0:
    print(True, "even")
elif a >= 0 and a%2 != 0:
    print(True, "odd")
else:
    print(False)
#9.3
stro = input("Введите строку:")
if stro[0] == "/":
    print("command")
else:
    print("It's string")
#_______________10
#10.1
a = input("Введите строку:")
if len(a) == 0:
    print(None)
elif len(a) <= 5:
    print("short")
elif len(a) >= 6 and len(a) <= 10:
    print("normal")
else:
    print("long")
#10.2
num = int(input("Введите число:"))
if num < 0:
    num = 1000000
    print(num)
elif num == 0:
    num = 2
    print(num**2)
else:
    print(num**3)
#10.3
number_1 = 10
number_2 = 100
b = int(input("Введите число:"))
if number_1 < b and b < number_2:
    print(True)
else:
    print(False)

#_______________11
#11.1
prog_num = 0
num1 = int(input("Введите первое число:"))
num2 = int(input("Введите второе число:"))

if num1 < 0 and num2 < 0:
    prog_num = num1 + num2
    print(prog_num)
elif num1 > 0 and num2 > 0:
    prog_num = num1 - num2
    print(prog_num)
else:
    print(False)

#11.2
num = int(input("Введите число:"))
if num % 2 != 0:
    print(num + 1)
else:
    print(True)

#11.3
text = input("Введите строку:")
if len(text) > 10:
    print(text[:5])
else:
    print(text)

#_______________12
#12.1
ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
en = "abcdefghijklmnopqrstuvwxyz"

letter = input("Введите букву:")

if letter in ru:
    print("rus")
elif letter in en:
    print("eng")
else:
    print(None)
#12.2
pc_num = 10
user_num = int(input("Введите: "))
if user_num == pc_num or user_num == pc_num - 1 or user_num == pc_num + 1:
    print(True)
else:
    print(False)
#12.3
print("(221 - 13) * 2")
correct1 = (221-13)*2

user = int(input("Введите ответ:"))
if user == correct1:
    print(True)
elif user > correct1:
    print(">")
else:
    print("<")
