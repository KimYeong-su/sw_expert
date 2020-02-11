T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())

    base = [0 for _ in range(N)]

    for i in range(1,Q+1):
        L, R = map(int,input().split())
        L -= 1
        R -= 1
        for j in range(L,R+1):
            base[j] = i
    
    print('#{} {}'.format(tc,' '.join(map(str,base))))
    
