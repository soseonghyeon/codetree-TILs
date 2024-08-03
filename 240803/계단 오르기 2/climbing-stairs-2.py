n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [[0]*4 for _ in range(n+1)]
# dp[i][j]: i번째 계단을 올랐음 + 1계단 오르는 행동을 j번 했음
# i번째 계단을 오를 때, 1계단 올라서 도달한 것일 수도 있고 2계단 올라서 도달한 것일 수도 있음
# 따라서 dp[i][j]는 1계단 올랐을 때와 2계단 올랐을 때 중 큰 값
# 가능한 모든 j(1계단 오른 횟수)를 고려 -> dp[n]의 column 중 가장 큰 값을 찾아 최종 값으로 선택
# dp[i][j]가 0이라면 도달 불가능하므로 고려 X
# 1, 2층은 따로 초기화 필요. 0층에서 바로 올라갈 수 있음

dp[1][1] = arr[1]
dp[2][0] = arr[2]
dp[2][2] = dp[1][1] + arr[2]

for i in range(3, n+1):
    for j in range(4):
        # 1계단을 j번 오르면 j층이므로 현재 층 i가 j보다 작거나 같아야 오를 수 있음
        if i < j:
            continue

        one_step = 0
        two_step = 0

        if i-2>=0 and dp[i-2][j]>0:
            two_step = dp[i-2][j] + arr[i]
        
        if i-1>=0 and j-1>=0 and dp[i-1][j-1]>0:
            one_step = dp[i-1][j-1] + arr[i]
        
        dp[i][j] = max(one_step, two_step)


print(max(dp[n]))