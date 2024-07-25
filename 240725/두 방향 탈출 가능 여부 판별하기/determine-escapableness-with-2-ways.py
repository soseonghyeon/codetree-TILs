# 아래, 오른쪽 방향
dxs = [1, 0]
dys = [0, 1]

n, m = map(int, input().split())
grid = [list(map(lambda x: True if x == '1' else False, input().split()))
        for _ in range(n)]

visited = [[False]*m
            for _ in range(n)]


def dfs(x, y):
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
    
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        
        if visited[nx][ny] or not grid[nx][ny]:
            continue
        
        visited[nx][ny] = True
        dfs(nx, ny)


visited[0][0] = True
dfs(0, 0)

if visited[n-1][m-1]:
    print(1)
else:
    print(0)