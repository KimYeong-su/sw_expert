# def work(arr,a,b,temp,row,col):
#     global maximum
#     if b==N:
#         result = 1
#         for pro in temp:
#             result *= pro
#         if maximum < result:
#             maximum = result
#         return
#     else:
#         row[a]=1
#         temp *= arr[a][b]
#         for j in range(N):
#             if row[j]==0:
#                 if temp*arr[j][b+1]>=temp:
#                     work(arr,j,b+1,temp,row,col)

# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     base=[list(map(float,input().split()))for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             base[i][j] /= 100 
#     v_row = [0 for _ in range(N)]
#     v_col = [0 for _ in range(N)]
#     maximum = 0
#     for i in range(N):
#         work(base,i,0,1,v_row,v_col)
#     answer = str(round(maximum/100**(N-1),6))
#     index = answer.index('.')
#     while len(answer[index+1:])!=6:
#         answer += '0'
#     print('#{} {}'.format(tc,answer))

def work(arr,i,temp,result):
    global maximum
    if maximum >= result:
        return
    if i == N:
        if maximum < result:
            maximum = result
            # print(maximum)
        return
    else:
        for p in range(N):
            if temp[p]==0:
                temp[p]=1
                # if i ==0:
                #     work(arr,i+1,temp,arr[i][p])
                # else:
                work(arr,i+1,temp,result*arr[i][p])
                temp[p]=0


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    base=[list(map(float,input().split()))for _ in range(N)]
    for i in range(N):
        for j in range(N):
            base[i][j] /= 100
    temp=[0 for _ in range(N)]
    maximum = 0
    work(base,0,temp,1)
    answer = str(round(maximum*100,6))
    index = answer.index('.')
    while len(answer[index+1:])!=6:
        answer += '0'
    print('#{} {}'.format(tc,answer))