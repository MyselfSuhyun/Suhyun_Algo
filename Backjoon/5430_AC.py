# 5430. AC
T = int(input()) # 첫 줄에 테스트 케이스의 개수 T

for tc in range(1,T+1):
    P = input() # 수행할 함수 p
    P = P.replace('RR','')
    n = int(input()) # 배열의 개수 n
    tmp = input()
    arr = tmp[1:len(tmp)-1].split(',')

    r = 0 # reverse 나온 횟수(R)
    f,b = 0,0 # front, back

    for p in P:
        if p == 'R':
            r+=1
        elif p == 'D':
            if r%2:
                b += 1
            else:
                f += 1
    if f+b<=n: # 없앤 갯수가 배열길이 n 보다 작을 경우
        arr = arr[f:n-b]

        if r%2:
            tmp=','.join(arr[::-1])
            print(f'[{tmp}]')
        else:
            tmp = ','.join(arr)
            print(f'[{tmp}]')
    else:
        print('error')
