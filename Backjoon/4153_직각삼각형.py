while True:
    tri = list(map(int, input().split()))
    if not tri[0] and not tri[1] and not tri[2]:
        break
    tri.sort()

    if tri[0] ** 2 + tri[1] ** 2 == tri[2] ** 2:
        print('right')

    else:
        print('wrong')