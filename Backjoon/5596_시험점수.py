# 5596. 시험점수
minguk = sum(list(map(int,input().split())))
mansae = sum(list(map(int,input().split())))

if minguk>=mansae:
    print(minguk)
else:
    print(mansae)