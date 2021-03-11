def check(row, col):
    tmp = []
    for i in range(-1,2):
        if 0<=row+i<N:
            for j in range(-1,2):
                if 0<=col+j<N:
                    if base[row+i][col+j] == '*':
                        return []
                    else:
                        if i == j == 0: continue
                        tmp.append((row+i,col+j))
    base[row][col] = 0
    return tmp

def change(row, col):
    tmp = []
    cnt = 0
    for i in range(-1,2):
        if 0<=row+i<N:
            for j in range(-1,2):
                if 0<=col+j<N:
                    if i == j == 0: continue
                    if base[row+i][col+j] == '*':
                        cnt += 1
                    else:
                        tmp.append((row+i,col+j))
    base[row][col] = cnt
    visit[row][col] = True
    if cnt==0:
        return tmp
    else:
        return []

                        

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    base = [list(input()) for _ in range(N)]

    visit = [[False for _ in range(N)]for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if base[i][j] == '*':
                visit[i][j] = True

    queue = []
    answer = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j]: continue
            queue += check(i,j)
            if queue:
                answer += 1
            while queue:
                r,c = queue.pop(0)
                if visit[r][c]: continue
                queue += change(r,c)

    for i in range(N):
        answer += base[i].count('.')
    print(f'#{tc} {answer}')