N = int(input())
chess = [[0 for _ in range(N)] for _ in range(N)]
dx = [1, 1, 1]
dy = [0, -1, 1]
queen = 0
cnt = 0
def back(row): # 퀸찍기
    global queen
    global cnt
    if queen == N:
        cnt += 1
        return
    else:
        for i in range(N):
            if chess[row][i] == 0:
                chess[row][i] = -1
                queen += 1
                attack(row,i)
                back(row+1)
                chess[row][i] = 0
                queen -= 1
                bockgu(row,i)

def attack(x,y): # 공격범위 증가
    for k in range(3):
        nx, ny = dx[k]+x,dy[k]+y
        if 0<=nx<N and 0<=ny<N and chess[nx][ny] != -1:
            while 0<=nx<N and 0<=ny<N:
                chess[nx][ny] += 1
                nx += dx[k]
                ny += dy[k]
def bockgu(x,y): # 공격범위 감소
    for k in range(3):
        nx, ny = dx[k]+x,dy[k]+y
        if 0<=nx<N and 0<=ny<N and chess[nx][ny] != -1:
            while 0<=nx<N and 0<=ny<N:
                chess[nx][ny] -= 1
                nx += dx[k]
                ny += dy[k]
back(0)
print(cnt)
                
    
