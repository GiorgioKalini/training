m = 'sttota text'
count = 0
for i in m:
    if i == 't':
        print('В строке есть буква:t')
        count += 1
    if i == 'a':
        break
    else:
        print('Букв t стоящих перед буквой a', count)
print('Программа работает дальше')