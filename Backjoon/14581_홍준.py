S = input()
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            print(f':{S}:',end='')
        else:
            print(f':fan:',end='')
    print()