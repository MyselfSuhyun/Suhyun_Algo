S = input()
name = [0,0,0,0]
for s in S:
    if s=='L':
        name[0]+=1
    elif s=='O':
        name[1]+=1
    elif s=='V':
        name[2]+=1
    elif s=='E':
        name[3]+=1
N = int(input())
result = ''
cnt = -1
for n in range(N):
    tmp = input()
    arr = [name[0],name[1],name[2],name[3]]
    for t in tmp:
        if t == 'L':
            arr[0] += 1
        elif t == 'O':
            arr[1] += 1
        elif t == 'V':
            arr[2] += 1
        elif t == 'E':
            arr[3] += 1
    rst = (arr[0]+arr[1])*(arr[0]+arr[2])*(arr[0]+arr[3])*(arr[1]+arr[2])*(arr[1]+arr[3])*(arr[2]+arr[3])
    print(rst)
