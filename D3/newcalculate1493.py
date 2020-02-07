def SARP(x,y):
    sum = 0
    for i in range(1,x+1):
        sum += i
    for j in range(x,x+y-1):
        sum += j
    return sum

def And(n):
    for x in range(1,150):
        if x*(x+1)//2 < n < (x+1)*(x+2)//2:
            a = n-x*(x+1)//2
            b = -a+x+2
            break
        elif x*(x+1)//2 == n:
            a=x
            b=1
            break
    return a,b


T = int(input())

for tc in range(1,T+1):
    p, q = map(int,input().split())

    x1, y1 = And(p)
    x2, y2 = And(q)
    x1 += x2
    y1 += y2
    result = SARP(x1,y1)

    print('#{} {}'.format(tc,result))