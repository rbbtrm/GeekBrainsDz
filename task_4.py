#4. Пользователь вводит строку из нескольких слов,
# разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.


while True:
  insert_paragraph = str(input("Insert simple paragraph or type exit: "))

  if insert_paragraph == 'exit':
    break

  split_paragraph = insert_paragraph.split(" ")

  for index, word in  enumerate(split_paragraph, 1):

    if len(word) > 10:
      word = word[0:10]

    print(f"{index}.{word}")
