A, B = map(int, input().split())
b, r = divmod(A, B)
if A != 0 and r < 0:
    b, r = b+1, r-B
print(b)
print(r)