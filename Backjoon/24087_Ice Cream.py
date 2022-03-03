# 24087. Ice Cream

S = int(input())
A = int(input())
B = int(input())

if (S-A)%B:
    tmp = (S-A)//B +1
else:
    tmp = (S-A)//B
result = 250+tmp*100
if result>250:
    print(result)
else:
    print(250)