N = int(input())
S = input()
ar = ['a','e','i','o','u']
rst = 0
for s in S:
    if s in ar:
        rst += 1

print(rst)