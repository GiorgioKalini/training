s = 'sTroka texta'

s1 = s.upper()       # все в верхний регистр
print(s1)
s2 = s.lower()       # все в нижний регистр
print(s2)
s3 = s.capitalize()  # первая заглавная остальные прописные
print(s3)

path = 'C:/Users/Home/Desktop/text.txt'
path1 = path.replace('/', '\\')             # заменили (слеши для лин на слеши для винд)
print(path1)

r = path1.split('\\')        # разбить по разделителю
print(r)
print(r[-1])

q = open(path1)       # открываем документ
r1 = q.read()
list_znk = ['(', ')', '"', '\n']
for i in list_znk:
    r1 = r1.replace(i, '')
print(r1)

r2 = r1.split()
print(r2)

new_text = ' '.join(r2)
print(r2)