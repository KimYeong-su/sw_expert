di = [0,0,1,-1]
dj = [1,-1,0,0]

def deepcopy(base, h, w):
    tmp = []
    for i in range(h):
        tmp1 = []
        for j in range(w):
            tmp1.append(base[i][j])
        tmp.append(tmp1)
    return tmp

def dfs(base, num):
    global minV
    if num == N:
        tmp = H * W
        for i in range(H):
            tmp -= base[i].count(0)
        if tmp < minV:
            minV = tmp
            # for i in range(H):
            #     print(base[i])
            # print()
        return
    for c in range(W):
        c_base = deepcopy(base, H, W)
        answer = bb(c_base, c)
        dfs(answer, num+1)


def bb(base, col):
    queue = []
    for i in range(H):
        if base[i][col]:
            queue.append((i,col))
            break
    else:
        return base
    while queue:
        i, j = queue.pop(0)
        for c in range(base[i][j]):
            if c == 0:
                base[i][j] = 0
            else:
                for a in range(4):
                    ni = i + di[a] * c
                    nj = j + dj[a] * c
                    if 0 <= ni < H and 0 <= nj < W:
                        if base[ni][nj] == 1:
                            base[ni][nj] = 0
                        elif base[ni][nj] > 1:
                            queue.append((ni, nj))

    tmp = [[0]*H for _ in range(W)]
    for i in range(H):
        for j in range(W):
            tmp[W-j-1][i] = base[i][j]
    tmp2 = []
    for i in range(W):
        tmp1 = []
        for j in tmp[i]:
            if j:
                tmp1.append(j)
        else:
            while len(tmp1) != H:
                tmp1.insert(0,0)
        tmp2.append(tmp1)
    tmp = [[0]*W for _ in range(H)]
    for i in range(W):
        for j in range(H):
            tmp[j][W-i-1] = tmp2[i][j]
    return tmp

T = int(input())
for tc in range(1,T+1):
    N,W,H = map(int,input().split())
    org = [list(map(int,input().split()))for _ in range(H)]
    minV = float('inf')
    dfs(org, 0)
    print('#{} {}'.format(tc,minV))