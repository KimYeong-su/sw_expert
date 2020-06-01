import heapq

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    E = float(input())
    visit = [False]*N
    key = [float('inf')]*N
    key[0]=0
    pq = []
    heapq.heappush(pq,(0,0))
    while pq:
        k,node = heapq.heappop(pq)
        if visit[node]: continue
        visit[node]=True
        for i in range(N):
            tax = E*(abs(x[node]-x[i])**2+abs(y[node]-y[i])**2)
            if not visit[i] and tax<key[i]:
                key[i]  = tax
                heapq.heappush(pq,(key[i],i))
    result = round(sum(key))
    print('#{} {}'.format(tc,result))