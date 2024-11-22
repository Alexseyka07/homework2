print('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if (x and (y or not z) and w) == (not x or not y and z):
                    print(x, y, z, w)
                
# Вывод            
# x y z w
# 1 0 0 0
# 1 1 0 0
# 1 1 1 0


# Ответ yxzw