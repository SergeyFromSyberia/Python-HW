# Напишите программу, которая
# принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится)
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

coordinateX = int(input('Введите координату X: '))
coordinateY = int(input('Введите координату Y: '))
if (coordinateX > 0 and coordinateY > 0):
    print("точка находится в четверти № 1")
if (coordinateX < 0 and coordinateY < 0):
    print("точка находится в четверти № 3")
if (coordinateX > 0 and coordinateY < 0):
    print("точка находится в четверти № 4")
if (coordinateX < 0 and coordinateY > 0):
    print("точка находится в четверти № 2")
