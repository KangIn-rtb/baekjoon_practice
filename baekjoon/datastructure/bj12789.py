# 도키도키 간식드리미
N = int(input())
human = list(map(int,input().split()))
sol = [0]
i = 1
for h in human:
    sol.append(h)
    while True:
        if sol[-1] == i:
            sol.pop()
            i += 1
        else:
            break
if N > i:
    print("Sad")
else:
    print("Nice")