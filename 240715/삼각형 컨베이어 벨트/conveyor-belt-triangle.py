n, t = map(int, input().split())
left_list = list(map(int, input().split()))
right_list = list(map(int, input().split()))
bottom_list = list(map(int, input().split()))


for _ in range(t):
    # 1초 시뮬레이션
    tmp_l = left_list[-1]
    tmp_r = right_list[-1]
    tmp_b = bottom_list[-1]

    for i in range(n-1, 0, -1):
        left_list[i] = left_list[i-1]
        right_list[i] = right_list[i-1]
        bottom_list[i] = bottom_list[i-1]
    
    left_list[0] = tmp_b
    right_list[0] = tmp_l
    bottom_list[0] = tmp_r

print(*left_list)
print(*right_list)
print(*bottom_list)