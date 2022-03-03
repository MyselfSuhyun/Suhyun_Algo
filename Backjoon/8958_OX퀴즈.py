T = int(input())

for _ in range(T):
    quiz = input()
    score = 0
    is_valid = False
    tmp = 0
    for q in quiz:
        if q =='O' and is_valid:
            score += tmp
            tmp +=1
        elif q =='O':
            score += 1
            tmp = 2
            is_valid = True
        else:
            is_valid = False
    print(score)
