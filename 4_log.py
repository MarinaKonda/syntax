# операции сравнени

x = 3
y = 5

# операция равенства (равно)
# мы спрашиваем "значение x равно y?"
res = x == y

# операция неравенства (не равно)
# мы спрашиваем "значение x не равно y?"
res = x != y

# операция "меньше"
# мы спрашиваем "значение x меньше значения y?"
res = x < y

# операция "больше"
# мы спрашиваем "значение x больше значения y?"
res = x > y

# операция "меньше либо равно"
# мы спрашиваем "значение x меньше либо равно значению y?"
res = x <= y

# операция "больше либо равно"
# мы спрашиваем "значение x больше либо равно значения y?"
res = x >= y

# print (res)

# логические операции

var_1 = True
var_2 = False

#  оператор "НЕ" (NOT, операция инверсия)
res = not var_1

res = not var_2

# оператор "И" (AND, операция конъюкция)
# логическое умножение
# возвращает True только тогда, когда оба значения True

res = var_1 and var_2

# оператор "ИЛИ" (OR, операция дизъюкция)
# логическое сложение
# возвращает False только тогда, когда оба значения False

res = var_1 or var_2

# print(res)

# отступы в python очень важны
# по отступам интерпретатор ориентируется во вложенности кода
# используйте tab - перемещение курсора вправо на один отступа
# Backspace либо Shift+Tab - перемещение курсора влево на один отступ
# ******

# условные операции

a = 0

# оператор if (если)
# if a == 0:
    # print("равно 0")

condition = a < 5

# if condition:
    # print("меньше 5")

    # оператор else (иначе)

a = 11

# if a <= 10:
#     res = "hello!"
# else:
#     res = "bye-bye!"

# print(res)

# оператор elif (else if)
a = 0

# if a > 0:
#     res = "больше нуля"
# elif a < 0:
#     res = "меньше нуля"
# else:
#     res = "равно нулю"

char = 'a'

if char == 'A':
    res = "буква A"
elif char == 'B':
    res = "буква B"
elif char == 'C':
    res = "буква C"
else:
    res = "другой символ"

print(res)