def check(number,cnt):
    global result
    if cnt==0:
        temp = int(''.join(number))
        if result<temp:
            result = temp
        return
    for i in range(len(number)-1):
        for j in range(i+1,len(number)):
            number[i],number[j]=number[j],number[i]
            temp1 = int(''.join(number))
            if temp1 not in history[cnt]:
                history[cnt].append(temp1)
                check(number,cnt-1)
            number[i],number[j]=number[j],number[i]

T = int(input())
for tc in range(1,T+1):
    init,n = map(str,input().split())
    history=[[] for _ in range(int(n)+1)]
    result=0
    init = list(init)
    check(init,int(n))
    print('#{} {}'.format(tc,result))