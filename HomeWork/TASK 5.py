""" Напишите программу, которая принимает на вход координаты двух точек 
и находит расстояние между ними в 2D пространстве. 
Пример: - A (3,6); B (2,1) -> 5,09 - A (7,-5); B (1,-1) -> 7,21 """


def inputNumbers(x):
    xy = ['X', 'Y']
    a = []
    for i in range(x):
        exit = False
        while not exit:
            try:
                number = int(input(f'Введите координату по {xy[i]}: '))
                a.append(number)
                exit = True
            except ValueError:
                print('Введите корректное значение (целое число)')
    return a


def calculateLengthSegment(a, b):
    lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return lengthSegment

print('Введите координаты точки А')
pointA = inputNumbers(2)
print('Введите координаты точки В')
pointB = inputNumbers(2)

print(f'Расстояние между точками = {format(calculateLengthSegment(pointA, pointB), ".2f")}')