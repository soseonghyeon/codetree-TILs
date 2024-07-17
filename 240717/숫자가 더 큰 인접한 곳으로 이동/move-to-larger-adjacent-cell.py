n, r, c = map(int, input().split())
r -= 1
c -= 1
grid = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우 순 변화량
# x: column, y: row
dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]


# x, y 좌표 범위가 grid 내에 있는지 체크
def in_range(y, x):
    return 0<=x and x<n and 0<=y and y<n


visited = [grid[r][c]]
is_moved = True
while is_moved:
    is_moved = False
    for dy, dx in zip(dys, dxs):
        ny, nx = r+dy, c+dx # 새로운 위치
        if not in_range(ny, nx): # 새로운 위치가 범위를 벗어남 -> 유효하지 않으므로 넘어감
            continue
        if grid[ny][nx] > grid[r][c]:
            r, c = ny, nx # 현재 위치보다 값이 더 크면 이동 -> 위치 갱신
            visited.append(grid[ny][nx])
            is_moved = True
            break
    
print(*visited)