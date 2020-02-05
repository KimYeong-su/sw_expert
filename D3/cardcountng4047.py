cases = int(input())

for case in range(cases):
    card = list(input())
    t=0
    he = []
    dia = []
    sp = []
    clo = []
    for i in range(0,len(card),3):
        num = ''.join(card[i+1:i+3])
        if card[i]=='H':
            if num in he:
                t=1
                break
            he.append(num)
        elif card[i]=='D':
            if num in dia:
                t=1
                break
            dia.append(num)
        elif card[i]=='S':
            if num in sp:
                t=1
                break
            sp.append(num)
        else:
            if num in clo:
                t=1
                break
            clo.append(num)

    if t==1:
        print('#{} ERROR'.format(case+1))
    else:
        print('#{} {} {} {} {}'.format(case+1,13-len(sp),13-len(dia),13-len(he),13-len(clo)))