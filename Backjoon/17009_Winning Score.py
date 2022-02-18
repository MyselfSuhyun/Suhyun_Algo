arr = [int(input()) for _ in range(6)]
result = []
for i in range(0,len(arr),3):
    result.append(3*arr[i]+2*arr[i+1]+arr[i+2])

if result[0]>result[1]:
    print('A')
elif result[0] == result[1]:
    print('T')
elif result[0] < result[1]:
    print('B')