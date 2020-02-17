def rotation(arr):
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[N-j-1][i]
    return arr

T=10

for tc in range(1,T+1):
    N=int(input())
    base=[list(map(int,input().split())) for _ in range(N)]
    base2 = [[0 for _ in range(N)]for _ in range(N)]
    for i in range(N):
        for j in range(N):
            base2[i][j] = base[N-j-1][i]
    
    # for row in base2:
    #     print(row)
    # print()
    
    cnt=0
    for i in range(N):
        for j in range(N):
            if base2[i][j]==2:
                temp = j
                while temp<N-1:
                    temp += 1
                    if base2[i][temp]==1:
                        base2[i][j]=0
                        base2[i][temp]=0
                        cnt+=1
                        break
                    elif base2[i][temp]==2:
                        base2[i][j]=0
                        break



        # for row in base2:
        #     print(row)
        # print(cnt)
    print('#{} {}'.format(tc,cnt))