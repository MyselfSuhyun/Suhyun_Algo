alpha = {
    '000000' : 'A',
    '001111' :'B',
    '010011':'C',
    '011100':'D',
    '100110':'E',
    '101001':'F',
    '110101':'G',
    '111010':'H'
}

N = int(input())
S = input()
rst = ''
for n in range(N):
    if alpha.get(S[n:6*n+6]) != None:
        rst += alpha[S[n:6*n+6]]
        print(rst)
    else:
        print(n+1)
        break
else:
    print(rst)
