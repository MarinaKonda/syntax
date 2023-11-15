# *** Коллекции ***

# Кортеж (typle)

# Упорядоченная неизменяемая (иммутабельная) коллекция

# создание предварительно заполненного кортежа
tuple_1 = (10, 20, 30, 0, 5, 3)
tuple_1 = tuple([1, 100, 3.14, "python"])
tuple_1 = tuple("hello, tuple")

# чтение значений
val_1 = tuple_1[-1]

# срез кортежа
slice_1 = tuple_1[2:6]
slice_1 = tuple_1[::-1]

# print(slice_1)


# Словарь (dict, dictionary)

# Неупорядоченная изменяемая коллекция

# Элемент словаря - пара "ключ-значение"

# создание пустого словаря
dict_1 = {}
dict_1 = dict()

# создание предварительно заполненного словаря
dict_2 = {7:1000, 0:3.14, 'A':20, "abc":"python", "кортеж":(1,2,3)}

lst_1 = [(10, 20), ('k', 'v'), (3, dict_2)]
dict_3 = dict(lst_1)

dict_3 = dict(a=200, b=300)

# чтение значения 
val_1 = dict_2[0]
val_1 = dict_2['A']

# добавление пары
dict_2['B'] = 888
dict_2['C'] = "hello"

# замена значения 
dict_2['A'] = 200

# удаление пары
del dict_2['B']
# del dict_2['C']

# методы
print(dict_2)

items_0 = list(dict_2.items())
values_0 = list(dict_2.values())
keys_0 = list(dict_2.keys())

val_2 = dict_2.pop('A')


print(val_2)
print(dict_2)