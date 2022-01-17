# 달을 우선 넣어주자.
month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
# 2009년 1월 1일은 목요일(Thursday) 이다.
# 즉, 나머지가 1일떄는 목요일, 0일떄는 수요일, 6일때는 화요일이 된다.
weekday = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday','Monday', 'Tuesday']

# 첫재쭐에 D와 M이 주어진다.
D, M = map(int,input().split())

# 출력은 요일을 출력해야하므로, 총 날짜를 계산한 후, 그 값의 나머지를 통해 weekday 를 구하자.
# 총 날짜 = M * month[M] + D
date = sum(month[0:M]) + D
# 나머지에 따라 weekday 가 변하게 된다.
print(weekday[date % 7])
