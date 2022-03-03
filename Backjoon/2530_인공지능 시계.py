A, B, C = map(int,input().split())
D = int(input())

tmpB = (C+D)//60
tmpC = (C+D)%60
tmA = (B+tmpB)//60
tmB = (B+tmpB)%60
tmpA = (A+tmA)%24

print(tmpA,tmB,tmpC)