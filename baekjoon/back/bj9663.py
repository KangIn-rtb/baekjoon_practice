# N = int(input())
# chess = [[0 for _ in range(N)] for _ in range(N)]
# dx = [1, 1, 1]
# dy = [0, -1, 1]
# queen = 0
# cnt = 0
# def back(row): # 퀸찍기
#     global queen
#     global cnt
#     if queen == N:
#         cnt += 1
#         return
#     else:
#         for i in range(N):
#             if chess[row][i] == 0:
#                 chess[row][i] = -1
#                 queen += 1
#                 attack(row,i)
#                 back(row+1)
#                 chess[row][i] = 0
#                 queen -= 1
#                 bockgu(row,i)

# def attack(x,y): # 공격범위 증가
#     for k in range(3):
#         nx, ny = dx[k]+x,dy[k]+y
#         if 0<=nx<N and 0<=ny<N and chess[nx][ny] != -1:
#             while 0<=nx<N and 0<=ny<N:
#                 chess[nx][ny] += 1
#                 nx += dx[k]
#                 ny += dy[k]
# def bockgu(x,y): # 공격범위 감소
#     for k in range(3):
#         nx, ny = dx[k]+x,dy[k]+y
#         if 0<=nx<N and 0<=ny<N and chess[nx][ny] != -1:
#             while 0<=nx<N and 0<=ny<N:
#                 chess[nx][ny] -= 1
#                 nx += dx[k]
#                 ny += dy[k]
# back(0)
# print(cnt)
import sys

def solve():
    # 입력을 빠르게 받기
    line = sys.stdin.readline().strip()
    if not line: return
    N = int(line)
    
    # N=1인 경우 예외 처리
    if N == 1:
        print(1)
        return

    # 모든 비트가 1인 마스크 (N=4이면 1111(2))
    full_mask = (1 << N) - 1
    count = 0

    def backtrack(row_mask, ld_mask, rd_mask):
        nonlocal count
        # 모든 열에 퀸이 놓임 (마스크가 꽉 참)
        if row_mask == full_mask:
            count += 1
            return

        # 놓을 수 있는 자리 찾기 (1인 비트가 놓을 수 있는 곳)
        # (row | ld | rd)는 공격받는 곳, ~는 비어있는 곳, & full_mask는 범위 한정
        pos = ~(row_mask | ld_mask | rd_mask) & full_mask

        while pos:
            # 가장 오른쪽에 있는 1비트 추출 (가장 왼쪽 빈 칸)
            bit = pos & -pos
            # 해당 자리에 퀸을 놓고 다음 행으로 (대각선 비트 시프트가 핵심!)
            backtrack(row_mask | bit, (ld_mask | bit) << 1, (rd_mask | bit) >> 1)
            # 사용한 비트 제거
            pos &= ~bit

    # 대칭성 최적화: 첫 번째 행의 절반만 탐색
    # 000...001 부터 시작해서 절반까지만 비트를 옮기며 탐색
    half = N // 2
    for i in range(half):
        bit = 1 << i
        # 첫 번째 퀸을 놓고 재귀 시작
        backtrack(bit, bit << 1, bit >> 1)
    
    count *= 2 # 좌우 대칭 적용

    # N이 홀수라면 가운데 열을 별도로 계산
    if N % 2 == 1:
        temp_count = count
        count = 0 # 임시로 0으로 초기화해서 가운데 결과만 측정
        bit = 1 << (N // 2)
        backtrack(bit, bit << 1, bit >> 1)
        count = temp_count + count

    print(count)

if __name__ == "__main__":
    solve()
