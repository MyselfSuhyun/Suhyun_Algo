# 테스트 케이스의 수 T
T = int(input())

for tc in range(1,T+1):
    a, b = map(int,input().split())

    print(f'Case #{tc}: {a} + {b} = {a+b}')