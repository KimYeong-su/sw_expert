cases = 10

for case in range(cases):
    base= list(map(str, input().split()))
    #base = list(input(num))
    base_num = list(base[1])
    # print(base_num)
    c = 0
    while c==0:
        for i in range(len(base_num)-1):
            # print(len(base_num))
            if base_num[i] == base_num[i+1]:
                # print(i)
                del base_num[i]
                del base_num[i]
                # print(base_num)
                c=0
                break
            else:
                c=1
    result = ''.join(base_num)
    print(f'#{case+1} {result}')