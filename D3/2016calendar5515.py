T = int(input())
for tc in range(1,T+1):
    dic = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30}
    m, d = map(int,input().split())

    day = 31
    for i in range(1,m+1):
        if i-1 == 0:
            day -= 31
        else:
            day += dic[i-1]
    day += d
    print('#{} {}'.format(tc,(day+3)%7))