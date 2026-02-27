# N과 M(3)
N, M = map(int,input().split())
sol = []
def back():
    if len(sol) == M:
        print(*sol)
    else:
        for i in range(1,N+1):
            sol.append(i)
            back()
            sol.pop()
back()