# Напишите программу, которая
# 1, принимает на вход цифру, обозначающую день недели,
# 2 и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# i = int(input('Введите номер дня недели (от 1 до 7)'))
# print ('нет') if i=1-5 elif i= 6 or i=7 print ('да')
# if i != 1-7:
#      print ('Введите корректное число')

# weekdays = [1, 2, 3, 4, 5]
# weekend = [6, 7]
# i = input('Введите номер дня недели (от 1 до 7): ')
# if i in weekdays:
#     print ('нет')
# elif i in weekend:
#     print ('да')
# else: print ('Введите корректное число')

num = int(input('Введите номер дня недели (от 1 до 7): '))
if (num == 1 or num == 2 or num == 3 or num == 4 or num == 5):
    print('нет')
elif (num == 6 or num == 7):
    print('да')
else:
    print('Введите корректное число')
