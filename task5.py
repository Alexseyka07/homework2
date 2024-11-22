print('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(((not x or w) or y and not z) and ((not y or not z) or x and not w)):
                    print(x, y, z, w)

# Вывод
# x y z w
# 0 1 1 0
# 0 1 1 1
# 1 0 0 0
# 1 0 1 0
# 1 1 1 0
# 1 1 1 1

# Убираем ненужные строки

# x y z w
# 0 1 1 0
# 1 0 0 0
# 1 0 1 0

# Ответ zwyx
