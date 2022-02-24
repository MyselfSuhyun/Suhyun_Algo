N, H, V = map(int,input().split())

result = max(H,N-H) * max(V,N-V)
print(result*4)