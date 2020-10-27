#1. Создать список
# и заполнить его элементами
# различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

my_list = []

#string type data
my_list.append(str("python"))

#integer type data
my_list.append(int(2020))

#float type data
my_list.append(float(45.78))

#complex
my_list.append(complex(2, 5))


#list type data
my_list.append(['one', 'two', 'three']);

#tuple
my_list.append(('one', 'two', 'three'));

#dict
my_list.append({"one", 'two'})

#boolean
my_list.append(True)

#frozenset
my_list.append(frozenset("python"))

#bytes
my_list.append(bytes('python', encoding='utf-8'))

#bytesarray
my_list.append(bytes([20, 30, 40]))

#NoneType
my_list.append(None)

#ZeroDivisionError: division by zero - exception
my_list.append(ZeroDivisionError)

for el in my_list:
  print(el, " type of: ", type(el))

print(my_list)
