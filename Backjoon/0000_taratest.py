a = [1, 2, 3, 4]
b = [11, 22, 33, 44, 55, 66, 77, 88]
c = [0] * len(b)
print(c)
for i in range(len(c)):
    c[i] = a[i%len(a)]

print(c)

