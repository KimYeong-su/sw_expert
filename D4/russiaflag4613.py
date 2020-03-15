T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    base = [list(input()) for _ in range(N)]

    result=2500
    for i in range(N-2):
        temp1 = (i+1)*M
        for a in range(i+1):
            temp1 -= base[a].count('W')
        for j in range(i+1,N-1):
            temp2 = (j-i)*M
            for b in range(i+1,j+1):
                temp2 -= base[b].count('B')
            temp3 = (N-j-1)*M
            for k in range(j+1,N):
                temp3 -= base[k].count('R')
            if temp1+temp2+temp3 < result:
                result = temp1+temp2+temp3

    print('#{} {}'.format(tc,result))