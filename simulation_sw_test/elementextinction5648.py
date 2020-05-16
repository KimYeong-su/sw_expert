dx = [0,0,-1,1]
dy = [1-1,0,0]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    element = []
    info = []
    result = 0
    for _ in range(N):
        x,y,d,e = map(float,input().split())
        element.append([x*2,y*2])
        info.append([d,e])
    
    while len(element)>1:
        while True:
            temp = []
            for i in range(len(element)):
                nx = element[i][0] + dx[info[i][0]]
                ny = element[i][1] + dy[info[i][0]]
                if [nx,ny] not in temp:
                    temp.append([nx,ny])
                else:
                    


