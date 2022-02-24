from math import pi

A1, P1 = map(int,input().split()) # 피자 조각
A2, P2 = map(int,input().split()) # 원형 피자
if P1/A1 < P2/(A2**2*pi):
    print("Slice of pizza")
else:
    print("Whole pizza")