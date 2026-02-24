# 연구소
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
N, M = map(int,input().split())
lab = [list(map(int,input().split())) for _ in range(N)]
virus = []
blank = [] # 빈칸 뽑기
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            blank.append((i,j))
        elif lab[i][j] == 2:
            virus.append((i,j))

ans = 0
def backtrack(count, start): # 벽세우기 
    if count == 3:
        matrix = [row[:] for row in lab]
        result = bfs(virus, matrix)
        global ans
        ans = max(result, ans)
        return 
    for i in range(start, len(blank)):
        x,y = blank[i]
        lab[x][y] = 1
        backtrack(count+1, i+1)
        lab[x][y] = 0

def bfs(virus, matrix): # 바이러스 감염
    safe = 0
    queue = deque(virus)
    while queue:
        x,y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<= nx < N and 0<= ny <M and matrix[nx][ny] == 0:
                queue.append((nx,ny))
                matrix[nx][ny] = 2
    for row in matrix:
        safe += row.count(0)
    return safe
backtrack(0,0)
print(ans)