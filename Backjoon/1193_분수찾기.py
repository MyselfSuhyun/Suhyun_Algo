# 1193. 분수 찾기

# 1 1/1
# 2,3 1/2 2/1
# 4,5,6 1/3,2/2,3/1

X = int(input())
if X == 1:
    print('1/1')
else:
    tmp = 0
    cnt = 1
    arr = []
    while X > tmp:
        tmp += cnt
        cnt += 1
        arr.append(tmp)
    if cnt%2:
        print(f'{cnt-(arr[-1]-X+1)}/{(arr[-1]-X+1)}')
    else:
        print(f'{(arr[-1]-X+1)}/{cnt-(arr[-1]-X+1)}')