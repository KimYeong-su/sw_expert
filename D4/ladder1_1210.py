for tc in range(1,11):
    case = int(input())
    base=[list(map(int,input().split())) for _ in range(100)]

    for i in range(100):
        j = 0
        d = i
        if base[j][d] == 1:
            while j != 99:
                if  0<=d<99 and base[j][d+1]==1:
                    base[j][d] = 3
                    d += 1
                elif 0<d<=99 and base[j][d-1]==1:
                    base[j][d] = 3
                    d -= 1
                else:
                    base[j][d] = 3
                    j += 1

        for x in range(100):
            for y in range(100):
                if base[x][y] == 3:
                    base[x][y] = 1
        if base[j][d]==2:
            print('#{} {}'.format(tc,i))
            break