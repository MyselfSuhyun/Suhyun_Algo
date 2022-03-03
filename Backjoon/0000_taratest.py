T = int(input())

for order in range(1, T + 1):
    # 문제 입력 처리
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 3x3 델타 이동 (4방향 원소 이동은 인덱스가 짝수 일때를 활용)
    dr_3 = [-1, -1, 0, +1, +1, +1, 0, -1]  # 상 우상 우 우하 하 좌하 좌 좌상
    dc_3 = [0, +1, +1, +1, 0, -1, -1, -1]  # 상 우상 우 우하 하 좌하 좌 좌상

    result = 0  # 최댓값 저장할 결과 변수

    for r in range(N):
        for c in range(N):
            temp_sum_3 = arr[r][c]  # 3x3 배열의 합을 구할 변수
            sum_count_3 = 1  # 3x3 배열의 합의 개수를 구할 변수
            temp_sum_4 = arr[r][c]  # 4방향원소 합을 구할 변수
            for i in range(8):  # 8방향을 돈다.
                new_r = r + dr_3[i]  # 새로운 위치 저장
                new_c = c + dc_3[i]  # 새로운 위치 저장

                # 만약 새로운 위치가 인덱스를 벗어난다면 continue
                if new_r < 0 or new_r >= N or new_c < 0 or new_c >= N:
                    continue
                # 3x3 배열의 합을 저장해주고 해당 저장 개수를 +1 해준다.
                temp_sum_3 += arr[new_r][new_c]
                sum_count_3 += 1

                # 만약 현재 새로 이동한 위치가 4방향이라면 그합을 계속 더해준다.
                if i % 2 == 0:
                    temp_sum_4 += arr[new_r][new_c]

            # 만약 3x3을 더한 횟수가 총 9번이라면 인덱스를 벗어나지 않았다는 의미이므로
            if sum_count_3 == 9:
                if result < temp_sum_3:  # 해당 값이 저장된 결과값보다 크다면
                    result = temp_sum_3  # 그값을 최댓값으로 설정
            # 만약 결과값보다 4방향 합이 더 크다면
            if result < temp_sum_4:
                result = temp_sum_4  # 그 값을 최댓값으로 설정

    print(f'#{order} {result}')