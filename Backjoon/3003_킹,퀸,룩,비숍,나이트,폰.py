# 화이트 피스를 숫자로 받는다.
white_piece = list(map(int, input().split()))
# 옳게 된 피스를 받아온다.
correct_piece = [1, 1, 2, 2, 2, 8]
# 피스의 총 길이
n = len(white_piece)
# 출력할 결과값을 받아줄 result
result = []

for i in range(n):
    # 피스의 길이를 돌면서 옳게된 피스 - 입력받은 피스 를 result 에 append 한다.
    result.append(correct_piece[i]-white_piece[i])

# unpacking 을 통해 배열을 문자열로 출력한다.
print(*result)
