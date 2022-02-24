N = int(input())

# N 이 홀수일 경우, 연속된 숫자의 합이 짝수거나 홀수임
if N%2:
    print(0)
elif N//2%2:
    print(1)
else:
    print(2)