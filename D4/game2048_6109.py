def turn(d):
    direction = {'right': 0, 'up': 1, 'left': 2, 'down': 3}
    tmp = [[0]*int(N) for _ in range(int(N))]
    if direction[d] == 1:
        for i in range(int(N)):
            for j in range(int(N)):
                tmp[i][j] = base[int(N)-j-1][i]
    elif direction[d] == 2:
        for i in range(int(N)):
            for j in range(int(N)):
                tmp[i][j] = base[int(N)-i-1][int(N)-j-1]
    elif direction[d] == 3:
        for i in range(int(N)):
            for j in range(int(N)):
                tmp[i][j] = base[j][int(N)-i-1]
    else:
        for i in range(int(N)):
            for j in range(int(N)):
                tmp[i][j] = base[i][j]
    for i in range(int(N)):
        for j in range(int(N)):
            if tmp[i][j] == 0:
                tmp[i].pop(j)
                tmp[i].insert(0,0)
        j = int(N)-1
        while j > 0:
            if tmp[i][j] == 0:
                break
            if tmp[i][j] == tmp[i][j-1]:
                tmp[i][j-1] = 0
                tmp[i][j] *= 2
                j -= 2
            else:
                j -= 1
        for j in range(int(N)):
            if tmp[i][j] == 0:
                tmp[i].pop(j)
                tmp[i].insert(0,0)
    if direction[d] == 3:
        for i in range(int(N)):
            for j in range(int(N)):
                base[i][j] = tmp[int(N)-j-1][i]
    elif direction[d] == 2:
        for i in range(int(N)):
            for j in range(int(N)):
                base[i][j] = tmp[int(N)-i-1][int(N)-j-1]
    elif direction[d] == 1:
        for i in range(int(N)):
            for j in range(int(N)):
                base[i][j] = tmp[j][int(N)-i-1]
    else:
        for i in range(int(N)):
            for j in range(int(N)):
                base[i][j] = tmp[i][j]

T = int(input())
for tc in range(1,T+1):
    N, D = input().split()
    base = [list(map(int,input().split())) for _ in range(int(N))]
    turn(D)
    print(f'#{tc}')
    for i in range(int(N)):
        print(' '.join(map(str,base[i])))