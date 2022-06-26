x = 5
def new():        
    x = 100
    def new2():
        nonlocal x  # изменяем локальную переменную основной функции
        x = 200
        print(x)
    new2()
    print(x)
new()
print(x)
def new3():
    global x        # изменяем глобальную переменную х
    x = 300
    print(x)

new3()
print(x)
