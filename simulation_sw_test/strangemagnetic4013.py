T = int(input())
for tc in range(1,T+1):
    K = int(input())

    # 자석의 빨간화살표의 인덱스는 0이고 오른쪽 방향으로 +1씩 증가
    magnetics = [list(map(int,input().split()))for _ in range(4)]
    result = 0
    for _ in range(K):
        num_mag,direction = map(int,input().split())
        temp = [0,0,0,0]
        temp[num_mag-1]=1
        i=num_mag
        while i<4:
            if magnetics[i-1][2]!=magnetics[i][6]:
                temp[i]=1
            else:
                break
            i+=1
        i=num_mag
        while i>1:
            if magnetics[i-2][2]!=magnetics[i-1][6]:
                temp[i-2]=1
            else:
                break
            i-=1
        for i in range(4):
            if temp[i]==1:
                if i%2==(num_mag-1)%2:
                    if direction==-1:
                        magnetics[i] = magnetics[i][1:]+[magnetics[i][0]]
                    else:
                        magnetics[i] = [magnetics[i][7]]+magnetics[i][:7]
                else:
                    if direction==1:
                        magnetics[i] = magnetics[i][1:]+[magnetics[i][0]]
                    else:
                        magnetics[i] = [magnetics[i][7]]+magnetics[i][:7]
    for i in range(4):        
        if magnetics[i][0]==1:
            result += 2**i
    print('#{} {}'.format(tc,result))    
