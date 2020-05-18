dx = [0,0,-1,1]
dy = [1,-1,0,0]

def check_atom(i,j):
    if info[i][0]==0:
        if info[j][0]==1:
            if element[i][0]==element[j][0] and element[i][1] < element[j][1]:
                return 2
        elif info[j][0] in [2,3]:
            if element[i][1] < element[j][1]:
                return 1
    elif info[i][0]==1:
        if info[j][0]==0:
            if element[i][0]==element[j][0] and element[i][1] > element[j][1]:
                return 2
        elif info[j][0] in [2,3]:
            if element[i][1] < element[j][1]:
                return 1
    elif info[i][0]==2:
        if info[j][0]==3:
            if element[i][1]==element[j][1] and element[i][0] > element[j][0]:
                return 2
        elif info[j][0] in [0,1]:
            if element[i][0] > element[j][0]:
                return 1
    else:
        if info[j][0]==2:
            if element[i][1]==element[j][1] and element[i][0] < element[j][0]:
                return 2
        elif info[j][0] in [0,1]:
            if element[i][0] < element[j][0]:
                return 1
    return 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    element = []
    info = []
    result = 0
    for _ in range(N):
        x,y,d,e = map(int,input().split())
        element.append([x*2,y*2])
        info.append([d,e])

    cnt = 0
    flag=1
    while len(element)>1:
        temp_e = []
        temp_i = []
        temp_l = []
        for i in range(len(element)-1):
            for j in range(i+1,len(element)):
                flag = check_atom(i,j)
                if flag==2:
                    if element[i] not in temp_e:
                        temp_e.append(element[i])
                        temp_i.append(info[i])
                        temp_l.append(abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][i]))
                    if element[j] not in temp_e:
                        temp_e.append(element[j])
                        temp_i.append(info[j])
                        temp_l.append(abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][i]))
                    if element[i] in temp_e:
                        idx = temp_e.index(element[i])
                        if temp_l[idx]>abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][i]):
                            temp_l[idx]=abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][i])
                    if element[j] in temp_e:
                        idx = temp_e.index(element[j])
                        if temp_l[idx]>abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][i]):
                            temp_l[idx]=abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][i])
                elif flag==1:
                    if element[i] not in temp_e:
                        temp_e.append(element[i])
                        temp_i.append(info[i])
                        temp_l.append((abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][i]))//2)
                    if element[j] not in temp_e:
                        temp_e.append(element[j])
                        temp_i.append(info[j])
                        temp_l.append((abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][i]))//2)
                    if element[i] in temp_e:
                        idx = temp_e.index(element[i])
                        if temp_l[idx]>(abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][i]))//2:
                            temp_l[idx]=(abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][i]))//2
                    if element[j] in temp_e:
                        idx = temp_e.index(element[j])
                        if temp_l[idx]>(abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][i]))//2:
                            temp_l[idx]=(abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][i]))//2
        extinction = min(temp_l)
        for i in range(len(temp_l)-1,-1,-1):
            if temp_l[i]==extinction:
                result+=temp_i[i][1]
                temp_e.pop(i)
                temp_i.pop(i)
                temp_l.pop(i)
        element = temp_e
        info = temp_i

    print('#{} {}'.format(tc,result))