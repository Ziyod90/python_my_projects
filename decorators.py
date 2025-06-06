# Декораторы в Python
"""
Синтаксис Python позволяет использовать декораторы для получения результата «прохождения» функции первого порядка через функцию высшего порядка. Декоратор – это функция высшего порядка, которая принимает функцию первого порядка и добавляет в результат что-нибудь от себя, не вмешиваясь в логику полученной функции:
"""


def print_result(f):
    def result(x):
        r = f(x)
        print(f'Результат вычисления: {r}')
        return r

    return result


@print_result
def triple(x):
    return x * 3


@print_result
def divide(x):
    return x / 5


triple(5)
divide(5)
