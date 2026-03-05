# 01타일
import sys
input = sys.stdin.readline
N = int(input())
a,b,c = 1,2,0
for i in range(3,N+1):
    c = (a + b)%15746
    b,a = c,b
if N <= 2:
    print(N)
else:
    print(c%15746)
    
