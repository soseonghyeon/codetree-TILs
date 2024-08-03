# 숫자의 길이 n을 입력받습니다.
n = int(input())

# 첫 번째 자리에 올 수 있는 숫자들의 경우의 수를 초기화합니다.
dp = [[0 for _ in range(15)] for _ in range(1005)]
for i in range(1, 10):
    dp[1][i] = 1

# 동적 프로그래밍을 사용하여 각 자리수마다 가능한 숫자들의 합을 계산합니다.
# dp[i][j] :: i자릿수 까지 봤을 때, 마지막 숫자가 j인 가짓수
MOD = 1000000007
for i in range(1, n):
    for j in range(10):
        # 숫자가 감소하는 경우를 고려합니다.
        if j > 0:
            dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % MOD

        # 숫자가 증가하는 경우를 고려합니다.
        if j < 9:
            dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD

# 최종 결과를 계산합니다.
ans = sum(dp[n]) % MOD

# 계산된 결과를 출력합니다.
print(ans)