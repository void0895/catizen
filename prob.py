p1 = 10
p2 = 9
p3 = 8
a = 12
for i in range(1, 4):
    rtx = eval('p' + str(i))
    print(f"probability for phone :{i} is", round((rtx/a) * 100))
