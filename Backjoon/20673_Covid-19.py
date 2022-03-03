# 평균 사례 50명 , 신규 사례 10명 이하 -> 흰색
# 평균 사례 50명 , 신규 사례 30명 이상 -> 빨간색

p = int(input())
q = int(input())
if q >30:
    print('Red')
elif p <=50 and q <=10:
    print('White')
else:
    print('Yellow')