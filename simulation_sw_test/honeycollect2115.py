def collect(case):
    index = [x for x in range(M)]
    cnt = 0
    for i in range(1<<len(index)):
        temp = 0
        temp1= 0
        for j in range(len(index)+1):
            if i & (1<<j):
                temp += base[case[0]][case[1]+j]
                temp1 += base[case[0]][case[1]+j]**2 
                if temp>C:
                    break
        if cnt<temp1 and j==len(index):
            cnt = temp1
    return cnt
    

T = int(input())

for tc in range(1,T+1):
    N,M,C = map(int,input().split())
    base = [list(map(int,input().split()))for _ in range(N)]
    case = []
    maximum = 0
    for i in range(N):
        for j in range(N-M+1):
            case.append((i,j))
    for i in range(len(case)):
        for j in range(i+1,len(case)):
            temp = 0
            if case[i][0]==case[j][0]:
                if case[i][1]+M<=case[j][1]:
                    temp += collect(case[i])
                    temp += collect(case[j])
            else:
                temp += collect(case[i])
                temp += collect(case[j])
            if temp>maximum:
                maximum=temp
    print('#{} {}'.format(tc,maximum))