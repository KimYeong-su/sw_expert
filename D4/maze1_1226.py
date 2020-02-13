def find(y,x):
    ny, nx = y, x
    stack = []
    top = -1

    top += 1
    stack.append((y,x))
    flag = 0
    while True:
        if base[ny][nx+1] == 0:
            base[ny][nx]=4
            top+=1
            nx+=1
            stack.append((ny,nx))
        elif base[ny][nx-1] == 0:
            base[ny][nx]=4
            top+=1
            nx-=1
            stack.append((ny,nx))
        elif base[ny+1][nx] == 0:
            base[ny][nx]=4
            top+=1
            ny+=1
            stack.append((ny,nx))
        elif base[ny-1][nx] == 0:
            base[ny][nx]=4
            top+=1
            ny-=1
            stack.append((ny,nx))
        elif base[ny-1][nx]==3 or base[ny+1][nx]==3 or base[ny][nx-1]==3 or base[ny][nx+1]==3:
            flag = 1
            break
        else:
            ny,nx = stack.pop(top)
            top-=1

        if len(stack)==0:
            break
    return flag

for i in range(10):
    tc = int(input())
    base = [list(map(int,input())) for _ in range(16)]

    a = find(1,1)
    if a==1:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))
