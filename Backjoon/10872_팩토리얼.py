N = int(input())
# for i in range(1,N+1):
#     answer *= i
# print(answer)

def factorial(n):
    answer = 1
    if n > 0:
        answer = n*factorial(n-1)
    return answer

print(factorial(N))
