# Напишите программу, которая
# найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
def get_list_from_user(x):
    list = []
    i = 1
    while i <= x:
        list.append(int(input(f"Введите {i} число ")))
        i += 1
    return list

count_numb = int(input("Сколько чисел будет в списке?"))

spisok = get_list_from_user(count_numb)
print(spisok)
i = 0
g = -1
mult = 1
finalList = []

if count_numb % 2 == 0:
    while i < int(count_numb/2):
        mult = spisok[i] * spisok[g]
        finalList.append(mult)
        i += 1
        g -= 1
else:
    while i < int(count_numb/2):
        mult = spisok[i] * spisok[g]
        finalList.append(mult)
        i += 1
        g -= 1
    mult = spisok[i] * spisok[g]
    finalList.append(mult)
print(finalList)
