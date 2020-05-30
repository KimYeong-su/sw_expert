T = int(input())
for tc in range(1,T+1):
    N = int(input())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    visit = [False]*N
    visit[0] = True
    for i in range(N-1):
        temp = float('inf')
        idx = -1
        for j in range(i+1,N):
            if visit[j]!=True:
                l = (abs(x[i]-x[j])**2+abs(y[i]-y[j])**2)**0.5
                if l<temp:
                    temp=l
                    idx = j
        visit[idx]=True
        