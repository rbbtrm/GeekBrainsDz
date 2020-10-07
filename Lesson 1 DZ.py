#1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

# name = input('Enter your Name: ')
# surname = input('Enter your Surname: ')
# age = int(input('Enter your Age: '))
# salary =int(input('Enter your Salary: '))

# print('Your name is: {}, Your surname is: {}, your age is: {}, Your salary is: {} .'.format(name ,surname, age, salary))

#2.Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

# import datetime
# hh = datetime.datetime.now().hour
# mm = datetime.datetime.now().minute
# ss = int(input('insert seconds :'))

# print(f'Time: {hh}:{mm}:{ss}'.format(str(hh),str(mm), str(ss)))

#3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

# n = int(input('Enter your Number: '))
# nn = int(str(n)+str(n))
# nnn = int(str(nn)+str(n))
# print(n+nn+nnn)

#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

# long_number = str(input('Insert Long Number: '))
# max_value = 0
# index = 0

# if long_number.isdigit() != True:
#     print("It's not number or not more than Zero!")
# elif int(long_number) <= 0:
#     print("It's not more than Zero!")
# else:
#     while index < len(long_number):
#         if int(max_value) < int(long_number[index]):
#             max_value = long_number[index]
#         index += 1
#
# print(f"Max number are: {max_value}")


#5. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который результат спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b и  выводить одно натуральное число — номер дня.
# reached_day = int(input("Первый день его результат составил в километрах: "))

# distance = int(input("Результат дистанции спортсмена составит: "))
# reached = 0
# duration_day = 1
#
# while reached < distance:
#     if duration_day > 1:
#         reached_day += (reached_day * 10) / 100
#
#     reached = reached_day
#     print(f"Distence per {duration_day} day: {reached_day} km")
#     print(f"Reached distance {reached} km")
#
#     if reached < distance:
#         duration_day += 1
#
# print(f"Distance completed on the {duration_day}-th day!")

# #6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который результат спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b и  выводить одно натуральное число — номер дня.
# reached_day = int(input("Первый день его результат составил в километрах: "))
# distance = int(input("Результат дистанции спортсмена составит: "))
# reached = 0
# duration_day = 1
#
# while reached < distance:
#     if duration_day > 1:
#         reached_day += (reached_day * 10) / 100
#
#     reached = reached_day
#     print(f"Distence per {duration_day} day: {reached_day} km")
#     print(f"Reached distance {reached} km")
#
#     if reached < distance:
#         duration_day += 1
#
# print(f"Distance completed on the {duration_day}-th day!")
