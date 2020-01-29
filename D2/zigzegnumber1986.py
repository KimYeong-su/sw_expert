cases = int(input())

for case in range(cases):
    num = int(input())
    result = 0
    for n in range(1,num+1):
        if n%2==1:
            result += n
        else:
            result -= n

    print(f'#{case+1} {result}')