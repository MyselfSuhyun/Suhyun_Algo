# 16017. Telemarketer or not?
arr = [int(input()) for _ in range(4)]

if 8<=arr[0]<=9 and 8<=arr[3]<=9 and arr[1]==arr[2]:
    print('ignore')
else:
    print('answer')