n, m = map(int, input().split())
num_arr = [int(x) for x in input().split()]

result = 0

def select_numbers(count, idx, xor):
    global result

    if count >= m:
        result = max(result, xor)
        return
    
    if idx == n:
        return

    cur_xor = xor ^ num_arr[idx]

    # 이번 idx번째 원소를 선택함
    select_numbers(count+1, idx+1, cur_xor)

    # 이번 idx번째 원소를 선택하지 않음
    select_numbers(count, idx+1, xor)    


# 0 xor A = A 이므로 초기 prev_xor은 0으로 한다
select_numbers(0, 0, 0)
print(result)