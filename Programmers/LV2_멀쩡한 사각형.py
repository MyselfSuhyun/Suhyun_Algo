# 수학문제 최대공약수를 쓰자
from math import gcd

def solution(w,h):
    # 넓이 * 높이 = 총사각형
    # w + h = 대각선이 지나가는 길이
    # gcd 최대공약수를 더해주면, 크기만큼 빠진다.(근데 이유는 잘 모르곘다...)
    answer = w*h - (w+h-gcd(w,h))
    return answer