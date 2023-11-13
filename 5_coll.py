# *** Коллекции ***

# Списки (list)

# Список - это упорядоченная (проиндексированная), изменяемая (мутабельная) коллекция

# объекты внутри списка - элементы
# каждый элемент проиндексирован

# создание пустого списка
lst_1 = []
lst_1 = list()

# создание предварительно заполненных списков
lst_2 = [10, 3, 100, 77]
lst_3 = [10, 20, 3.14, "python", 'A', [1,2,3]]
lst_4 = list("python")

# добавление элемента (объекта) в список
# print(lst_3)

lst_1.append(100)
lst_1.append("hello")
lst_1.append('$')

lst_3.append("привет")

# чтение значений элементов
# прямая индексация (слево направо)
el_1 = lst_3[0]

# lenght = len(lst_3)
# last_el = lst_3[lenght - 1]

#обратная индексация (справа налево)
last_el = lst_3[-1]

# замена значений
lst_3[1] = 777

# удаление элемента
# по индексу
# del lst_3[-2]

# по значению
lst_3.remove(777)

# очистка списка
lst_3.clear()

# срезы списка (кусеи)
lst_5 = list("Hello, World!")

# срез от начала до конца
slice_1 = lst_5[0:13]
slice_1 = lst_5[:]

# срез от начала до индекса B (не включительно)
slice_1 = lst_5[:6]

# срез от индекса А до конца исходного списка

slice_1 = lst_5[6:]

# срез от индекса А до индекса В (не включительно)

slice_1 = lst_5[4:8]

# срез от начала до конца с шагом  2
slice_1 = lst_5[::2]

print(slice_1)


