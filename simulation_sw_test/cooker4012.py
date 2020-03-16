T = int(input())

for tc in range(1,T+1):
    N = int(input())
    table = [list(map(int,input().split()))for _ in range(N)]

    case = []
    for i in range(N):
        for j in range(i+1,N):
            case += [(i,j)]
    result=20000
    for i in range(len(case)):
        for j in range(i+1, len(case)):
            if case[j][0] not in case[i] and case[j][1] not in case[i]:
                a,b = case[i]
                c,d = case[j]
                if abs(table[a][b]+table[b][a]-table[c][d]-table[d][c])<result:
                    result = abs(table[a][b]+table[b][a]-table[c][d]-table[d][c])
    print('#{} {}'.format(tc,result))
