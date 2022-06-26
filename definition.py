def count_list(par1, par2 = False, count = 0):    # задаем параметры функции
    if par2 == True:
        typ = type(par1[0])
        for i in par1:
            count += 1
        return count, typ
    else:
        for i in par1:
            count += 1
        return count

x = [2, 5, 7, 4, 9, 3]

y, z = count_list(x, True)
print(y)
print(z)

def name(h, x, *args, key):    # *args - аргумент который записывает все неименованные аргументы функции
    print(h)                   # стоящие после h,x в кортеж, если *args первый, то все начиная с первой...
    print(x)                   # чтобы обратиться к стоящим после нее, например key  - надо указать его имя
    print(*args)
    print(key)

name(1,4,4,56,84, key = 'gh')