print('x y z')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            if (not x and y and z) or (not x and y and not z) or (not x and not y and not z):
                print(x, y, z)
                
# Вывод            
# x y z
# 0 0 0
# 0 1 0
# 0 1 1

# Ответ yxz