# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
#
products = []

while True:
  title_product = str(input("Add new product title or type exit: "))

  if title_product == 'exit':
    break

  price_product = int(input("Price per product: "))
  entity_product = int(input('Entity product: '))
  measuring_product = str(input("Type measuring product: "))
  products.insert(len(products), (len(products)+1, {"название": title_product, "цена": price_product, "количество":entity_product, "ед.":measuring_product}))
  print(products)

analitics = {"название":[], "цена":[], "количество":[], "ед.":[]}
if len(products):
  for item in products:
    analitics["название"].append(item[1]["название"])
    analitics["цена"].append(item[1]["цена"])
    analitics["количество"].append(item[1]["количество"])
    analitics["ед."].append(item[1]["ед."])

analitics["название"] = list(dict.fromkeys(analitics["название"]))
analitics["цена"] = list(dict.fromkeys(analitics["цена"]))
analitics["количество"] = list(dict.fromkeys(analitics["количество"]))
analitics["ед."] = list(dict.fromkeys(analitics["ед."]))

print("Аналитика по товарам готова!")
while True:
  show_or_exit = int(input("Type 1 - to get products list, 2 - to get analitics, 3 - exit: "))
  if show_or_exit == 1:
    print(products)
  elif show_or_exit == 2:
    print(analitics)
  else:
    break


# Пример готовой структуры:
#
# [
#
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
#
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик,
# например список названий товаров.
#
# Пример:
#
# {
#
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
