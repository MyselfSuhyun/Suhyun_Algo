# 1065. 한수
# 한수란? X 라는 수에서 각 자리의 값이 등차수열을 이룬다.
# 즉, 123 과 같은 수를 한수라 볼 수 있다.

# N 값 이하의 한수의 개수를 출력한다.
N = int(input())

# 한수의 개수를 담아둘 변수를 지정한다.
answer = 0

# 두자리 수이하는 모두 한수이다.
K = 99
if N<=K:
    answer = N
# 세자리 수 부터 한수인지를 확인해준다.
else:
    answer = K
    for n in range(K+1,N+1):
        #각 자리수의 차를 확인하자.
        arr = []
        tmp = str(n)
        for i in range(len(tmp)-1):
            arr.append(int(tmp[i])-int(tmp[i+1]))
        t = arr[0]
        for a in arr:
            if t != a:
                break
        else:
            answer += 1
print(answer)
