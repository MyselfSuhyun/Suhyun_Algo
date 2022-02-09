N, M = map(int,input().split())
K = int(input())
hour = [i for i in range(0,24)]

tmp = (M+K)//60
minute = (M+K)%60
h= hour[(N+tmp)%24]
print(h,minute)
