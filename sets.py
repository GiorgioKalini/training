import time

def f(*args):
    list_new = []
    for i in args:
        for y in i:
            if y not in list_new:
                list_new.append(y)
    return list_new

z = list(range(10000))
x = list(range(5000, 15000))
y = list(range(10000, 20000))

start = time.time()
f(z, x, y)
stop = time.time() - start
print(stop)

start2 = time.time()
r = set(z)                         # создаем множества из списков
t = r.union(set(x), set(y))
stop2 = time.time() - start2
print(stop2)                       # операции над множествами быстрее, используются когда необходимо сравнить списки, откинуть одинаковые значения и т.д.