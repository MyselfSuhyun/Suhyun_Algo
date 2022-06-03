result = int(input())
while True:
    N = input()
    if N == '+':
        result += int(input())
    elif N== '-':
        result -= int(input())
    elif N== '*':
        result *= int(input())
    elif N=='/':
        result //= int(input())
    elif N=='=':
        print(result)
        break
