# 24365. ПЧЕЛИЧКАТА МАЯ
arr = list(map(int,input().split()))

tmp = [0]*3
avg = sum(arr)//3

for i in range(len(arr)):
    tmp[i] = arr[i]-avg
result = 0
if tmp[0] < 0:
    print(1,tmp)
    if tmp[1] > 0:
        result += tmp[1]-avg
        tmp[0] += result
    elif tmp[2]>0:
        result += 2*(tmp[2]-avg)
        tmp[0] += result//2
print(tmp)
print(result)