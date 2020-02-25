def area(x,y,K):
    temp = 0
    for a in range(x-K+1,x+K):
        if 0<=a<N:
            for b in range(y-(K-abs(a-x))+1,y+(K-abs(a-x))):
                if 0<=b<N:
                    if base[a][b]==1:
                        temp+=1
    return temp


T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())

    base = [list(map(int,input().split()))for _ in range(N)]
    
    home = 0
    for i in range(N):
        for j in range(N):
            if base[i][j]==1:
                home +=1
    maximum = 0
    for k in range(22):
        money = 2*k**2-2*k+1 #운영비용
        for i in range(N):
            for j in range(N):
                cnt = area(i,j,k)
                if M*cnt-money>0:
                    if maximum<cnt:
                        maximum = cnt

    print('#{} {}'.format(tc,maximum))