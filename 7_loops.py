# *** ЦИКЛЫ ***

# Оператор while (пока)

# бесконечный цикл
# while True:
#     print("hello!")

# цикл с условием
val_1 = 0

# while val_1 <= 10:
    # print(f"значение": {val_1})
#     val_1 = val_1 + 1
    # val_1 += 1

# прерывание цикла по дополнительному условию

# while True:
#     val = input("Введите имя: ")
#     if val == "stop":
#         print("bye-bye")
#         break
#     print(f"Привет, {val}!")

# пропуск части кода тела цикла

val_1 = 0

# while val_1 < 20:
#     # 1 кусок кода
#     print(val_1)
#     val_1 += 1

#     if val_1 < 10:
#         continue

#     # 2 кусок кода
#     print("hello")

# Оператор for

# 1. "чтение" значения из объекта с последовательностью по порядку
# 2. считанное значение присваивает в собственную переменную
# 3. выполняет код тела

lst_0 = [10, 20, 4, 3, 100, 234]

# for v in lsy_0:
#     v *= 100
#     print(v)

dict_0 = dict(a=100, b=200, c=300)

# print(dict_0)

# for item in dict_0.items():
#     print(item)

# for k, v in dict_0.items():
#     print(k, v)

# val_1, val_2, val_3 = (100, 200, 300)

# print(val_1, val_2, val_3)

# for k in dict_0.values():
#     print(k)

# класс range()

# r = range(10)
r = range(-10, 10, 2)
# print(r)

tuple_0 = tuple(r)

# print(tuple_0)

# for v in r:
#     print(v)

for _ in range(5):
    print("hello")

    # генератор списка (кортежа) дз
    # генератор словаря (for)