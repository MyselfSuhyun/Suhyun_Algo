A, B = input().split()

answer = 0xffffff
for i in range(len(B)-len(A)+1):
    tmp = 0
    for j in range(len(A)):
        if A[j]!=B[i+j]:
            tmp +=1
    if tmp < answer:
        answer = tmp

print(answer)