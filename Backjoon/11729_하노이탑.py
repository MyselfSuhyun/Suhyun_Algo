def hanoi(n, s, e):
    if n == 1:
        print(s, e)
        return

    hanoi(n - 1, s, 6 - s - e)  # 1단계
    print(s, e)  # 2단계
    hanoi(n - 1, 6 - s - e, e)  # 3단계


n = int(input())
print(2 ** n - 1)
hanoi(n, 1, 3)