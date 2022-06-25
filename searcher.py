import os                                                  # os - модуль по работе с операционной системой
import time
('C:\\Users\\Home\\Desktop\\пайтон', ['.git', 'test'], ['.gitignore', 'errors.txt', 'index.html', 'readme.md', 'script.js'])

spisok = []
for adress, dirs, files in os.walk('C:\\Users\Home\Desktop\пайтон'):           # walk - генерирует пути к файлам
    for file in files:
        full = os.path.join(adress, file)                                     # os.path.join - проставляет \\ в адресах к файлам
        if '.txt' in full:
            spisok.append(full)
print(spisok)
