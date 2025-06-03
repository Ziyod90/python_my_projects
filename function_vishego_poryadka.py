# Функции высшего порядка
"""
В программировании (и в математике) функциями высшего порядка называются функции, которые выполняют одно (или оба) из этих действий:

Принимают одну (и более) функций в качестве аргументов.
Возвращают функцию в качестве результата.
Все остальные функции считаются функциями первого порядка. Вот простейший пример обработки нескольких функций первого порядка multiply(), power(), add(), subtract() функцией высшего порядка higher_order():
"""


def higher_order(function):
    return function(15)


def multiply(x):  # функция первого порядка
    return x * x


def power(x): # функция первого порядка
    return x ** x


def add(x): # функция первого порядка
    return x + x


def subtract(x): # функция первого порядка
    return x - (x * x)


print(higher_order(multiply))
print(higher_order(power))
print(higher_order(add))
print(higher_order(subtract))