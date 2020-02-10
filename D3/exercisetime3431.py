T = int(input())

for tc in range(1,T+1):
    L, U, X = map(int,input().split())

    if L<=X<=U:
        print('#{} {}'.format(tc,0))
    elif X<L:
        print('#{} {}'.format(tc,L-X))
    elif U<X:
        print('#{} {}'.format(tc,-1))