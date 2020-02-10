T = int(input())

for tc in range(1,T+1):
    A, B, C = map(int,input().split())
    if A<B:
        result = C//A
    else:
        result = C//B
    print('#{} {}'.format(tc,result))