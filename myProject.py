# Программа с графическим пользовательским интерфейсом (GUI)

# *** Генератор паролей ***

from tkinter import Tk, Label, Entry, Button, StringVar
import hashlib as h

def pwdGenerator(pwd_str):
    # кодирование в байт-строку
    byte_str = pwd_str.encode()
    # хэширование
    hash_str = h.sha256(byte_str)
    # преобразование объекта хэш-строки в обычную строку шестнадцетиричныхи значений
    hex_str = hash_str.hexdigest()[:10]
    # возрат хэш-строки
    return hex_str

# тестирование функции
# while True:
#     pwd = input("Введите пароль: ")
#     if pwd == "stop":
#         break
#     print(pwdGenerator(pwd))

# объект окна
window = Tk()

# объекты для хранения строк
raw_pwd = StringVar()
hash_pwd = StringVar()

# виджет (компонент) текстовой метки
Label(text="Пароль:").grid(row=0, column=0)

# виджет поля ввода сырой пароль
Entry(textvariable=raw_pwd).grid(row=0, column=1)

# виджет кнопки
def button_func():
    hash_pwd.set(pwdGenerator(raw_pwd.get()))

Button(text="Пуск", command=button_func).grid(row=1, column=0)

# виджет поля вывода результата
Entry(textvariable=hash_pwd).grid(row=1, column=1)

# точка входа программы 
window.mainloop()


