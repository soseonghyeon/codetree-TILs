from collections import deque

n, m = map(int, input().split())
# True면 갈 수 있음
grid = [list(map(lambda x: True if x == '1' else False, input().split()))
        for _ in range(n)]

# 방문처리 및 깊이 저장
step = [[-1]*m for _ in range(n)]

# 상하좌우
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

q = deque()
q.append((0, 0))
step[0][0] = 0

while q:
    x, y = q.popleft()
    
    for dx, dy in zip(dxs, dys):
        # 인접한 새로운 위치의 좌표 계산
        nx, ny = x+dx, y+dy

        # 범위에서 벗어남
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        
        # 새로운 자리에 뱀이 있거나 이미 방문했다면 넘긴다
        if not grid[nx][ny] or step[nx][ny] != -1:
            continue
        
        # 유효한 범위의 새로운 좌표 방문 가능
        q.append((nx, ny))
        step[nx][ny] = step[x][y]+1

print(step[n-1][m-1])