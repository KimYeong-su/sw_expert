cases = int(input())

for case in range(cases):
    n = int(input())
    base = list(map(int,input().split()))
    mul = []
    for i in range(len(base)-1):
        for j in range(i+1,len(base)):
            temp = list(str(base[i]*base[j]))
            for k in range(len(temp)-1):
                if temp[k]>temp[k+1]:
                    break
                elif k+1 == len(temp)-1:
                    mul.append(base[i]*base[j])
    if mul == []:
        print('#{} -1'.format(case+1))
    else:
        print('#{} {}'.format(case+1,max(mul)))