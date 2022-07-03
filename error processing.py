import sys
url_list = ['C:/Users/Home/Desktop/text.txt', 'C:/Users/Home/Desktop/text2.txt']
list_defekt = []
list_info = []
try:
    for url in url_list:
        try:
            r = open(url)
            list_info.append(r.read())
            print('записано')
        except Exception:
            list_defekt.append(url)
            print('ошибка адреса')
            sys.exit()              # генерирует ошибку которую мы не можем обработать
            continue
finally:
    r = open('C:/Users/Home/Desktop/save.txt', 'a')
    for i in list_info:
        r.write(i)
    r.write(str(list_defekt))
    r.close()
    print('успешно сохранено')

