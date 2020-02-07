T = int(input())

for tc in range(1,T+1):
    ans = list(map(int,input()))
    base = [0 for _ in range(len(ans))]

    f=1
    cnt = 0
    i = 0
    while ans != base:
        if f==1:
            if ans[i] ==1:
                for a in range(i,len(base)):
                    base[a]=1
                cnt+=1
                f=0
            i+=1
        else:
            if ans[i] ==0:
                for a in range(i,len(base)):
                    base[a]=0
                cnt+=1
                f=1
            i+=1
    
    print('#{} {}'.format(tc,cnt))