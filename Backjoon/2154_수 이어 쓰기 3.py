N = input()
s = ''
for i in range(1,100001):
    s += str(i)
print(s.index(N)+1)