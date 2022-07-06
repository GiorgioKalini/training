h = [9, 8, 6, 7, 4, 4, 5, 8, 3, 7, 1, 2, 3]

new_h = []               #   создаем
for x in h:              #            новый 
    new_h.append(x*2)    #       список
print(new_h)             #               из h с помощью цикла

# более простые и быстрые в обработке способы:

n = [x*2 for x in h]     #  создаем список
z = {x*2 for x in h}     #  создаем множество
f = {x: x*2 for x in h}  #  создаем словарь
g = [x for x in h if x % 2 == 0]   # выбираем только четные числа из списка
print(n)
print(z)
print(f)
print(g)

r = (x*2 for x in h)     # это выражение генератор, запускается циклом и выдает по одному значению за раз
for i in r:
    print(i)

