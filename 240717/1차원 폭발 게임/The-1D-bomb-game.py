n, m = map(int, input().split())
bombs = [int(input()) for _ in range(n)]
END = -1


def bomb():
    global n, bombs

    bombs += [END] # 리스트의 끝을 표시하기 위해 END 추가
    target = bombs[0]
    cnt = 1
    is_change = False

    new_bombs = []

    for i in range(1, len(bombs)):
        if bombs[i] != target: # 현재 값이 이전까지의 값과 다름
            if cnt < m: # 이전 값이 m개 이하이므로 터지지 않음 -> 새 폭탄 리스트에 target을 cnt개 추가
                new_bombs += [target for _ in range(cnt)]
            else: # 이전 값이 m개 이상이면 터짐 -> 새 폭탄 리스트에 추가 X
                is_change = True # 폭탄이 터져 리스트가 처음과 달라짐 -> 리스트 변화 O

            # 타겟 갱신
            target = bombs[i]
            cnt = 1
        else: # 현재 값이 이전 값과 같음
            cnt = cnt+1
    
    bombs = new_bombs.copy() # bombs 갱신
    return is_change # bombs 변화 여부 리턴


is_change = True
while is_change: # is_change가 True인 동안 반복. 즉, bomb() 수행 결과 폭탄 리스트가 변화하지 않으면 멈춘다
    is_change = bomb()

print(len(bombs))
for i in range(len(bombs)):
    print(bombs[i])