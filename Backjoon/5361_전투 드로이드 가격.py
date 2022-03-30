arr = [350.34,230.90,190.55,125.30,180.90]

T = int(input())
for tc in range(1,T+1):
    price = list(map(int,input().split()))
    rst = 0
    for i in range(5):
        rst += price[i]*arr[i]
    print(f'${round(rst,2):.2f}')