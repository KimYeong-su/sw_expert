cases = int(input())

for case in range(cases):
    length = int(input())
    base = list(map(int,input().split()))

    a = []
    for i in base:
        if base.count(i)%2 ==1:
            a.append(i)
    
    result = []
    if base.index(a[0]) %2 == 0:
        start = base.index(a[0])
    else:
        start = base.index(a[1])
    
    result.append(base[start])
    result.append(base[start+1])
    
    
    while len(result) != len(base):
        for i in range(0,len(base),2):
            if result[-1] == base[i]:
                result.append(base[i])
                result.append(base[i+1])

    result = ' '.join(list(map(str,result)))
    print('#{} {}'.format(case+1,result))