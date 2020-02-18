def promissing(a):
    #같은열, 같은 대각선 여부 판단 : True False 리턴
    for i in range(1,a):
        if col[a]==col[i]:
            return False
        if abs(i-a)==abs(col[i]-col[a]):
            return False
    return True

def queen(level):
    global cnt
    if level == N+1:
        cnt+=1
        return
    #재귀호출로 각 행에 체스를 놓기
    for i in range(level,N+1):
        col[level] = i
        if promissing(level)==False:
            continue
        queen(level+1)
        

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    col = [0]*(N+1)
    cnt = 0
    queen(1)
    print(cnt)