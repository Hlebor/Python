#Задание 1
def alpha(x):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    z = []
    o = []
    for i in x:
        if i in alphabet and i not in z:
            z.append(i)
    for i in alphabet:
        if i not in z:
            o.append(i)
    print(' '.join(alphabet))
    print(' '.join(z + o))

alpha('пайтон')

#Задание 2
def create_calendar(month, year, days):
    print(f"calendar: {month} {year}")
    for i in range(days):
        if (i + 1) % 7 == 0:
            print(i + 1, end="\n")
        else:
            print(i + 1, end=" ")

create_calendar('Randomner', 2045, 23)
print (end="\n")

#Задание 3
def bin_sys(x, y):
    summ = 0
    for i in range(x, y + 1):
        summ += i
        print(bin(i)[2:])
    print(f"сумма: ", bin(summ)[2:])

bin_sys(3,6)

#Задание 4
field = [['[ ]', '[ ]', '[ ]'],
        ['[ ]', '[ ]', '[ ]'],
        ['[ ]', '[ ]', '[ ]']]

def begin(massiv, stroka, stolbets):
    global field
    massiv[stroka][stolbets] = " * "
    print(massiv[0])
    print(massiv[1])
    print(massiv[2])

begin(field, 1, 2)

#Задание 5
def _numbers(n1, n2 = 1):
    print(f"[{n1}] [{(n1 + 1) * n2}]\n[{(n1 + 2) * n2}] [{(n1 + 3) * n2}]")

_numbers(1)

#Задание 6
def exam(text, b):
    text_lower = text.lower()
    b_lower = b.lower()
    result = text_lower.count(b)
    print(result)

exam('My name is Sara.', 's')
