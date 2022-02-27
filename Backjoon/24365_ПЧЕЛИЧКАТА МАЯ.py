# 24365. ПЧЕЛИЧКАТА МАЯ
A, B, C = map(int,input().split())

result = min(abs(A-C)*2+abs(A-B),abs(B-A)+abs(B-C),abs(C-A)*2+abs(C-B))
print(result)