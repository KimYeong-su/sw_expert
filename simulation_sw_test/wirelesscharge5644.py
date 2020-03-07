dx = [0,-1,0,1,0]
dy = [0,0,1,0,-1]

T = int(input())

for tc in range(1,T+1):
    M, A = map(int,input().split())
    moving = [list(map(int,input().split()))for _ in range(2)]

    AP =[]
    for _ in range(A):
        AP.append(tuple(map(int,input().split())))

    time=0
    A_row, A_col = 1,1
    B_row, B_col = 10,10
    result = 0
    while time<M+1:
        temp_a=[]
        temp_b=[]
        for i in range(A):
            col, row, d, p = AP[i]
            if abs(col-A_col)+abs(row-A_row)<=d:
                temp_a += [i]
            if abs(col-B_col)+abs(row-B_row)<=d:
                temp_b += [i]
        temp = 0
        if len(temp_a)>0 and len(temp_b)>0:
            for i in temp_a:
                for j in temp_b:
                    if i==j and temp < AP[i][3]:
                        temp = AP[i][3]
                    elif i!=j:
                        if temp < AP[i][3]+AP[j][3]:
                            temp = AP[i][3]+AP[j][3]
        elif len(temp_a)>0:
            for i in temp_a:
                if temp < AP[i][3]:
                    temp = AP[i][3]
        elif len(temp_b)>0:
            for i in temp_b:
                if temp < AP[i][3]:
                    temp = AP[i][3]
        if time<M:
            A_row, A_col = A_row + dx[moving[0][time]], A_col + dy[moving[0][time]]
            B_row, B_col = B_row + dx[moving[1][time]], B_col + dy[moving[1][time]]
        # print(temp)
        result += temp
        time +=1

    print('#{} {}'.format(tc,result))