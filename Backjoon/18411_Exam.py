scores = list(map(int,input().split()))
scores.sort(reverse=True)
print(sum(scores[:2]))