n, m = map(int, input().split())
START = 1

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

visited[START] = True
result = 0

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(node):
    global grahp, visited, result

    for next_node in graph[node]:
        if visited[next_node]:
            continue
        
        visited[next_node] = True
        result += 1
        dfs(next_node)


dfs(START)
print(result)