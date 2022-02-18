arr = [list(map(int, input().split())) for _ in range(5)]


def cell(y, x):
    # 8가지 방향으로, 내 주변에 불안정 물질이 있는지 확인하기 위한 델타함수
    directy = [-1, -1, -1, 0, 0, 1, 1, 1]
    directx = [-1, 0, 1, -1, 1, -1, 0, 1]
    # 8방향이므로 8개의 반복문
    for i in range(8):
        # 현재 위치에서 이동한 위치를 저장해둘 변수
        dy = y + directy[i]
        dx = x + directx[i]
        # 현재 배열(arr) 의 영역은 4 * 5 배열이므로, 해당 영역안에 존재할 경우, 확인한다.
        # 해당 배열 크기 밖으로 하면 index 초과를 보았다고 오류가 발생한다.
        if 0 <= dx < 4 and 0 <= dy < 5:
            # 해당 영역에서 불안정한 상태(1) 이존재할경우 1을 반환한다.
            if arr[dy][dx]:
                return 1
    # 8가지 반복문은 정상 적으로 수행했을 경우 발동하는 영역, 안정상태이므로 0을 반환한다.
    else:
        return 0

# 불안정 갯수를 세기 위한 변수.
# 함수 cell 을 통해, 불안정할경우 return 1, 안정할경우 0을 반환한다.
cnt = 0
# 4*5 배열(array) 를 돌면서, arr[i][j] = 1 이 되는, 즉 안정상퇴를 확인해야는 지점을 만날경우,
# cell 함수를 실행하여 cnt 에 그 값을 더해준다.
for i in range(5):
    for j in range(4):
        if arr[i][j]:
            cnt += cell(i, j)
if cnt:
    print('불안정한 상태')
else:
    print('안정된 상태')