# T = int(input())

# for tc in range(1,T+1):
#     N,M = map(int,input().split())
#     relation = {}
#     count = [x for x in range(1,N+1)]
#     for i in range(1,N+1):
#         relation[i]=[]
#     for _ in range(M):
#         a,b = map(int,input().split())
#         relation[a] += [b]
#         relation[b] += [a]
#     result = set()
#     if len(relation[1]):
#         for i in relation[1]:
#             if i!=1:
#                 result.add(i)
#                 for j in relation[i]:
#                     if j!=1:
#                         result.add(j)
#     result = len(list(result))
#     print('#{} {}'.format(tc,result))


def find(cur, start):
    global cnt
    queue = [start]
    # print(queue)
    v=set()
    v.add(1)
    while True:
        temp = []
        while queue:
            friend = queue.pop(0)
            for f in friend:
                v.add(f)
                temp.append(bin[f])
        queue=temp
        cur +=1
        if cur>2:
            return len(list(v))-1

T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    bin = {i:[] for i in range(N+1)}
    for _ in range(M):
        a,b = map(int,input().split())
        bin[a]+=[b]
        bin[b]+=[a]
    # print(bin)
    cnt = find(1,bin[1])
    print('#{} {}'.format(tc,cnt))