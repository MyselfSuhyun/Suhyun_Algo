# F(x) 는 입력으로
#주어진 수 x 의 첫자리수와 x 의 자리수를 곱한 결과를 반환하는 함수

N = input()

while True:
    a = N[0]
    L = len(N)
    tmp = a*L
    if N == tmp:
        print('FA')
        break
    N = tmp