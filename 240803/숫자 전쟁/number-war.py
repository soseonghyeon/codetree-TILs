n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

dp = [[0]*(n+1) for _ in range(n+1)]

black_row = []
black_col = []

for i in range(n):
    for j in range(n):
        if i in black_row or j in black_col:
            continue

        # 두 값이 같으면 둘 모두 버려야만 함
        # 둘 모두 카드를 넘기므로 이후 해당 행과 열은 전파 불가
        if arr2[i] == arr1[j]:
            black_row.append(i)
            black_col.append(j)

        # 민우 카드가 버려짐: 아래 방향으로 전파, 민우 점수 획득
        if arr2[i] < arr1[j]:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]+arr2[i])
        # 상대 카드가 버려짐: 오른쪽 방향으로 전파
        if arr2[i] > arr1[j]:
            dp[i][j+1] = max(dp[i][j+1], dp[i][j])


        # 카드 버리기: 그냥 버리는 경우
        # 오른쪽 아래 대각선 방향으로 전파
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j])

result = 0
for i in range(n):
    result = max(result, dp[i][n])

result = max(result, max(dp[n]))

print(result)