# 임의의 자연수 N
N = int(input())

# 손가락 배열 8 을 기준으로 순회하게 된다.
# 1 : 엄지손가락 2: 검지손가락 3: 중지손가락 4: 약지손가락 5: 새끼손가락
arr = [2, 1, 2, 3, 4, 5, 4, 3]

# N에서 남은 나머지를 기준으로, index 접근하면 손가락을 구할 수 있다.
print(arr[N % 8])
