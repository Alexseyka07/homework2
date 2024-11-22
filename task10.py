def f1(x, y, z, w):
    return int((x <= y) or (not w == z))

def f2(x, y, z, w):
    return int((x <= y) == (w and not z))


print('x y z w f1 f2')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if f1(x, y, z, w) == f2(x, y, z, w):
                    print(x, y, z, w, f1(x, y, z, w), f2(x, y, z, w))

# Вывод
# x y z w f1 f2
# 0 0 0 1 1 1
# 0 1 0 1 1 1
# 1 0 1 0 1 1
# 1 1 0 1 1 1




# Ответ wyxz
