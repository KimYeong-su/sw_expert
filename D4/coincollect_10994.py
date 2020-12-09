import heapq

T = int(input())

for tc in range(1,T+1):
    N, K = map(int, input().split())
    coin = []
    get = []
    result = []

    for i in range(N):
        ci, di = map(int, input().split())
        get.append(ci)
        if di:
            heapq.heappush(coin,(-ci,0))
        else:
            heapq.heappush(coin,(-ci,-1))

    maxNum = 0
    maxCount = 0 
    maximum = K
    while coin:
        print(get)
        n, c = heapq.heappop(coin)
        # print(n,c)
        if maxCount < -c:
            maxNum = -n
            maxCount = -c
        elif maxCount == -c:
            if maxNum < -n:
                maxNum = -n
        tmp = list(sorted(coin))
        # print(tmp)
        for i in tmp:
            # print(get)
            nn = i[0] + n
            if -nn > K-1 or -nn in get or -nn > maximum-1: break
            nc = i[1] + c
            heapq.heappush(coin,(nn,nc))
            get.append(-nn)
        maximum = -n
            
            
    print('#{} {} {}'.format(tc, maxCount, maxNum))