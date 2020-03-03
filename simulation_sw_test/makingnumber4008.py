def f(a,add,sub,mul,div,result):
    global maximum, minimum
    if a==N:
        if result>maximum:
            maximum = result
        if result<minimum:
            minimum = result
        return
    else:
        if add:
            add -= 1
            f(a+1,add, sub, mul, div,result+numbers[a])
            add += 1
        if sub:
            sub -= 1
            f(a+1,add, sub, mul, div,result-numbers[a])
            sub += 1
        if mul:
            mul -= 1
            f(a+1,add, sub, mul, div,result*numbers[a])
            mul += 1
        if div:
            div -= 1
            f(a+1,add, sub, mul, div,int(result/numbers[a]))
            div += 1

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    oper_count = list(map(int,input().split()))

    numbers = list(map(int,input().split()))
    maximum = -1000000000
    minimum = 1000000000
    f(1,oper_count[0],oper_count[1],oper_count[2],oper_count[3],numbers[0])
    print('#{} {}'.format(tc,maximum-minimum))