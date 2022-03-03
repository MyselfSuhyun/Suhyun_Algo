#
arr = [4,2,3,3,3,3,3,3,3,3]

while True:
    N = input()
    if N == '0':
        break
    result = len(N) + 1
    for i in N:
        result += arr[int(i)]

    print(result)
