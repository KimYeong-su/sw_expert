
# 크루스칼 알고리즘
def find(i):
    global P
    if P[i] != i:
        P[i] = find(P[i])
    return P[i]

def check():
    global P
    cnt = 0 # 가중치 더해가기
    num = 0 # 간선 갯수
    P={} # key값(최대 부모(root))
    rank={} # 덩어리 덩어리 이어질때
    for i in range(V):
        P[i] = i
        rank[i] = 0
    for i in range(E):
        s,e,w=base[i]
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
        if num>=V-1:
            return cnt
    
T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    base = []
    for _ in range(E):
        s, e, w = map(int,input().split())
        base.append((s-1,e-1,w))
    base = sorted(base, key=lambda x : x[2])
    # print(base)
    result = check()
    print('#{} {}'.format(tc,result))