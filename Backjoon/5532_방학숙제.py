L = int(input()) # 방학 일
A = int(input()) # 국어
B = int(input()) # 수학
C = int(input()) # 국어 풀 수 있는 양
D = int(input()) # 수학 하루 풀 수 있는 양

if A%C:
    ta = A//C+1
else:
    ta = A//C
if B%D:
    tb = B//D+1
else:
    tb = B//D
print(L-max(ta,tb))