# 숫자 카드
# N개 카드 정수 M개 수가 적혀있는 숫자 카드를 가지고있는지 아닌지 구하기

N = int(input())
sang = set(map(int,input().split()))
M = int(input())
checkcard = list(map(int,input().split()))

for i in range(M):
    if checkcard[i] in sang:
        checkcard[i] = 1
    else:
        checkcard[i] = 0
print(*checkcard)