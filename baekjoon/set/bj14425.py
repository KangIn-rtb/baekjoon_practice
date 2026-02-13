# 문자열 집합 


N, M = map(int,input().split())
sol = [input() for _ in range(N)]
sol = set(sol)
count = 0
for i in range(M):
    if input() in sol:
        count += 1
print(count)