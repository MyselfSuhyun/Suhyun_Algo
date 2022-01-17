# 딕셔너리로 우선 주사위 고유별칭을 담아주자.
dice = {1:'Yakk',2:'Doh',3:'Seh',4:'Ghar',5:'Bang',6:'Sheesh'}
double_dice = {1:'Habb Yakk',2:'Dobara',3:'Dousa',4:'Dorgy',5:'Dabash',6:'Dosh'}
# 테스트 케이스의 수는 T 이다.
T = int(input())
for tc in range(1,T+1):
    # 던진 주사위를 리스트로 받고, 이를 내림차순 해주자.
    throw = list(map(int,input().split()))
    throw.sort(reverse=True)

    # 주사위의 눈이 일치할 경우
    if throw[0] == throw[1]:
        print(f'Case {tc}: {double_dice[throw[0]]}')
    # Sheesh Bang 이 나오는 5-6, 6-5 의 경우
    elif throw[0]==6 and throw[1]==5:
        print(f'Case {tc}: Sheesh Beesh')
    # 일치하지 않을 경우,
    else:
        print(f'Case {tc}: {dice[throw[0]]} {dice[throw[1]]}')
