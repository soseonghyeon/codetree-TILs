n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

k -= 1

row = n-1
for i in range(1, n):
    is_fill = False
    for j in range(k, k+m):
        if grid[i][j] == 1:
            row = i - 1
            is_fill = True
    if is_fill:
        break

for i in range(k, k+m):
    grid[row][i] = 1

for i in range(n):
    print(*grid[i])