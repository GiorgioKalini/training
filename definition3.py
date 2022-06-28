import math                         # запускаем модуль math
PI = math.pi                        # берем из модуля math значение числа pi

def radius():
    n = float(input('Диаметр цилиндра в см '))
    n = n/2
    return n

def height():
    m = float(input('Высота цилиндра в см '))
    return m

def volume():
    r = radius()
    h = height()
    s = PI*r**2
    v = s*h
    return v

print('Объем цилиндра', volume(), 'см3')

def massa(g):
    c = float(input('Удельный вес г/см3 '))
    return g*c/1000

print('Вес цилиндра', massa(volume()), 'кг')