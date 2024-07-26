from collections import deque

n = int(input())

# 방문처리 및 깊이 저장
step = [[-1]*n for _ in range(n)]

# 나이트의 움직임
dxs, dys = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, 2, 1, -1, -2]

r1, c1, r2, c2 = map(lambda x: int(x)-1, input().split())

q = deque()
q.append((r1, c1))
step[r1][c1] = 0

while q:
    x, y = q.popleft()
    
    for dx, dy in zip(dxs, dys):
        # 인접한 새로운 위치의 좌표 계산
        nx, ny = x+dx, y+dy

        # 범위에서 벗어남
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        
        # 이미 방문했다면 넘긴다
        if step[nx][ny] != -1:
            continue
        
        # 유효한 범위의 새로운 좌표 방문 가능
        q.append((nx, ny))
        step[nx][ny] = step[x][y]+1

print(step[r2][c2])