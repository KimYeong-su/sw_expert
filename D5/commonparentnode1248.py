T = int(input())
for tc in range(1,T+1):
    V, E, n1, n2 = map(int,input().split())
    edges = list(map(int,input().split()))
    tree_down = {}
    tree_up = {}
    for _ in range(E):
        s = edges.pop(0)
        e = edges.pop(0)
        if s not in tree_down:
            tree_down[s] = [e]
        else:
            tree_down[s] += [e]
        tree_up[e] = s
    temp1 = []
    temp2 = []
    while True:
        if n1 in tree_up.keys():
            n1 = tree_up[n1]
            temp1.append(n1)
        if n2 in tree_up.keys():
            n2 = tree_up[n2]
            temp2.append(n2)
        if n1 in temp2:
            root=n1
            break
        if n2 in temp1:
            root=n2
            break
    # print(n1)
    queue = [root]
    result = 1
    while len(queue)!=0:
        n=queue.pop(0)
        if n in tree_down.keys():
            for i in tree_down[n]:
                queue.append(i)
                result += 1
    print('#{} {} {}'.format(tc,root,result))