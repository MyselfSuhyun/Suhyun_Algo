A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

a = A*P
if C>P:
    b = B
else:
    b = B+ D*(P-C)
print(min(a,b))