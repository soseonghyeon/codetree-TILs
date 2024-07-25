from collections import deque
# queue 모듈은 멀티쓰레딩을 위한 동기화 과정을 거치므로 deque보다 느리다
# deque의 append(), popleft()를 통해 큐 사용

n, m = map(int, input().split())
# True면 뱀이 없음. 갈 수 있는 길
grid = [list(map(lambda x: True if x=='1' else False, input().split()))
        for _ in range(n)]
visited = [[False]*m for _ in range(n)]

# 상하좌우
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

q = deque()
q.append((0, 0))

while q: # while len(q):
    x, y = q.popleft()
    visited[x][y] = True
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        
        if visited[nx][ny] or not grid[nx][ny]:
            continue
        
        q.append((nx, ny))

if visited[n-1][m-1]:
    print(1)
else:
    print(0)