T = int(input())

for tc in range(1,T+1):
    D, H, M = map(int, input().split())

    result = -11*60-11
    result += (D-11)*24*60+H*60+M
    if result < 0:
        result = -1
    
    print('#{} {}'.format(tc,result))
