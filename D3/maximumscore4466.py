T = int(input())

for tc in range(1,T+1):
    N, K = map(int,input().split())
    score = list(map(int,input().split()))
    score_sort = list(sorted(score,reverse=True))

    maximum = 0
    for i in range(K):
        maximum += score_sort[i]
    print('#{} {}'.format(tc,maximum))