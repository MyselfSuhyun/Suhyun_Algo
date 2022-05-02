arr = [input() for _ in range(5)]
rst = []
for i in range(5):
    if arr[i].find('FBI')==-1:
        continue
    else:
        rst.append(i+1)
if rst:
    print(*rst)
else:
    print('HE GOT AWAY!')
