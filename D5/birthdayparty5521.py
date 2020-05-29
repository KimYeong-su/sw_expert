T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    relation = {}
    count = [x for x in range(1,N+1)]
    for i in range(1,N+1):
        relation[i]=[]
    for _ in range(M):
        a,b = map(int,input().split())
        relation[a] += [b]
        relation[b] += [a]
    result = set()
    if len(relation[1]):
        for i in relation[1]:
            if i!=1:
                result.add(i)
                for j in relation[i]:
                    if j!=1:
                        result.add(j)
    result = len(list(result))
    print('#{} {}'.format(tc,result))