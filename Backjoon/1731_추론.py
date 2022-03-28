N = int(input())
arr = [int(input()) for _ in range(N)]
a = arr[-3]
b = arr[-2]
c = arr[-1]
if 2* b  == a+c:
    print(c + (c-b))
else:
    print(c**2//b)
