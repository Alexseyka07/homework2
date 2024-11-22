print('x y z')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            if not (z or x) or (y) and (not x) and (z and (not y or z)):
                print(x, y, z)

# Вывод
# x y z
# 0 0 0
# 0 1 0
# 0 1 1


# Ответ yxz
