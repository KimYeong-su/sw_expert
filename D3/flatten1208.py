cases = 10
for case in range(cases):
    N = int(input())
    base = list(map(int,input().split()))
    while N>0:
        Max = base.index(max(base))
        Min = base.index(min(base))
        base[Max] -=1
        base[Min] +=1
        N -= 1

    result = base[base.index(max(base))] - base[base.index(min(base))]
    print('#{} {}'.format(case+1, result))