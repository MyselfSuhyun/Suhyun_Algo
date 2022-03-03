# 뉴비 1학년 혹은 2학년
# 올드비 N 학년 이하, 뉴비가 아닌 학생
# TLE 뉴비도 올드비도 아닌 학생
N, M = map(int,input().split())

if M <=2:
    print('NEWBIE!')
elif M<=N:
    print('OLDBIE!')
else:
    print('TLE!')