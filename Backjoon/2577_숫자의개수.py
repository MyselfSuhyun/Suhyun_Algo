# 2577 숫자의 개수
A = int(input())
B = int(input())
C = int(input())

result = A * B * C

# dict_num = {
#     '0':0, '1':0, '2':0, '3':0,
#     '4':0, '5':0, '6':0, '7':0,
#     '8':0, '9':0,
# }
#
# for s in str(result):
#     dict_num[s] += 1

# for v in dict_num.values():
#     print(v)

result = list(str(result))
for i in range(10):
    print(result.count(str(i)))

