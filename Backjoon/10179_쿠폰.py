# 10179. 쿠폰
T = int(input()) # 테스트 케이스의 수 T
for tc in range(1,T+1):
    N = float(input())
    print(f'${round(N*0.8,2):.2f}')