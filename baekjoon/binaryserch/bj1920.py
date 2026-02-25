# 수 찾기

N = int(input())
sol = list(map(int,input().split()))
M = int(input())
quiz = list(map(int,input().split()))    
check = dict()
for i in sol:
    check[i] = i
for i in quiz:
    if i in check:
        print(1)
    else:
        print(0)
        