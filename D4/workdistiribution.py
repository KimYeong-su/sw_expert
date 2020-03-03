def work(arr,a,temp,row,col,list):
    global maximum
    if a==len(list):
        result = 1
        for pro in temp:
            result *= pro
        if maximum < result:
            maximum = result
        return
    else:
        for i in range(N):
            for j in range(N):
                if arr[i][j] == list[a] and row[i]==0 and col[j]==0:
                    row[i], col[j], temp[i] = 1,1,list[a]
                    for p in range(len(list)):
                        work(arr,p,temp,row,col,list)
                        work(arr,p+1,temp,row,col,list)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    base=[list(map(int,input().split()))for _ in range(N)]
    sorting = []
    for i in range(N):
        for j in range(N):
            sorting.append(base[i][j])
    sorting = list(sorted(set(sorting),reverse=True))
    pro=[0 for _ in range(N)]
    v_row = [0 for _ in range(N)]
    v_col = [0 for _ in range(N)]
    maximum = 0
    for i in range(len(sorting)):
        work(base,i,pro,v_row,v_col,sorting)
    answer = str(round(maximum/100**(N-1),6))
    index = answer.index('.')
    while len(answer[index+1:])!=6:
        answer += '0'
    print('#{} {}'.format(tc,answer))