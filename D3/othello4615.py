cases = int(input())

for case in range(cases):
    N, M = map(int, input().split())
    board = [[0 for _ in range(N)] for _ in range(N)]
    board[int(N/2)-1][int(N/2)-1] = 2
    board[int(N/2)][int(N/2)] = 2
    board[int(N/2)-1][int(N/2)] = 1
    board[int(N/2)][int(N/2)-1] = 1


    while M>0:
        i, j, c = map(int, input().split())
        i -= 1
        j -= 1
        
        if i+1<N: # 오른쪽
            if board[j][i+1] != c and board[j][i+1] != 0:
                for b in range(i+2,N):
                    if board[j][b] == c:
                        for a in range(i,b):
                            board[j][a] = c
                        break
                    elif board[j][b] == 0:
                        break

        if i-1>=0:# 왼쪽
            if board[j][i-1] != c and board[j][i-1] != 0:
                for b in range(i-2,-1,-1):
                    if board[j][b] == c:
                        for a in range(b+1,i+1):
                            board[j][a] = c
                        break
                    elif board[j][b] == 0:
                        break
        
        if j-1>=0: #위
            if board[j-1][i] != c and board[j-1][i] != 0:
                for b in range(j-2,-1,-1):
                    if board[b][i] == c:
                        for a in range(b+1,j+1):
                            board[a][i] = c
                        break
                    elif board[b][i] == 0:
                        break

        if j+1<N:#아래
            if board[j+1][i] != c and board[j+1][i] != 0:
                for b in range(j+2,N):
                    if board[b][i] == c:
                        for a in range(b-1,j-1,-1):
                            board[a][i] = c
                        break
                    elif board[b][i] == 0:
                        break

        if j+1<N and i+1<N: #오른쪽 아래
            if board[j+1][i+1] != c and board[j+1][i+1] != 0:
                for b in range(2,N):
                    if j+b<N and i+b<N:
                        if board[j+b][i+b] == c:
                            for a in range(0,b):
                                board[j+a][i+a] = c
                            break
                        elif board[j+b][i+b] == 0:
                            break
        
        if 0<=j-1 and i+1<N: # 오른쪽 위
            if board[j-1][i+1] != c and board[j-1][i+1] != 0:
                for b in range(2,N):
                    if j-b>=0 and i+b < N:
                        if board[j-b][i+b] == c:
                            for a in range(0,b):
                                board[j-a][i+a] = c
                            break
                        elif board[j-b][i+b] == 0:
                            break

        if j+1<N and i-1>=0: # 왼쪽 아래
            if board[j+1][i-1] != c and board[j+1][i-1] != 0:
                for b in range(2,N):
                    if j+b<N and i-b>=0:
                        if board[j+b][i-b] == c:
                            for a in range(0,b):
                                board[j+a][i-a] = c
                            break
                        elif board[j+b][i-b] == 0:
                            break

        if j-1>=0 and i-1>=0: # 왼쪽 위
            if board[j-1][i-1] != c and board[j-1][i-1] != 0:
                for b in range(2,N):
                    if j-b>=0 and i-b>=0:
                        if board[j-b][i-b] == c:
                            for a in range(0,b):
                                board[j-a][i-a] = c
                            break
                        elif board[j-b][i-b] == 0:
                            break


        # for i in range(len(board)):
        #     print(board[i])
        M -= 1

    black = 0
    white = 0
    for i in range(N):
        black += board[i].count(1)
        white += board[i].count(2)
    print(f'#{case+1} {black} {white}')