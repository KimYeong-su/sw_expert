def row_search(base):
    num = 1
    while num<10:
        for p in range(9):
            if num in base[p][:]:
                continue
            else:
                return 0
        num += 1
    return 1

def colume_search(base):
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(base[j][i])
        num = 1
        while num<10:
            if num in temp:
                num += 1
            else:
                return 0
    return 1

def square_search(base):
    for j in range(0,9,3):
        for l in range(0,9,3):        
            temp = []
            for i in range(3):
                for k in range(3):
                    temp.append(base[j+i][l+k])
            num = 1
            while num<10:
                if num in temp:
                    num += 1
                else:
                    return 0
    return 1


cases = int(input())

for case in range(cases):
    base = []
    for i in range(9):
        temp = []
        for j in map(int, input().split()):
            temp.append(j)
        base.append(temp)
    # print(f'#{case+1}')
    # print(row_search(base))
    # print(colume_search(base))
    # print(square_search(base))

    if row_search(base)==1 and colume_search(base)==1 and square_search(base)==1:
        print(f'#{case+1} 1')
    else:
        print(f'#{case+1} 0')