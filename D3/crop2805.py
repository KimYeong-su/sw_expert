T = int(input())

for tc in range(1,T+1):
    N = int(input())
    base = [list(map(int,input())) for _ in range(N)]
    
    i = 0
    j = int((N-1)/2)
    c = 1
    sum = 0
    while i < N:
        if i < int((N-1)/2):
            for k in range(c):
                sum += base[i][j+k]
            c += 2
            j -= 1
        else:
            for k in range(c):
                sum += base[i][j+k]
            c -= 2
            j +=1
        i += 1

    print('#{} {}'.format(tc,sum))