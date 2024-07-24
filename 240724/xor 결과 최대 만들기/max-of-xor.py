n, m = map(int, input().split())
num_arr = [int(x) for x in input().split()]

result = 0
arr = []

def select_numbers(count, prev_idx, prev_xor):
    global result
    if count >= m:
        result = max(result, prev_xor)
        return
    
    # xor은 결힙, 교환 법칙이 성립하므로 뽑는 순서는 중요하지 않음
    # 숫자 구성만 같으면 결과가 같으므로 n개 중 m개를 뽑는 조합을 얻어야 함
    # 이를 위해 num_arr의 인덱스 오름차순으로 선택

    for i in range(prev_idx+1, n):
        arr.append(num_arr[i])
        cur_xor = prev_xor ^ num_arr[i]
        select_numbers(count+1, i, cur_xor)
        arr.pop()
    
    return


# 0 xor A = A 이므로 초기 prev_xor은 0으로 한다
select_numbers(0, -1, 0)
print(result)