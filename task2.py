print('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(((not x or y) and (not y or w)) or (z == (x or y))):
                    print(x, y, z, w)
                
# Вывод            
# x y z w
# 0 1 0 0
# 1 0 0 0
# 1 0 0 1
# 1 1 0 0


# Ответ ywzx