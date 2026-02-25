# N과 M (4)

N, M = map(int,input().split())

ans = []
def back(count,start):
    if count == M:
        print(*ans)
        return
    for i in range(start,N+1):
        ans.append(i)
        back(count + 1, i)
        ans.pop()
        
back(0,1)