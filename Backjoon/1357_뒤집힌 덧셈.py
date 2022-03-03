# 1357. 뒤집힌 덧셈
X, Y = input().split()
X = X[::-1]
Y = Y[::-1]
result = str(int(X)+int(Y))
print(int(result[::-1]))