#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

#list
month_interval = [
  {"start":12, "end":2, "season":"winter"},
  {"start":3, "end":5, "season":"spring"},
  {"start":6, "end":8, "season":"summer"},
  {"start":9, "end":11, "season":"outem"}
]
# print(month_interval[0]['start'])
while True:
  month_number = input("Get season by month number or type exit to exit: ")
  if month_number == 'exit':
    break

  month_number = int(month_number)
  if month_number > 0 and month_number <=12:
    for el in month_interval:
      # print(el, el['start'], el['season'])
      if month_number == el['start'] or month_number <= el['end']:
        print(el['season'])
        break
  else:
    print('Out of season month requirements! Try again!')
