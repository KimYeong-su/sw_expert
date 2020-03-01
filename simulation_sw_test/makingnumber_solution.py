def cal(oper,num1,num2):
    if oper == 0:
        return num1+num2
    elif oper == 1:
        return num1-num2
    elif oper == 2:
        return num1*num2
    else:
        return int(num1/num2)
    

def permutation(arr, r):
    # 1.
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            temp = []
            for i in chosen:
                temp.append(i)
            history.append(temp)
            return
	
        for i in range(len(arr)):
	    # 3.
            if not used[i] and (i == 0 or arr[i-1] != arr[i] or used[i-1]):
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    operator_count = list(map(int,input().split()))
    numbers = list(map(int,input().split()))
    operator = []
    maximum = -100000000
    minimum = 100000000
    for i,count in enumerate(operator_count):
        for _ in range(count):
            operator.append(i)
    history = []
    permutation(operator,N-1)

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
