#2. Для списка
# реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

collation = []

while True:
  new_input = input("Insert new item in list or set[exit] to exist: ")

  if new_input == 'exit':
    break

  collation.append(new_input)
  print("Our list: ", collation)

last_index = 0
i = 0
print(len(collation))
while i<len(collation):
  if (i % 2) > 0 and i > 0:
    prev_value = collation[i-1]
    collation[i-1] = collation[i]
    collation[i] = prev_value

  i+=1

print(collation)
