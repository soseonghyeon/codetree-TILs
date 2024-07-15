n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def num_of_coin(row_s, col_s):
    result = 0
    for i in range(row_s, row_s+3):
        for j in range(col_s, col_s+3):
            result += grid[i][j]
    return result


max_coin = 0
for i in range(n-2):
    for j in range(n-2):
        max_coin = max(max_coin, num_of_coin(i, j))

print(max_coin)