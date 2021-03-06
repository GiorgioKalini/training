d1 = {'a': 3, 'b': 5}                       # методы                        
d2 = dict(a=4, b=6, c=8)                    #         создания             
d3 = dict.fromkeys(['a','b','c'])           #                   словарей   
d4 = dict.fromkeys(['a','b','c'], 3)
d5 = dict([[1,2], [3,4], [5,6]])
print(d1['a'])
d1['a'] = 6
print(d1['a'])
del d1['a']
print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
d6 = d5.copy            # копируем словарь d5 в переменную d6
print(d1.items())       # возвращает список в виде кортэжей чтобы работать со словарем при помощи цикла for
print(d2.keys())        # возвращает ключи в словаре
print(d5.values())      # возвращает значения
d4.update(d2)           # добавляет значения из списка d2 в d4, если ключи повторяются, то заменяет значения у соответствующих ключей
print(d4)
y = d1.get('c', 9)      # если в списке будет значение 'c' то вернет его, если нет, то подставит туда 9, и ошибки не будет
print(y)
t = d2.pop('a')         # удаляет ключ и значение и возвращает значение ключа
print(t, d2)



price = {'мясо': 350, 'хлеб': 43, 'картофель': 76, 'вода': 54}

def buy():
    pay = 0
    while True:
        enter = input('Что покупаем?\n')
        if enter == '':
            break
        pay += price[enter]
    return pay

print('К оплате', buy(), 'руб')
