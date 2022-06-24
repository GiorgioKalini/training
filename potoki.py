x = 5
y = [1, 6, 5]
if x > 0:
    print(5/x)
elif x < 0:
    x = -x
    print(5/x)
else:
    x += 1
    print(5/x)
if y != 0 and (type(y) == type(5) or type(y) == type(5.5)):
    print('y допустимое число')
elif y == 0:
    y += 1
    print('y равен 0')
else:
    y = 1
    print('y не допустимое число')
print(100/y)
