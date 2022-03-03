# 24083. Hour Hand

A = int(input())
B = int(input())
if not (A+B)%12:
    print(12)
else:
    print((A+B)%12)