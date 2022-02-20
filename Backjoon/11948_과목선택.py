a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

arr = [a,b,c,d]
arr.sort(reverse=True)
print(sum(arr[:3])+max(e,f))