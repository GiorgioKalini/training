x = (1, 6, 4, 9, 7, 1, 8, 7)   #  кортэж - не изменяемый тип данных
print(x.count(7))           #  возвращает кол-во одинаковых указанных элементов в кортэже
print(x.index(9))           #  возвращает индекс нужного элемента (первого из них, если есть одинаковые)
x += (5, 6, 7)              #  можно добавлять к кортэжу еще один кортэж
print(x)