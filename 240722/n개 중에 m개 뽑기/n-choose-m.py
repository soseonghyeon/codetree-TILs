k, n = map(int, input().split())
arr = [0]

# 직전 수보다 더 큰 수만 append
# 파라미터로 넘겨도 되지만, arr의 마지막 원소 확인해도 됨
def choose_number_cond(count):
    global k, n

    if count > n:
        print(*arr[1:])
        return
    
    for i in range(arr[-1]+1, k+1):
        arr.append(i)
        choose_number_cond(count+1)
        arr.pop()

    return

choose_number_cond(1)