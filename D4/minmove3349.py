T = int(input())

for tc in range(1,T+1):
    W,H,N = map(int,input().split())
    order = [tuple(map(int,input().split()))for _ in range(N)]

    result = 0
    for i in range(N-1):
        x1, y1 = order[i]
        x2, y2 = order[i+1]
        if x1<=x2 and y1<=y2:
            for k in range(10001):
                if x2==x1+k or y2==y1+k:
                    result += x2-x1+y2-y1-k
                    break
        elif x1>x2 and y1>y2:
            for k in range(10001):
                if x1==x2+k or y1==y2+k:
                    result += x1-x2+y1-y2-k
                    break
        else:
            result += abs(x2-x1)+abs(y2-y1)

    print('#{} {}'.format(tc,result))