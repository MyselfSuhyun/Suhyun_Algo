dic = dict()
for _ in range(10):
    N = int(input())
    if dic.get(N) is None:
        dic[N]=1
    else:
        dic[N]+=1
rst1 = 0
rst2 = 0
val = max(dic.values())
for k,v in dic.items():
    rst1 += k*v
    if v == val:
        rst2 = k
print(rst1//10)
print(rst2)