def f1(x, y, z, w):
    return int((w <= z) == (y <= x))

def f2(x, y, z, w):
    return int((w <= z) == (not x <= y))


print('x y z w f1 f2')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                    print(x, y, z, w, f1(x, y, z, w), f2(x, y, z, w))

# Вывод
# x y z w f1 f2
# 0 0 0 0 1  0
# 0 0 0 1 0  1
# 0 0 1 0 1  0
# 0 0 1 1 1  0
# 0 1 0 0 0  0
# 0 1 0 1 1  1
# 0 1 1 0 0  0
# 0 1 1 1 0  0
# 1 0 0 0 1  1
# 1 0 0 1 0  0
# 1 0 1 0 1  1
# 1 0 1 1 1  1
# 1 1 0 0 1  0
# 1 1 0 1 0  1
# 1 1 1 0 1  0
# 1 1 1 1 1  0




# Ответ wzyx
