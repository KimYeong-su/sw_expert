def money_count(money, scale, counting):
    counting = 0
    while money - scale >= 0:
        if money >= scale:
            counting += 1
            money -= scale
    return money, counting

cases = int(input())

for case in range(cases):
    money = int(input())
    a,b,c,d,e,f,g,h = 0, 0, 0, 0, 0, 0, 0, 0
    money,a = money_count(money,50000,a)
    money,b = money_count(money,10000,b)
    money,c = money_count(money,5000,c)
    money,d = money_count(money,1000,d)
    money,e = money_count(money,500,e)
    money,f = money_count(money,100,f)
    money,g = money_count(money,50,g)
    money,h = money_count(money,10,h)

    print(f'#{case+1}')
    print(a,b,c,d,e,f,g,h)