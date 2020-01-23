case = int(input())

def pascal(n):
    result = []
    for i in range(n):
        if i ==0 or i == n-1:
            result.append(1)
        else:
            result.append(pascal(n-1)[i-1]+pascal(n-1)[i])
    return result


for i in range(case):
    lines = int(input())
    print(f'#{i+1}')
    for line in range(1,lines+1):
        print(" ".join(map(str,pascal(line))))