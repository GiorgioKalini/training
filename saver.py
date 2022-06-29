#import os
#list_paths = []
#for adress, papka, file in os.walk('C:/Users/Home/Desktop'):
#    for i in file:
#        full_path = os.path.join(adress, i)
#        list_paths.append(full_path)

# 'r' открыть для чтения (по умолчанию)
# 't' открыть в текстовом режиме (по умолчанию)
# 'w' открыть для записи, содержимое файла удаляется, если файла нет создается новый
# 'a' открыть для дозаписи в конец файла, если файла нет создается новый
# 'b' открыть в бинарном режиме
# '+' открыть для чтения и записи 'r+', 'w+', 'a+'

r = open('C:/Users/Home/Desktop/textic.txt', 'w')
for x in list_paths:
    r.write(x + '\n')
r.close