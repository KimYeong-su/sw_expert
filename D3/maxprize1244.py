cases = int(input())

for case in range(cases):
    num, c = map(str,input().split())
    init = list(map(int,num))
    setup = list(sorted(init,reverse=True))
    # print(setup)
    
    c = int(c)
    i = 0
    while c > 0:
        if init[i] != setup[i]:
            for j in range(-1,-len(init)-1,-1):
                if init[j] == setup[i]:
                    init[i], init[len(init)+j] = init[len(init)+j], init[i]
                    c -= 1
                    if i<len(init)-1:
                        i += 1
        else:
            if i<len(init)-1:
                i += 1
            else:
                init[len(init)-1], init[len(init)-2] = init[len(init)-2], init[len(init)-1]

    print(init)