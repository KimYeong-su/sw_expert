cases = 10

for case in range(cases):

    base_n = int(input())
    base = list(map(str,input().split()))
    c = int(input())

    insert = list(map(str,input().split()))
    i = 0
    while c>0:
        if insert[i] == 'I':
            k = i + int(insert[i+2])+3
        else:
            k = i + 3

        if c == 1:
            temp = insert[i:]
        else:
            temp = insert[i:k]

        index = int(temp[1])
        d_index = int(temp[2])

        if temp[0] == 'I':
            base = base[:index] + temp[3:] + base[index:]
        else:
            base = base[:index] + base[index + d_index:]
        
        i = k
        c -= 1

    result = ' '.join(map(str,base[:10]))
    print(f'#{case+1} {result}')