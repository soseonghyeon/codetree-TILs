from collections import deque

n, k = map(int, input().split())

# True면 갈 수 있는 곳
grid = [list(map(lambda x: True if x =='0' else False, input().split()))
        for _ in range(n)]
visited = [[False]*n for _ in range(n)]

# 상하좌우
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

q = deque()
result = 0

for _ in range(k):
    r, c = map(lambda x: int(x)-1, input().split())
    q.append((r, c))
    visited[r][c] = True
    result += 1

while q:
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue

        if visited[nx][ny] or not grid[nx][ny]:
            continue
        
        q.append((nx, ny))
        visited[nx][ny] = True
        result += 1

print(result)