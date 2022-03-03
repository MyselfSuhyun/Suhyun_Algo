N = int(input())
M = int(input())

if N >= M:
    print('Congratulations, you are within the speed limit!')
else:
    tmp = M - N
    if tmp<=20:
        print('You are speeding and your fine is $100.')
    elif tmp<=30:
        print('You are speeding and your fine is $270.')
    else:
        print('You are speeding and your fine is $500.')