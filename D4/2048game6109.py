T = int(input())
for tc in range(1,T+1):
    n, S = map(str,input().split())
    N = int(n)

    base = [list(map(int,input().split())) for _ in range(N)]
    i = 1
    if S == 'up':
        while i != N:
            for j in range(N):
                if base[i][j] != 0:
                    if base[i-1][j] == 0:
                        base[i-1][j] = base[i][j]
                        base[i][j] = 0
                    elif base[i][j] == base[i-1][j]:
                        base[i-1][j] += base[i][j]
                        base[i][j] = 0
            i+=1

    print(base)
