# 팬케이스 16 x 를 만들기 위해 필요한 반죽 재료의 양
# 우유 8컵, 계란 노른자 8개, 설탕 4스푼, 소금 1스푼, 밀가루 9컵
correct_pan = [8,8,4,1,9]
# 토핑 재료
# 바나나 1개, 딸기, 30그램, 초콜릿 25그램, 호두, 10개
correct_toping = [1,30,25,10]

# 테스트 케이스의 수 T
T = int(input())
for _ in range(T):
    # 테스트 케이스의 구분
    state = input()
    # 팬케이크 반죽 재료 입력 값
    pan = list(map(int,input().split()))
    # 팬케이크 토핑 재료 입력 값
    toping = list(map(int,input().split()))

    # 만든 반죽 갯수
    create_pan = 0xffffff
    for i in range(len(pan)):
        # 해당 재료로 만들 수 있는 반죽 값
        tmp = pan[i]/correct_pan[i]
        # 그 중 최소의 값을 correct_pan 에 대입한다.
        create_pan= min(tmp,create_pan)
    # 16 x 를 만들 수 있으므로 16을 곱해준다.
    create_pan *= 16
    create_toping = 0
    for j in range(len(toping)):
        # 해당 토핑으로 만들 수 있는 팬케이크를 더해주자.
        tmp = toping[j]//correct_toping[j]
        create_toping += tmp

    # 두개의 값중 작은 쪽을 출력하자. 그게 만들어진 팬케이크의 갯수다
    print(int(min(create_pan,create_toping)))
