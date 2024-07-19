# 인접한 여덟 칸 표현 (순서 무관: 범위 내의 수가 한 번씩만 등장하기 때문에 우선순위 필요 X)
drs = [-1, 1, 0, 0, -1, -1, 1, 1]
dcs = [0, 0, 1, -1, -1, 1, 1, -1]

n, m = map(int, input().split())
grid = [list(map(int, input().split()))
        for _ in range(n)]


def get_num_pos(num):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == num:
                return i, j
    
    return -1, -1


def move_num():
    # 1부터 n*n 수를 순서대로 이동
    for i in range(1, n*n+1):
        # 이번 숫자의 위치를 알아낸다
        r, c = get_num_pos(i)
        # 주위 8방향 확인하여 가장 큰 수 찾기
        max_val = 0
        mr, mc = -1, -1
        for dr, dc in zip(drs, dcs):
            nr, nc = r+dr, c+dc
            # 유효 범위 밖이라면 넘긴다
            if nr<0 or nr>=n or nc<0 or nc>=n:
                continue
            # 인접 최댓값 갱신
            if grid[nr][nc] > max_val:
                max_val = grid[nr][nc]
                mr, mc = nr, nc
        # 인접 최댓값과 가운데 칸 swap
        tmp = grid[r][c]
        grid[r][c] = grid[mr][mc]
        grid[mr][mc] = tmp


for _ in range(m):
    move_num()

for i in range(n):
    print(*grid[i])