arr = list(map(int, input().split()))

if 0 in arr:
    arr = arr[:arr.index(0)]

arr.reverse()

for a in arr:
    print(a, end=' ')