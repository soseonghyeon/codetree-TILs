# 모든 행이 각자 다른 열에 한 칸씩 색칠해야 함
# 따라서 0 ~ n-1 까지의 수를 나열하는 순열을 구하는 문제

n = int(input())
grid = [list(map(int, input().split()))
        for _ in range(n)]
visited = [False] * n

result = 0


def select(count, sum_val):
    global n, result
    if count >= n:
        result = max(result, sum_val)
        return
    
    # count번째 행에서 i번째 column 색칠
    for i in range(n):
        if visited[i]:
            continue
        
        visited[i] = True
        select(count+1, sum_val+grid[count][i])
        visited[i] = False


select(0, 0)
print(result)