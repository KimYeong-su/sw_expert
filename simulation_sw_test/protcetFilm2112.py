def check(N,M):
    temp=[0 for _ in range(M)]
    for j in range(M):
        cnt=0
        flag=0
        for i in range(N):
            if i == 0:
                flag=base[i][j]
                cnt=1
            else:
                if base[i][j]!=flag:
                    flag=base[i][j]
                    cnt=1
                else:
                    cnt+=1
            if cnt==K:
                temp[j]=1
                break
        if temp[j]==0:
            break
    if 0 in temp:
        return 0
    else:
        return 1
    
def change(arr,s,result):
    global minimum
    if s==result:
        flag = check(D,W)
        if flag==1:
            minimum=result
        return
    else:
        temp_a = [0 for _ in range(W)]
        temp_b = [1 for _ in range(W)]
        index = arr[s]
        for i in range(W):
            temp_a[i], base[index][i] = base[index][i], temp_a[i]
        change(arr,s+1,result)
        for i in range(W):
            temp_a[i], base[index][i] = base[index][i], temp_a[i]
            temp_b[i], base[index][i] = base[index][i], temp_b[i]
        change(arr,s+1,result)
        for i in range(W):
            temp_b[i], base[index][i] = base[index][i], temp_b[i]

T = int(input())
for tc in range(1,T+1):
    D,W,K = map(int,input().split())
    base = [list(map(int,input().split()))for _ in range(D)]
    case_count = [[] for _ in range(K+1)]

    for i in range(1<<D):
        temp = []
        for j in range(D+1):
            if i & (1<<j):
                temp.append(j)
        if len(temp)<=K:
            case_count[len(temp)]+=[temp]

    case = []
    for i in case_count:
        case += i    
    minimum = 100000
    if K==1:
        minimum=0
    else:
        while minimum==100000:
            temp=case.pop(0)
            result = len(temp)
            change(temp,0,result)
    print('#{} {}'.format(tc,minimum))