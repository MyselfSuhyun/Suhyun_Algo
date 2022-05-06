T = int(input())
for tc in range(1,T+1):
    a,b = map(int,input().split())
    prime = []
    for i in range(1,a+1):
        if i*i > a:
            break
        if a%i == 0:
            prime.append(i)
            if i*i !=a:
                prime.append(a//i)
    if sum(prime)-1-a == b:
        print('yes')
    else:
        print('no')