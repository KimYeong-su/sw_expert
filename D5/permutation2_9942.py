def permute(temp):
    if False not in visit:
        a = []
        for i in temp:
            a.append(i)
        case.append(a)
        return
    for i in range(1,N+1):
        if visit[i-1]!=True:
            visit[i-1]=True
            temp.append(i)
            permute(temp)
            temp.pop()
            visit[i-1]=False

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    visit=[False]*N
    case = []
    permute([])
    result = 0
    for i in case:
        for j in case:
            score = 0
            for k in range(N):
                score += max(i[k],j[k])
                if score>=K:
                    result+=1
                    break
    print('#{} {}'.format(tc,result))