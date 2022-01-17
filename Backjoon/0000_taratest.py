arr = [1,2,3]

for i in range(30):
    print(arr[i%len(arr)],end=' ')