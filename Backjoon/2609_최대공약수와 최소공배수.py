a,b = map(int,input().split()) # a > b 라고 하자

A, B = a,b
while b > 0:
    a, b = b, a % b

print(a)
print(A * B // a) # = > 구하고자하는 값 A,B 를 곱해준 뒤, 최대 공약수를 나누어주자.