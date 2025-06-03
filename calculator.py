def bmi(h, w):
    bmi = w / (h / 100) ** 2
    if bmi <= 18.5:
        return 'У вас дефицит веса'
    elif bmi <=24.9:
        return 'Вес в норме'
    elif bmi <= 29.9:
        return 'Есть лишный вес'
    else:
        return 'Срочно на диету!'

h = float(input('Введите рост в см: '))
w = float(input('Введите вес в кг: '))
print(bmi(h, w))