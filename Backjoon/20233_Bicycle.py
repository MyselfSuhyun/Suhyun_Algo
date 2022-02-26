a = int(input())
x = int(input())
b = int(input())
y = int(input())
t = int(input())

if t - 30>0:
    A = a + (t-30)*x*21
else:
    A = a
if t - 45>0:
    B = b + (t-45)*y*21
else:
    B = b
print(A,B)