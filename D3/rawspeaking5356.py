cases = int(input())

for case in range(cases):
    base = []
    for _ in range(5):
        temp=list(input())
        base.append(temp)

    for i in range(len(base)):
        if i == 0:
            maximum = len(base[i])
        else:
            if maximum<len(base[i]):
                maximum = len(base[i])

    for i in base:
        if len(i) != maximum:
            i += ' '*(maximum-len(i))
    result = []
    for i in range(maximum):
        for j in range(len(base)):
            result.append(base[j][i])
    
    s = ''.join(result)
    s = s.replace(' ','')
    print('#{} {}'.format(case+1,s))