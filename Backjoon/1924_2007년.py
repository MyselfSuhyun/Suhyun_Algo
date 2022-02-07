# 2007년 1월 1일은 월요일
dic = {0:'SUN',1:'MON',2:'TUE',3:'WED',4:'THU',5:'FRI',6:'SAT'}
dal = [0,31,28,31,30,31,30,31,31,30,31,30,31]
m,d = map(int,input().split())
ans = (sum(dal[:m])+d)%7

print(dic[ans])