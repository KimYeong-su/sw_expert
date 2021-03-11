tc = 1
while True:
    try:
        N = int(input())
    except:
        break
    base = list(input())
    stack = []
    rule = {'}':'{', '>':'<', ')':'(', ']':'['}
    for p in base:
        if p in ['{','[','<','(']:
            stack.append(p)
        else:
            if len(stack)==0:
                print(f'#{tc} 0')
                break
            if stack[-1] == rule[p]:
                stack.pop(-1)
            else:
                print(f'#{tc} 0')
                break
    else:
        print(f'#{tc} 1')
    tc += 1