# 괄호
from collections import deque
T = int(input())
for i in range(T):
    count = 0
    sol = deque(list(input()))
    for _ in range(len(sol)):
        c = sol.popleft()
        if c == '(':
            count += 1
        else:
            count -= 1
        if count < 0:  
            break
    if count == 0:
        print("YES")
    else:
        print("NO")
        