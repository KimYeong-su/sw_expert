num = int(input())
result = []
for i in range(1,num+1):
    n = 0
    for k in str(i):
        if str(k) == '3' or str(k) == '6' or str(k) == '9':
            n += 1
    if n == 0:
        result.append(int(i))
    else:
        result.append('-'*n)

print(' '.join(map(str, result)))