n, m = map(int, input().split())

# 0 ~ n-1번 옷
# arr[i][0]: start, arr[i][1]: end, arr[i][2]: value
arr = [list(map(int, input().split()))
        for _ in range(n)]


def check_day(cloth_idx, day):
        if arr[cloth_idx][0] <= day and day <= arr[cloth_idx][1]:
                return True
        else:
                return False


# dp[i][j]: j번째 옷을 입었을 때, i번째 날의 최대 만족도
# i의 범위: 1 ~ m
# j의 범위: 0 ~ n-1
dp = [[0]*n
        for _ in range(m+1)]

for i in range(2, m+1):
    for j in range(n):
        # i번째 날에 j번째 옷을 입을 수 있으면 계산
        if check_day(j, i):
                max_value = 0
                for k in range(n):
                        if not check_day(k, i-1):
                                continue
                        # 전날에 k번째 옷을 입고, 오늘 j번째 옷을 입었을 때 누적 화려함 계산
                        cur_value = dp[i-1][k] + abs(arr[j][2] - arr[k][2])
                        # 최댓값 갱신
                        max_value = max(max_value, cur_value)
                dp[i][j] = max_value

print(max(dp[m]))