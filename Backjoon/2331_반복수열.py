A, P = map(int,input().split())
arr = [A]
while True:
    n = arr[-1]
    rst = 0
    while n//10:
        rst += (n%10)**P
        n //= 10
    rst += n**P
    if rst in arr:
        break
    arr.append(rst)
# print(rst)
print(arr.index(rst))
