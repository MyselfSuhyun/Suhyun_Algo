N = 3
before = int(input())
increase = 0
decrease = 0
constant = 0
for i in range(N):
    t = int(input())
    if before > t:
        decrease += 1
    elif before == t:
        constant += 1
    elif before < t:
        increase += 1
    before = t
if increase == 3:
    print('Fish Rising')
elif decrease == 3:
    print('Fish Diving')
elif constant == 3:
    print('Fish At Constant Depth')
else:
    print('No Fish')
