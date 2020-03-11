T = int(input())

for tc in range(1,T+1):
    case = input()
    pipe = []
    result = 0
    for i in range(len(case)-1):
        if case[i:i+2] == '((':
            pipe.append(1)
        elif case[i:i+2] == '()':
            for j in range(len(pipe)):
                pipe[j]+=1
        elif case[i:i+2] == '))':
            result += pipe.pop()

    print('#{} {}'.format(tc,result))
    