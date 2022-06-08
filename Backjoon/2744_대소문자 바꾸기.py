# print(ord('a'),ord('z'))
# print(ord('A'),ord('Z'))

S = input()
rst = ''
for s in S:
    if 97<=ord(s)<=122:
        rst += chr(ord(s)-32)
    else:
        rst += chr(ord(s)+32)

print(rst)