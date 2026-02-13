# 다리놓기 
# N <= M 상태에서 1ㄷ1 로 다리 놓기 다리는 겹치면 안됨
# 순서가 이미 정해져있는 뽑기 -> MCN 
# 펙토리얼 써야되는데 M최대가 30이라 애매함 되는지 안되는지 모르겠음 재귀
# 그니까 걍 dp 씀


def facto(n):
    dp = [1]*(n+1)
    for i in range(1,n+1):
        dp[i] = dp[i-1]*(i)
    return dp[-1]
    
T = int(input())
for i in range(T):
    N,M = map(int,input().split())
    MCN = facto(M)/(facto(N)*(facto(M-N)))
    print(int(MCN))