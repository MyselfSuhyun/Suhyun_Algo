# 휴대폰 키보드 위치를 하나의 이차원 배열로 보고, 그 좌표값을 입력해주자.
y = [3,0,0,0,1,1,1,2,2,2]
x = [1,0,1,2,0,1,2,0,1,2]


# effort 를 구해주는 함수
def get_dist(a,b):
    return abs(x[a]-x[b]) + abs(y[a]-y[b])

# 시간과 분을 입력받자 H:M
H, M = map(int,input().split(':'))

# 시간은 99:99를 넘어갈 수 없으므로, 이를 반복문으로 넣어주자
K = 100
# 최소 노력값
efforts = 0xffffff
# 결과 시간과 분
ansH = ansM = 0

for h in range(H,K,24):
    for m in range(M,K,60):
        # 노력값을 구하자.
        tmp = get_dist(h//10,h%10) + get_dist(h%10,m//10) + get_dist(m//10,m%10)

        # 구해진 노력값보다 작으면, 그 값을 넣어주고, 답을 출력해주자.
        if tmp < efforts:
            efforts = tmp
            ansH = h
            ansM = m

# 10 보다 작으면 앞에 0을 붙여서 시를 출력한다.
if ansH<10:
    print('0'+str(ansH),end=':')
else:
    print(ansH,end=':')
# 10보다 작으면 앞에 0을 붙여서 분을 출력한다.
if ansM<10:
    print('0'+str(ansM))
else:
    print(ansM)
