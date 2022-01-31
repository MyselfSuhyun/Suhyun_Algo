N = 5

arr = [int(input()) for _ in range(N)]

burger = min(arr[:3])

drink = min(arr[3:])

print(burger+drink-50)

