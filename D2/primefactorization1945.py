cases = int(input())

for case in range(cases):
    w_num = int(input())
    result = []

    for i in range(w_num):
        word, number = map(str, input().split())
        for k in range(int(number)):
            result.append(word)
            
    print(f'#{case+1}')
    if len(result)%10==0:
        for j in range(1,(len(result)//10)+1):
            print(''.join(result[10*(j-1):10*j]))
    else:
        for j in range(1,(len(result)//10)+1):
            print(''.join(result[10*(j-1):10*j]))
        print(''.join(result[10*j:]))