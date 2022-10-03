# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

num = int(input("Введите число: "))
i = 1
list = []
forlist = 1
while i != num + 1:
    forlist = (1+1/i)**i
    list.append(forlist)
    i += 1
lenght = len(list)
j = 0
sum = 0
while j != lenght:
     sum += list[j]
     j+=1
print (sum)