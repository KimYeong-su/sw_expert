cases = 10

for case in range(cases):
    search = int(input())
    base = [] # 주어진 배열을 그대로
    base2 = [] # 주어진 배열의 행과 열을 바꾸기
    for i in range(8):
        base.append(list(input()))

    for i in range(8): #배열의 행과 열 바꾸기
        temp = []
        for k in range(8):
            temp.append(base[k][i])
        base2.append(temp)

    cnt = 0
    for i in range(8):
        for j in range(len(base)-search+1):
            if base[i][j:j+search] == list(reversed(base[i][j:j+search])):
                cnt += 1
            if base2[i][j:j+search] == list(reversed(base2[i][j:j+search])):
                cnt += 1
    
    print(f'#{case+1} {cnt}')