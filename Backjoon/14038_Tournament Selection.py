arr = [input() for _ in range(6)]
result = arr.count('W')
if result >=5:
    print(1)
elif result>=3:
    print(2)
elif result >=1:
    print(3)
else:
    print(-1)