cases = 10

for case in range(cases):

    base_n = int(input())
    base = list(map(str,input().split()))
    c = int(input())

    insert = list(map(str,input().split()))
    i = 1
    while c>0:
        k = i + int(insert[i+1])+2
        if c == 1:
            temp = insert[i:]
        else:
            temp = insert[i:k]
        
        index = int(temp[0])
        if index<10:
            base = base[:index] + temp[2:] + base[index:]
        base = base[:10]
        i = k + 1
        c -= 1

    result = ' '.join(map(str,base))
    print(f'#{case+1} {result}')