# def some():
#     list_text = []
#     with open('text.txt', encoding='utf_8') as r:
#         for x in r:
#             list_text.append(x)
#     return list_text

def some():
    with open('text.txt', encoding='utf_8') as r:
        for x in r:
            yield x                # yield - создает из функции объект-генератор который будет выдавать
                                   # по одному значению за раз... для экономии мощностей

for i in some():
    print(i.split())
    print(i)