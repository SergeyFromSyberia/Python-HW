# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
list = []
num = int(input("Введите число: "))
j = -num
while j!= num +1:
    list.append (j)
    j+=1
print (list)
list2 = []
data = open('file.txt', 'r')
for line in data:
    list2.append(int(line))
print (list2)
data.close()
i = 0
multiplication = 1
lenght = len(list2)
while i != lenght:
    multiplication *= int(list[list2[i]])
    i+=1
print(multiplication)