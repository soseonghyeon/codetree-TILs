n, t = map(int, input().split())
upper_list = list(map(int, input().split()))
lower_list = list(map(int, input().split()))
lower.reverse()


def simulate(sec):
    for _ in range(sec):
        tmp_u = upper_list[-1]
        tmp_l = lower_list[0]

        for i in range(n-1, 0, -1):
            upper_list[i] = upper_list[i-1]
        upper_list[0] = tmp_l

        for i in range(1, n, -1):
            upper_list[i-1] = upper_list[i]
        upper_list[0] = tmp_u


simulate(t)
for e in upper_list:
    print(e, end=' ')
print()
for e in lower_list:
    print(e, end=' ')