# 토마토
import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

M,N = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
ick = []

def bfs(spot): # 그냥 모든 토마토의 위치를 spot에 때려넣고 시작 하면
                # 1일차에 처음에 저장된 모든 큐 쏟고 2일차 시작
    queue = deque(spot)
    day = 0
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<N and 0<=ny<M and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx,ny))
                day = matrix[x][y]
    return day

def check(matrix,result):
    for row in matrix:
        for i in row:
            if i == 0:
                print(-1)
                return 0
    print(result)
    return 0

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            ick.append((i,j)) # 익토 좌표
check(matrix, bfs(ick))