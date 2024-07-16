n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]


# arr이 행복한 수열인지 판단
def is_happy_sequence(arr):
    for i in range(n-m+1):  # 인덱스 0부터 n-m까지
        # 인덱스 i부터 연속된 m개 확인 -> m개가 모두 같으면 행복한 수열에 해당
        is_happy = True
        for j in range(i, i+m-1):
            if arr[j] != arr[j+1]:
                is_happy = False
                break # m개 중 값이 다른 것이 있으므로 다른 m개를 확인하기 위해 넘어감
        if is_happy: # 이번 m개를 확인하며 계속 is_happy를 True로 유지했다면 m개가 같은 것이므로 행복한 수열에 해당
            return True
    return False # 위에서 리턴되지 못했다면 m개가 같은 경우가 없었음을 의미하므로 arr는 행복한 수열이 아님


result = 0
for i in range(n):
    col_list = [grid[j][i] for j in range(n)]
    if is_happy_sequence(grid[i]):
        result = result + 1
    if is_happy_sequence(col_list):
        result = result + 1

print(result)