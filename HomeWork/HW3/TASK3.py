# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# минимальное значение дробной части отличное от нуля, у целых чисел дробной части нет их в расчет не берем
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
def FillList(x):
    i = 1
    list = []
    while i <= x:
        list.append(float(input(f"Введите число {i}: ")))
        i += 1
    return list


size = int(input("Сколько чисел будет в списке?: "))
list = FillList(size)
print(list)
i = 1
max = float(list[0] % 1)
min = float(list[0] % 1)
while i < size:
    end = float(list[i] % 1)
    if end > max:
        max = end
    if end < min:
        min = end
    i += 1
result = max - min
print(f'=> {str(result)[:4]}')