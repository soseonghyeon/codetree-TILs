n = int(input())

step = [0 for _ in range(n+1)]

# 0 ~ n-2까지 
for i in range(n-1):
    if step[i+2] == 0:
        step[i+2] = step[i]+1
    
    if i < n-2 and step[i+3] == 0:
        step[i+3] = step[i]+1


print(step[n])