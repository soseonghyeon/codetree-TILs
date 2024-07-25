n = int(input())

# 사람은 True, 벽은 False -> True인 곳만 갈 수 있음
grid = [list(map(lambda x: True if x=='1' else False, input().split()))
        for _ in range(n)]

visited = [[False]*n for _ in range(n)]
# 상하좌우
dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]


# dfs에 들어오면 특정 노드를 방문한 것
# 따라서 dfs 재귀 호출 횟수 == 마을 사람 수
def dfs(x, y):
    global grid, visited, dxs, dys, n

    visited[x][y] = True
    count = 0

    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        
        if visited[nx][ny] or not grid[nx][ny]:
            continue
        
        count += dfs(nx, ny)

    return 1 + count


humans = []
for i in range(n):
    for j in range(n):
        if grid[i][j] and not visited[i][j]:
            humans.append(dfs(i, j))

humans.sort()
print(len(humans))
for num in humans:
    print(num)