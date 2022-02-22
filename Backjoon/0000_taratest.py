# 엣지케이스 발견해서 얘기나눠보기
N = int(input())

lst = list(map(int, input().split()))
num = len(lst)
ascV = descV = 1
asc_lst = []
desc_lst = []

if num != 1:
    for i in range(N-1):
        if lst[i] <= lst[i+1]:
            ascV += 1
        else:
            asc_lst += [ascV]
            ascV =1
    asc_lst += [ascV]
    for i in range(N-1):
        if lst[i] >= lst[i+1]:
            descV += 1
        else:
            desc_lst += [descV]
            descV = 1
    desc_lst += [descV]
    # print(asc_lst,desc_lst)
    sol1 = max(asc_lst)
    sol2 = max(desc_lst)

    # for i in range(num-1):
    #     if sol1 < asc_lst[i]:
    #          sol1 = asc_lst[i]
    #     if sol2 < desc_lst[i]:
    #          sol2 = desc_lst[i]

    res = sol1 if sol1 > sol2 else sol2
else:
    res = 1
print(res)