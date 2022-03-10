n = int(input())
arr = list(map(int,input().split()))
students = int(input())
stud = [list(map(int,input().split()))for _ in range(students)]

for i in range(len(stud)):
    if stud[i][0] == 1:
        for j in range(stud[i][1]-1,n,stud[i][1]):
            if arr[j] == 0:
                arr[j] = 1
            else:
                arr[j] = 0

    elif stud[i][0] == 2:
        j = 0
        while True:
            if j == 0:
                if arr[stud[i][1]-1]:
                    arr[stud[i][1]-1] = 0
                else:
                    arr[stud[i][1]-1] = 1
            else:
                if 0<=stud[i][1]-1+j<n and 0<=stud[i][1]-1-j<n:
                    if arr[stud[i][1]-1-j] == arr[stud[i][1]-1+j]:
                        if arr[stud[i][1]-1-j]:
                            arr[stud[i][1]-1-j] = 0
                            arr[stud[i][1]-1+j] = 0
                        else:
                            arr[stud[i][1]-1-j] = 1
                            arr[stud[i][1]-1+j] = 1
                    else:
                        break
                else:
                    break
            j+=1


for i in range(0,n//20+1):
    print(*arr[20*i:20*(i+1)])