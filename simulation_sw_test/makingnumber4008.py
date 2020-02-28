def cal(oper,num1,num2):
    if oper == 0:
        return num1+num2
    elif oper == 1:
        return num1-num2
    elif oper == 2:
        return num1*num2
    else:
        if num1 < 0:
            return num1//num2+1
        return num1//num2
    

def permutation(input,i):
    if i == len(input)-1:
        temp = []
        for i in input:
            temp.append(i)
        if temp not in history:
            history.append(temp)
    else:
        for j in range(i,len(input)):
            if input[i] != input[j]:
                input[i], input[j] = input[j], input[i]
            permutation(input,i+1)
            input[i], input[j] = input[j], input[i]

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    operator_count = list(map(int,input().split()))
    numbers = list(map(int,input().split()))
    operator = []
    maximum = -10000
    minimum = 10000
    for i,count in enumerate(operator_count):
        for _ in range(count):
            operator.append(i)
    history = []
    permutation(operator,0)
    
    for a in history:
        for i in range(N-1):
            if i == 0:
                result = cal(a[0],numbers[0],numbers[1])
            else:
                result = cal(a[i],result,numbers[i+1])
        if result > maximum:
            maximum = result
        if result < minimum:
            minimum = result
    # print(maximum,minimum)
    print('#{} {}'.format(tc,maximum-minimum))