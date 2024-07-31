n = int(input())

arr = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + arr[i], arr[i])

result = dp[0]
for i in range(1, n):
    result = max(result, dp[i])

print(result)