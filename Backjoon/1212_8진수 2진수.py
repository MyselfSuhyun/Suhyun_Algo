# 1212. 8진수 2진수

S = int(input(),8)
print(bin(S)[2:])

# 시간 초과
# l = len(S)
# dec = 0
#
# for i in range(l):
#     dec += int(S[i])*(8**(l-1-i))
# print(bin(dec)[2:])

