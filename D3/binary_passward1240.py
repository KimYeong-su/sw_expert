cases = int(input())
for case in range(cases):
    a, b = map(int, input().split())
    base = []
    dic = {'0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}
    for i in range(a):
        temp = list(map(int,input()))
        if 1 in temp:
            base.append(temp)

    for i in range(0,len(base[0]),-1):
        if base[0][i]== 1:
            break

    temp2 = []
    for j in range(len(base[0])):
        if base[0][j] == 1:
            temp2.append(j)

    i = temp2[-1]-55
    n = 8
    result = []
    while n>0:
        # print(base[0][i:i+7])
        temp = ''.join(map(str,base[0][i:i+7]))
        if temp in dic:
            result.append(dic[temp])
            i += 7
            n -= 1
        else:
            result = [0 for _ in range(8)]
            break


    add = 0
    for k in range(len(result)-1):
        if k%2==0:
            add += result[k]*3
        else:
            add += result[k]

    add += result[-1]
    v = 0
    if add%10==0:
        for i in result:
            v += i
            
    print(f'#{case+1} {v}')