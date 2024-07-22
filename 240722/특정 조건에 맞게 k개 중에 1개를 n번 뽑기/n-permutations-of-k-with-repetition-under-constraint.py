k, n = map(int, input().split())
arr = []

def choose_number_cond(count):
    global k, n

    if count > n:
        print(*arr)
        return
    
    for i in range(1, k+1):
        if count > 2:
            if i == arr[-1] and arr[-1] == arr[-2]:
                continue
        arr.append(i)
        choose_number_cond(count+1)
        arr.pop()

    return

choose_number_cond(1)