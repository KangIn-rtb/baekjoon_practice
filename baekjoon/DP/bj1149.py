# RGB 거리
import sys
input = sys.stdin.readline

N = int(input())
price = [0]*3
dp = list(map(int,input().split()))
for i in range(1,N):
    price = list(map(int,input().split()))
    pre_price = dp[:]
    pre_price[0] = min(price[0]+dp[1],price[0]+dp[2])
    pre_price[1] = min(price[1]+dp[0],price[1]+dp[2])
    pre_price[2] = min(price[2]+dp[1],price[2]+dp[0])
    dp = pre_price[:]
print(min(dp))
