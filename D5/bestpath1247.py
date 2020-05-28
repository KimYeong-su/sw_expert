def check(s,e,result,cnt):
    global minimum
    if cnt==N+1:
        if minimum > result+d[s][e]:
            minimum = result+d[s][e]
        return
    for i in range(2,N+2):
        if visit[i]!=True and d[s][i]!=0:
            visit[i]=True
            if result+d[s][i]<minimum:
                check(i,e,result+d[s][i],cnt+1)
            visit[i]=False

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    p = list(map(int,input().split()))
    d = [[0]*(N+2) for _ in range(N+2)]
    for i in range(N+2):
        for j in range(N+2):
            if i!=j:
                d[i][j] = abs(p[i*2]-p[j*2])+abs(p[i*2+1]-p[j*2+1])
    minimum = float('inf')
    visit=[False]*(N+2)
    # print(d)
    visit[0]=True
    check(0,1,0,1)
    print('#{} {}'.format(tc,minimum))