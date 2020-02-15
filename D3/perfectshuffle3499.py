T = int(input())

for tc in range(1,T+1):
    n = int(input())
    base = list(input().split())

    base2 = []
    for i in range(n//2):
        if n%2==0:
            base2.append(base.pop(n//2))
        else:
            base2.append(base.pop(n//2+1))
    
    result = []
    while True:
        if len(base)!=0:
            result.append(base.pop(0))
        if len(base2)!=0:
            result.append(base2.pop(0))
        if len(base)==0 and len(base2)==0:
            break

    r = ' '.join(map(str,result))
    print('#{} {}'.format(tc,r))