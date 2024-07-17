n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
BLANK = 0


# col 열에 중력 작용
def fall(col):
    global grid, n
    # col 열을 아래부터 확인하여 0이 아닌 것을 tmp로 옮김
    tmp = [0 for _ in range(n)]
    idx = n-1  # tmp도 아래부터 채운다
    for i in range(n-1, -1, -1):
        if grid[i][col] != BLANK:
            tmp[idx] = grid[i][col]
            idx = idx-1
    
    # 기존 grid를 tmp로 업데이트
    for i in range(n):
        grid[i][col] = tmp[i]


# 십자 모양 폭발
def boom(row, col):
    global grid
    intensity = grid[row][col] -1

    # 폭발 범위 계산
    start_r = max(0, row-intensity)
    end_r = min(n-1, row+intensity)

    start_c = max(0, col-intensity)
    end_c = min(n-1, col+intensity)

    # 폭탄 터짐
    for i in range(start_r, end_r+1):
        grid[i][col] = BLANK
    
    for i in range(start_c, end_c+1):
        grid[row][i] = BLANK
    
    # 중력 작용
    for i in range(start_c, end_c+1):
        fall(i)


r, c = map(int, input().split())
boom(r-1, c-1)

for i in range(n):
    print(*grid[i])