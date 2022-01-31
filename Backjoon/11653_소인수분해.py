N = int(input())

k = 2
while N != 1:
    while not N%k:
        print(k)
        N /= k
    k +=1