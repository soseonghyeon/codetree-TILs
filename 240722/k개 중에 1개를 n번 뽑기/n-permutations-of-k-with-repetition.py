k, n = map(int, input().split())
arr = []

def choose_number(count):
    global k, n
    if count > n:
        print(*arr)
        return
    
    for i in range(1, k+1):
        arr.append(i)
        choose_number(count+1)
        arr.pop()
    
    return

choose_number(1)