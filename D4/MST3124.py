'''
# 크루스칼 알고리즘
def find(i):
    global P
    if P[i] != i:
        P[i] = find(P[i])
    return P[i]

def check():
    global P
    cnt = 0
    num = 0
    P={}
    rank={}
    for i in range(V+1):
        P[i] = i
        rank[i] = 0
    for i in range(E):
        s,e=base[i][0]
        w = base[i][1]
        x = find(s)
        y = find(e)
        if x!=y:
            if rank[x]>rank[y]:
                P[y] = x
            else:
                P[x] = y
                if rank[x] == rank[y]:
                    rank[y] += 1
            cnt+=w
            num+=1
        # print(P)
        if num==V-1:
            return cnt
    
T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    base = {}
    for _ in range(E):
        s, e, w = map(int,input().split())
        base[(s,e)] = w
    base = sorted(base.items(), key=lambda x : x[1])
    # print(base)
    result = check()
    print('#{} {}'.format(tc,result))
'''