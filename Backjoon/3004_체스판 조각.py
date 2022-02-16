N = int(input())

# 1 = > 2 2*1 N+1 N
# 2 = > 4 2*2 N N
# 3 = > 6 3*2 N N-1
# 4 = > 9 3*3 N-1 N-1
# 5 = > 12 4*3 N-1 N-2
# 6 = > 16 4*4 N-2 N-2

result = 1
tmp = 1
for i in range(N):
    result += tmp
    if not i%2:
        tmp +=1
print(result)