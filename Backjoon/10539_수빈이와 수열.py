N = int(input())
arr = list(map(int,input().split()))[:N]
b_arr = [0]*N
b_arr[0] = arr[0]
for i in range(1,N):
    b_arr[i] = (i+1)*arr[i]-sum(b_arr[0:i])

print(*b_arr)

# b[1] = (a[0]+a[1])/2
# 2*b[1]-a[0] = a[1]
# b[2] = (a[0]+a[1]+a[2])/3
# 3*b[2] - (a[0]+a[1]) = a[2]