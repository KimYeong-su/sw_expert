T = int(input())

for tc in range(1,T+1):
    base = list(map(int,input().split()))
    n = len(base)
    add = []
    for i in range(1<<n):
        temp = []
        temp2 = 0
        for j in range(n+1):
            if i&(1<<j):
                temp.append(base[j])
        if len(temp) == 3:
            for k in temp:
                temp2 += k
        add.append(temp2)
    add = list(set(add))
    result = list(sorted(add,reverse=True))
    print('#{} {}'.format(tc,result[4]))
