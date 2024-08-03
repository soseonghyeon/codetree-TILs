import sys

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

MIN_VALUE = -sys.maxsize+1
dp = [[MIN_VALUE]*(n+1) for _ in range(n+1)]
dp[0][0] = 0

start_idx = 0
for i in range(n):
    for j in range(n):
        if dp[i][j] == MIN_VALUE:
            continue

        # 두 값이 같으면 둘 모두 버려야만 함
        if arr2[i] == arr1[j]:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j])
        # 민우 카드가 버려짐: 아래 방향으로 전파, 민우 점수 획득
        elif arr2[i] < arr1[j]:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]+arr2[i])
        # 상대 카드가 버려짐: 오른쪽 방향으로 전파
        elif arr2[i] > arr1[j]:
            dp[i][j+1] = max(dp[i][j+1], dp[i][j])

        # 카드 버리기: 그냥 버리는 경우
        # 오른쪽 아래 대각선 방향으로 전파
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j])

result = 0
for i in range(n):
    result = max(result, dp[i][n])

result = max(result, max(dp[n]))

print(result)