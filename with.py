#r = open('C:/Users/Home/Desktop/text3.txt', 'a')
#try:
#    r.write('что-то записали' + '\n')
#    10/0                               # создали ошибку
#    r.write('и еще что-то')
#finally:
#    r.close()
#print('Все норм...')

with open('C:/Users/Home/Desktop/text3.txt', 'a') as r:  # используется при работе с файлами требовательными к закрытию
    r.write('что-то записали' + '\n')
    10/0
    r.write('и еще что-то')
print('Все норм...')