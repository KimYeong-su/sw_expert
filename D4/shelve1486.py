T = int(input())

for tc in range(1,T+1):
    N, B = map(int,input().split())
    clerk = list(map(int,input().split()))

    result = 10000
    for i in range(1<<N):
        temp = 0
        for j in range(N+1):
            if i & (1<<j):
                temp += clerk[j]
        if temp >= B:
            if result > temp-B:
                result = temp-B
    print('#{} {}'.format(tc,result))