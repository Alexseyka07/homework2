print('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(x and (not y or z) or w):
                    print(x, y, z, w)

# Вывод
# x y z w
# 0 0 0 0
# 0 0 1 0
# 0 1 0 0
# 0 1 1 0
# 1 1 0 0



# Ответ 4
