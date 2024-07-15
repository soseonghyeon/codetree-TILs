n = int(input())
jenga = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

BLANK = 0


def delete_jenga(s, e):
    global jenga
    for i in range(s-1, e):
        jenga[i] = BLANK

    tmp = [0 for i in range(n)]
    # 왼쪽에서부터 채운다
    idx = 0
    for i in range(n):
        if jenga[i] != BLANK:
            tmp[idx] = jenga[i]
            idx = idx+1

    jenga = tmp.copy()  # jenga = tmp[:]
    return idx


r1 = delete_jenga(s1, e1)
r2 = delete_jenga(s2, e2)

print(r2)
for i in range(r2):
    print(jenga[i])