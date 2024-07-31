# 변수 선언 및 입력:
n = int(input())
arr = list(map(int, input().split()))

# dp[i] :
# 마지막으로 고른 원소의 위치가 i인
# 부분 수열 중 최장 감소 부분 수열의 길이
dp = [0] * n

for i in range(n):
    # 현재 위치에서 시작할 때에는
    # dp값이 1이 되므로
    # 초기 셋팅은 1입니다.
    dp[i] = 1

    # i번째 보다 앞에 있는 원소들 중 
    # arr[i]보다는 값이 큰 곳에 
    # 새로운 원소인 arr[i]를 추가했을 때의 
    # 부분 수열 중 최대 감소 부분 수열의 길이를 계산합니다.
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 마지막 원소의 위치가 i일 때의 부분 수열들 중
# 가장 길이가 긴 감소 부분 수열을 고릅니다.
ans = 0
for i in range(n):
    ans = max(ans, dp[i])

print(ans)