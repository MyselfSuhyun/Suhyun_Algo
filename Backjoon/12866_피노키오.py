n = int(input())

s = input()


result = []
for i in ['A','C','G','T']:
    result.append(s.count(i))

total = 1
for k in result:
    total *= k

print(total % 1000000007)