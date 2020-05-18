# 다시 짜보자(Hint : 모르겠으면 문자열, 딕셔너리 이용하자..)
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def check_atom(i,j):
    if info[i][0]==0:
        if info[j][0]==1:
            if element[i][0]==element[j][0] and element[i][1] < element[j][1]:
                return 1
        elif info[j][0] in [2,3]:
            if element[i][1] < element[j][1]:
                return 1
    elif info[i][0]==1:
        if info[j][0]==0:
            if element[i][0]==element[j][0] and element[i][1] > element[j][1]:
                return 1
        elif info[j][0] in [2,3]:
            if element[i][1] < element[j][1]:
                return 1
    elif info[i][0]==2:
        if info[j][0]==3:
            if element[i][1]==element[j][1] and element[i][0] > element[j][0]:
                return 1
        elif info[j][0] in [0,1]:
            if element[i][0] > element[j][0]:
                return 1
    else:
        if info[j][0]==2:
            if element[i][1]==element[j][1] and element[i][0] < element[j][0]:
                return 1
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
    while cnt<2001 and flag==1:
        for i in range(len(element)-1):
            for j in range(i+1,len(element)):
                flag = check_atom(i,j)
                if flag==1:
                    break
            if flag==1:
                break
        temp = []
        temp_info = []
        distroy = []
        for i in range(len(element)):
            nx = element[i][0]+dx[info[i][0]]
            ny = element[i][1]+dy[info[i][0]]
            if [nx,ny] not in temp:
                temp.append([nx,ny])
                temp_info.append(info[i])
            else:
                if [nx,ny] not in distroy:
                    distroy.append([nx,ny])
                result += info[i][1]
        if distroy!=[]:
            for i in range(len(distroy)):
                idx = temp.index(distroy[i])
                temp.pop(idx)
                d,e = temp_info.pop(idx)
                result += e
        element = temp
        info = temp_info
        cnt += 1
    print('#{} {}'.format(tc,result))