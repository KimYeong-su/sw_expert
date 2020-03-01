T = int(input())

for tc in range(1,T+1):
    N = int(input())

    base = []
    while len(base)!=N:
        base += list(map(int,input().split()))

    result = 0
    val = '0'
    flag = 0
    while flag!=1:
        l = len(val)
        for i in range(len(base)-l+1):
            temp = ''.join(map(str,base[i:i+l]))
            if val == temp:
                val = str(int(val)+1)
                break
            else:
                if i ==len(base)-l:
                    flag = 1
    result = val
    print('#{} {}'.format(tc,result))