result = 0
answer = -1
for _ in range(4):
    A,B= map(int,input().split())
    result += B-A
    if answer < result:
        answer = result

print(answer)