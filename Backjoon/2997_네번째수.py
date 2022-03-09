arr = list(map(int,input().split()))
arr.sort()
result = []
for i in range(len(arr)-1):
    result.append(arr[i+1]-arr[i])
if result[0]==result[1]:
    print(arr[-1]+result[0])
elif result[0]>result[1]:
    print(arr[0]+result[1])
else:
    print(arr[1]+result[0])