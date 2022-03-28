def permutation(arr, n):
    # arr = sorted(arr)
    visited = [0 for _ in range(len(arr))]

    def generate(chosen, visited):
        if len(chosen) == n:
            for i in chosen:
                print(i, end=" ")
            print()
            return

        for i in range(len(arr)):
            if not visited[i]:
                chosen.append(arr[i])
                visited[i] = 1
                generate(chosen, visited)
                visited[i] = 0
                chosen.pop()
                # print(i,chosen)


    generate([], visited)


N = int(input())
lst = [i for i in range(1, N+1)]
permutation(lst,N)
