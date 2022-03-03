N = int(input()) # 이번 달에 사용하고 싶은 양
K = int(input()) # 저번 달에 남은 양

tmp = min(K+60,N)
result = tmp*1500 + (N-tmp) *3000
print(result)