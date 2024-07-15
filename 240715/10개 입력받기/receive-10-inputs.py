arr = list(map(int, input().split()))

idx = 1
total = 0

for i in range(10):
    if arr[i] == 0:
        break
    idx = i
    total += arr[i]

average = total/(idx+1)
print(f'{total} {average:.1f}')