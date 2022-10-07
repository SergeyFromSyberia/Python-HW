# Напишите программу, которая будет
# преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input("Введите десятичное число: "))
list1 = []
x = 0
y = 1
z = 0
while number != 0:
    x = int(number % 2)
    number = int(number / 2)
    list1.append(x)
list1 = list(reversed(list1))
i = 0
while i < len(list1):
    print (list1[i], end='')
    i+= 1
