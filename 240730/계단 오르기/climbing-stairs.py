n = int(input())

step = [0 for _ in range(n+1)]
M = 10007

step[2] = 1
if n >= 3:
    step[3] = 1

# 0 ~ n-2까지 
for i in range(n-1):
    step[i+2] += step[i]
    step[i+2] %= M
    
    if i < n-2:
        step[i+3] += step[i]
        step[i+3] %= M


print(step[n])