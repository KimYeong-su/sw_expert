# dx = [0,0,-1,1]
# dy = [1,-1,0,0]

def check_atom(i,j):
    if info[i][0]==0:
        if info[j][0]==1:
            if element[i][0]==element[j][0] and element[i][1] < element[j][1]:
                return 2
        elif info[j][0]==2:
            if element[i][1] < element[j][1] and element[i][0] < element[j][0] and abs(element[i][1]-element[j][1])==abs(element[i][0]-element[j][0]):
                return 1
        elif info[j][0]==3:
            if element[i][1] < element[j][1] and element[i][0] > element[j][0] and abs(element[i][1]-element[j][1])==abs(element[i][0]-element[j][0]):
                return 1
    elif info[i][0]==1:
        if info[j][0]==0:
            if element[i][0]==element[j][0] and element[i][1] > element[j][1]:
                return 2
        elif info[j][0]==2:
            if element[i][1] > element[j][1] and element[i][0] < element[j][0] and abs(element[i][1]-element[j][1])==abs(element[i][0]-element[j][0]):
                return 1
        elif info[j][0]==3:
            if element[i][1] > element[j][1] and element[i][0] > element[j][0] and abs(element[i][1]-element[j][1])==abs(element[i][0]-element[j][0]):
                return 1
    elif info[i][0]==2:
        if info[j][0]==3:
            if element[i][1]==element[j][1] and element[i][0] > element[j][0]:
                return 2
        elif info[j][0]==0:
            if element[i][0] > element[j][0] and element[i][1] > element[j][1] and abs(element[i][1]-element[j][1])==abs(element[i][0]-element[j][0]):
                return 1
        elif info[j][0]==1:
            if element[i][0] > element[j][0] and element[i][1] < element[j][1] and abs(element[i][1]-element[j][1])==abs(element[i][0]-element[j][0]):
                return 1
    else:
        if info[j][0]==2:
            if element[i][1]==element[j][1] and element[i][0] < element[j][0]:
                return 2
        elif info[j][0]==0:
            if element[i][0] < element[j][0] and element[i][1] > element[j][1] and abs(element[i][1]-element[j][1])==abs(element[i][0]-element[j][0]):
                return 1
        elif info[j][0]==1:
            if element[i][0] < element[j][0] and element[i][1] < element[j][1] and abs(element[i][1]-element[j][1])==abs(element[i][0]-element[j][0]):
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
                        temp_l.append((abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][1]))//2)
                    else:
                        idx = temp_e.index(element[i])
                        if temp_l[idx]>(abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][1]))//2:
                            temp_l[idx]=(abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][1]))//2
                    if element[j] not in temp_e:
                        temp_e.append(element[j])
                        temp_i.append(info[j])
                        temp_l.append((abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][1]))//2)
                    else:
                        idx = temp_e.index(element[j])
                        if temp_l[idx]>(abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][1]))//2:
                            temp_l[idx]=(abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][1]))//2
                elif flag==1:
                    if element[i] not in temp_e:
                        temp_e.append(element[i])
                        temp_i.append(info[i])
                        temp_l.append((abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][1]))//2)
                    else:
                        idx = temp_e.index(element[i])
                        if temp_l[idx]>(abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][1]))//2:
                            temp_l[idx]=(abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][1]))//2
                    if element[j] not in temp_e:
                        temp_e.append(element[j])
                        temp_i.append(info[j])
                        temp_l.append((abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][1]))//2)
                    else:
                        idx = temp_e.index(element[j])
                        if temp_l[idx]>(abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][1]))//2:
                            temp_l[idx]=(abs(element[i][0]-element[j][0])+abs(element[i][1]-element[j][1]))//2
        if len(temp_l)==0:
            break
        extinction = min(temp_l)
        for i in range(len(temp_l)-1,-1,-1):
            if temp_l[i]==extinction:
                idx = element.index(temp_e[i])
                result+=temp_i[i][1]
                element.pop(idx)
                info.pop(idx)

    print('#{} {}'.format(tc,result))