def best(top,money):
    global minimum
    if top == 12:
        if minimum>money:
            minimum = money
        return

    best(top+1,money + plan[top]*d)
    best(top+1,money + m)
    if top<10:
        best(top+3,money+tm)
    best(12,y)
    

T = int(input())

for tc in range(1,T+1):
    d, m, tm, y = map(int,input().split())

    plan = list(map(int,input().split()))
    # plan.append(0)

    minimum = 10000
    best(0,0)
    print('#{} {}'.format(tc,minimum))