# 10798. 세로 읽기

# 영어 대문자 A 부터 까지 소문자 a 부터 z 까지, 숫자 0 부터 9 까지
# 최대 15개의 글자들로 이루어짐
# 다섯 개의 단어를 세로로 읽으려 한다.

arr = []
for i in range(5):
    tmp = input()
    t_arr = ['']*15
    for t in range(len(tmp)):
        t_arr[t] = tmp[t]
    arr.append(t_arr)
for i in range(15):
    for j in range(5):
        if arr[j][i]:
            print(arr[j][i],end='')
