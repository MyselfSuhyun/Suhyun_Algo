# 목표: 1~n 까지의 자연수 중 소수를 모두 출력한다.
P, n = map(int,input().split())
isPrime = [True for i in range(n + 1)]

# 2. 가지치기 한 방법
isPrime[0] = False  # 0 역시도 아니니까!
isPrime[1] = False  # 1은 소수가 아니니까!!
for i in range(2, n + 1):
    if not isPrime[i]:
        continue

    for j in range(i * i, n + 1, i):  # i 보다 작은 값은 이미 미리 봤으니까!
        isPrime[j] = False
prime = [i for i in range(2, n) if isPrime[i] == True]
# print(prime)
g, b = 1, 0
for i in prime:
    if not P%i:
        g,  b = 0, i
        break
print("GOOD" if g else f"BAD {b}")
