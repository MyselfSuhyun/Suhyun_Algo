N = input()
num = {
    '0':0,'1':0,'2':0,'3':0,
    '4':0,'5':0,'7':0,
    '8':0,'9':0,
}

for n in N:
    if n != '6':
        num[n] +=1
    else:
        num['9'] +=1

if num['9']%2:
    num['9'] = num['9']//2 + 1
else:
    num['9'] //= 2
print(max(num.values()))
