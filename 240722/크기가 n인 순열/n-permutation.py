n = int(input())
arr = []
visited = [False for _ in range(n+1)]

def permutation(count):
    global n

    if count > n:
        print(*arr)
        return
    
    for i in range(1, n+1):
        if visited[i]:
            continue
        
        visited[i] = True
        arr.append(i)
        permutation(count+1)
        arr.pop()
        visited[i] = False

    return

permutation(1)