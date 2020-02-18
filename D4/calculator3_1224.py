def is_number(token):
    if token in ('*','+','(',')'):
        return False
    return True

def icp(token):
    if token == '*':
        return 2
    elif token == '+':
        return 1
    elif token == '(':
        return 3

def isp(token):
    if token == '*':
        return 2
    elif token == '+':
        return 1
    elif token == '(':
        return 0

def cal(token,a,b):
    if token == '+':
        return a+b
    elif token == '*':
        return a*b


for tc in range(1,11):
    N = int(input())
    infix = list(input())
    postfix=[]
    top = -1
    stack=[]
    for t in infix:
        if is_number(t):
            postfix.append(t)
        else:
            if len(stack)==0:
                top +=1
                stack.append(t)
            else:
                if t == ')':
                    while stack[top] != '(':
                        postfix.append(stack.pop())
                        top -= 1
                    stack.pop()
                    top -= 1
                elif (icp(t)>isp(stack[top])):
                    stack.append(t)
                    top +=1
                else:
                    while icp(t)<=isp(stack[top]):
                        postfix.append(stack.pop())
                        top -=1
                    stack.append(t)
                    top +=1

    for c in postfix:
        if is_number(c):
            stack.append(c)
        else:
            b = float(stack.pop())
            a = float(stack.pop())
            stack.append(cal(c,a,b))
    print('#{} {}'.format(tc,int(stack.pop())))