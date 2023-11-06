# *** Типы данных ***

# целочисленные значения (int, integer)
mu_int = 100

# числа с плавающей точкой (вещественные числа) (float)
my_float = 3.14

# строковые типы данных (символ, слово, текст) (str, string)

my_str_1 = 'python'
my_str_2 = "мой текст"
my_char = 'A'

my_text_2 = 'мой "текст" с кавычками'

# способы форматирования строк

# 1. Конкатенация строк - старый способ
str_1 = "Hello"
str_2 = "World"

num_1 = 8763

res = str_1 + ' ' + str_2 + str(num_1)

# print(res)

# 2. f-string - новый способ
str_3 = "число = "
num_2 = 100.25371625

# res = f"{str_3}{num_2}"
res = f"число = {num_2:.3f}"

# print(res)

# методы строк

str_4 = "Hello, World!"

# res = str_4.upper()
# res = str_4.lower()
res = str_4.split(',')

# print(res)

# Булевы типы данных (bool, boolean)
# в честь Джордж Буль (булева алгебра)

# логическая 1 True
# логический 0 False

bool_1 = True 
bool_2 = False 

# Арифметические операции

a = 10
b = 3

# сложение
res = a + b

# вычитание
res = a - b

# умножение
res = a * b

# обычное деление
# результат всегда будет float
res = a / b

# целочисленное деление
# результат всегда будет int (целое число)
res = a // b

# деление по остатку
b = 2
res = a % b

# возведение в степень 
res = a ** b

# извлечение из корня
import math

res = math.sqrt(100)

print(res)