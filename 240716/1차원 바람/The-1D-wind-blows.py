n, m, q = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
LEFT = True
RIGHT = False


# 바람이 row 행을 direction 방향으로 민다
def push(row, direction):
    global matrix, LEFT, RIGHT, m
    if direction == LEFT: # 왼쪽으로 밀린다
        # tmp = matrix[row].pop()
        # matrix[row].insert(0, tmp)

        tmp = matrix[row][-1]
        for i in range(m-1, 0, -1):
            matrix[row][i] = matrix[row][i-1]
        matrix[row][0] = tmp
    else: # 오른쪽으로 밀린다
        tmp = matrix[row][0]
        for i in range(0, m-1):
            matrix[row][i] = matrix[row][i+1]
        matrix[row][-1] = tmp


def check_prop_condition(r1, r2): # r1행과 r2행이 전파 조건에 해당하는지 판단
    global m
    for i in range(m):
        if matrix[r1][i] == matrix[r2][i]:
            return True # 하나라도 같은 열에 일치하는 수가 같다면 전파 대상
    return False # 전파 X


def wind(init_row, init_direction):
    global n, matrix
    push(init_row, init_direction)

    # 전파 대상 비교 기준 행, -1이면 전파 X
    prop_upper_row = init_row
    prop_lower_row = init_row
    # 다음 전파 방향
    prop_upper_d = not init_direction
    prop_lower_d = not init_direction

    for i in range(1, n):
        # 위쪽 방향 전파
        if prop_upper_row != -1 and init_row - i >= 0: # matrix 범위 내인지 체크
            # init_row - i 번째 행이 유효함 -> 전파 조건 체크 (현재 행과 기준 행 비교)
            cur_row = init_row - i
            if check_prop_condition(cur_row, prop_upper_row):
                # 전파 조건 만족
                push(cur_row, prop_upper_d)
                
                prop_upper_row = cur_row # 다음 전파 기준 지정
                prop_upper_d = not prop_upper_d # 다음 전파 방향 지정

            else:
                prop_upper_row = -1
        
        # 아래쪽 방향 전파
        if prop_lower_row != -1 and init_row + i < n:
            # init_row + i 번째 행이 유효함 -> 전파 조건 체크
            cur_row = init_row + i
            if check_prop_condition(cur_row, prop_lower_row):
                # 전파 조건 만족
                push(cur_row, prop_lower_d)
                prop_lower_row = cur_row # 다음 전파 기준 지정
                prop_lower_d = not prop_lower_d # 다음 전파 방향 지정

            else:
                prop_lower_row = -1
    

for i in range(q):
    r, d = input().split()
    r = int(r) - 1
    if (d == 'L'):
        wind(r, LEFT)
    else:
        wind(r, RIGHT)

for i in range(n):
    print(*matrix[i])