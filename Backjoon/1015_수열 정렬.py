N = int(input())
arr = list(map(int,input().split()))
cnt = [0]*1001
for a in arr:
    cnt[a] +=1
for i in range(len(cnt)-1):
    cnt[i+1] += cnt[i]

for a in arr:
    print(cnt[a-1],end=' ')
    cnt[a-1]+=1
print()