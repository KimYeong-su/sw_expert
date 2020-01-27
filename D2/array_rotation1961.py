def zero_base(num):
    base = []
    for i in range(num):
        row = []
        for k in range(num):
            row.append(0)
        base.append(row)
    return base

def rotation_90(base, base_degree, num):
    for i in range(num):
        for k in range(num):
            base_degree[i][k] = base[num-k-1][i]
    return base_degree

def rotation_180(base, base_degree, num):
    for i in range(num):
        for k in range(num):
            base_degree[i][k] = base[num-1-i][num-1-k]
    return base_degree

def rotation_270(base, base_degree, num):
    for i in range(num):
        for k in range(num):
            base_degree[i][k] = base[k][num-1-i]
    return base_degree

cases = int(input())

for case in range(cases):
    num = int(input())
    base_90 = zero_base(num)
    base_180 = zero_base(num)
    base_270 = zero_base(num)
    base = []

    for n in range(num):
        row = []
        for m in map(int, input().split()):
            row.append(m)
        base.append(row)

    print(f'#{case+1}')
    for p in range(num):
        print(''.join(map(str,rotation_90(base,base_90,num)[p])),''.join(map(str,rotation_180(base,base_180,num)[p])),''.join(map(str,rotation_270(base,base_270,num)[p])))