def tank(m, c, i, j, d,height,width): # 탱크 동작 함수
    if c == 'U':
        d = 1
        if i-1 >= 0:
            if m[i-1][j] == '.':
                i = i-1
    elif c == 'D':
        d = 3
        if i+1<=height:
            if m[i+1][j] == '.':
                i = i+1
    elif c == 'L':
        d = 4
        if j-1 >= 0:
            if m[i][j-1] == '.':
                j = j-1
    elif c == 'R':
        d = 2
        if j+1 <= width:
            if m[i][j+1] == '.':
                j = j+1
    elif c == 'S':
        if 0<i<height and 0<j<width:
            if d == 1:
                for p in range(i-1,-1,-1):
                    if m[p][j] == '#':
                        break
                    elif m[p][j] == '*':
                        m[p][j]=='.'
                        break
            if d == 3:
                for p in range(i+1,height):
                    if m[p][j] == '#':
                        break
                    elif m[p][j] == '*':
                        m[p][j]=='.'
                        break
            if d == 2:
                for p in range(j+1,width):
                    if m[i][p] == '#':
                        break
                    elif m[i][p] == '*':
                        m[i][p]=='.'
                        break
            if d == 2:
                for p in range(j-1,-1,-1):
                    if m[i][p] == '#':
                        break
                    elif m[i][p] == '*':
                        m[i][p]=='.'
                        break


cases = int(input())

for case in range(cases):

    # 필드 생성하기
    H, W = map(int,input().split())
    field = []
    for i in range(H):
        field.append(list(input()))
    
    # 탱크 현 위치 확인하기(field[i][j])
    for i in range(H):
        if '^' in field[i]:
            j = field[i]
            d = 1
            field[i][j] = '.'
            break
        elif 'v' in field[i]:
            j = field[i].index('v')
            d = 2
            field[i][j] = '.'
            break
        elif '<' in field[i]:
            j = field[i].index('<')
            d = 3
            field[i][j] = '.'
            break
        elif '>' in field[i]:
            j = field[i].index('>')
            d = 4
            field[i][j] = '.'
            break

    # 명령 받아들이기
    command_num = int(input())
    command = list(input())

    # 탱크 동작하기
    for z in command:
        tank(field,z,i,j,d,H,W)

    for q in field:
        print(q)
