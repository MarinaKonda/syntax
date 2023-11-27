# *** Функция ***

# создание (определение) функции
def my_func():
    print("hello from mu_func")

# вызов функций
# my_func()

def func_2(arg_0, arg_1):
    res = arg_0 = arg_1
    # print(res) 
    return res

var = func_2(5, 2)
print(var)

# *** Классы ***

# опредедение класса
class MyClass:
    def __init__(self, name, age):
        # атрибуты (свойства)
        self.name = name
        self.age = age

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# создание экземпляров (объектов) класса MyClass
obj_0 = MyClass("Marina", 25)
obj_1 = MyClass("Lena", 27)
obj_2 = MyClass("Denis", 18)

# вызов методов у экземпляров
# obj_0.info()
# obj_1.info()
# obj_2.info()