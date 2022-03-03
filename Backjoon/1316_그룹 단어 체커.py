N = int(input()) # 단어의 개수
answer = 0 # 답안출력

for _ in range(N):
    S = input()
    dic_alpha = {}
    for i in range(ord('a'),ord('z')+1):
        dic_alpha[i] = []
    for j in range(len(S)):
        if not dic_alpha[ord(S[j])]:
            dic_alpha[ord(S[j])] = [j]
        else:
            if dic_alpha[ord(S[j])][-1] == j-1:
                dic_alpha[ord(S[j])].append(j)
            else:
                break
    else:
        answer+=1
print(answer)
