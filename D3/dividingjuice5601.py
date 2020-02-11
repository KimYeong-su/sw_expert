T = int(input())

for tc in range(1,T+1):
    N = int(input())
    s = '1/{}'.format(N) + ' '
    print('#{} {}'.format(tc, s*N))