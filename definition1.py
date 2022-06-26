def exclusive_item(*args, key=False):
    new_list = []
    for i in args:
        for y in i:
            if y not in new_list:
                new_list.append(y)
    if key == True:
        new_list.sort()
    return new_list

z = [2,3,6,8,8,9]
x = [3,7,6,5,1]
c = [1,2,3,4,5,6]
t = exclusive_item(z, x, c, key=True)
print(t)