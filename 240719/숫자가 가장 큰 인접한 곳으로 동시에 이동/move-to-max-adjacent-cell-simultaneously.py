n, m, t = map(int, input().split())
grid = [list(map(int, input().split()))
        for _ in range(n)]

# 상하좌우 순 정의 (우선순위 부여)
drs = [-1, 1, 0, 0]
dcs = [0, 0, -1, 1]

beads = [list(0 for _ in range(n))
        for _ in range(n)] # n*n 배열, 0으로 초기화

for i in range(m):
    r, c = map(int, input().split())
    beads[r-1][c-1] = 1

def move_beads():
    # 새로운 n*n 배열 생성
    new_beads = [list(0 for _ in range(n))
                for _ in range(n)]
    
    # 구슬 이동
    for i in range(n):
        for j in range(n):
            # 구슬의 상하좌우 탐색
            if beads[i][j] == 1:
                mr, mc = -1, -1
                max_value = 0
                for dr, dc in zip(drs, dcs):
                    nr = i + dr
                    nc = j + dc
                    # 새로운 위치가 유효한 범위에 해당하지 않는다면 넘긴다
                    if nr<0 or nr>=n or nc<0 or nc>=n:
                        continue
                    # 유효한 범위 내라면 max값 갱신
                    if grid[nr][nc] > max_value:
                        max_value = grid[nr][nc]
                        mr, mc = nr, nc
                # 새로운 배열에 구슬의 새로운 위치를 업데이트
                new_beads[mr][mc] += 1
            
    # 기존 리스트에 새 리스트 내용 복사
    for i in range(n):
        beads[i] = new_beads[i][:]
    
    # 위치 중복된 구슬 제거
    for i in range(n):
        for j in range(n):
            if beads[i][j] >= 2:
                beads[i][j] = 0
    

for _ in range(t):
    move_beads()

num_of_beads = 0
for i in range(n):
    for j in range(n):
        if beads[i][j] == 1:
            num_of_beads += 1

print(num_of_beads)