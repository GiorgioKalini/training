print('Lets go!')
number = 1
number1 = 3
number2 = 5
result = number + number1 + number2
print(result)
num1 = result
num2 = result + 1
print(num1, num2)
num1, num2 = num2, num1 + number2
print(num1, num2)
num2 -= number1
print(num2)
x, y, *z = [33, 42, 57, 64, 73]
print(x, y, z)
x = float(input('Введите число1 '))
y = float(input('Введите число2 '))
r = x + y
print('Результат ' + str(r))
