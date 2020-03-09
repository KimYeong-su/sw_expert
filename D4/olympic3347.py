T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    kinds = list(map(int,input().split()))
    k_count = [0 for _ in range(N)]
    price = list(map(int,input().split()))

    for i in range(M):
        for j in range(N):
            if price[i]>=kinds[j]:
                k_count[j]+=1
                break
    
    print('#{} {}'.format(tc,k_count.index(max(k_count))+1))