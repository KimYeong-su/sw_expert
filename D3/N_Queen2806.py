def promissing(a):
    #같은열, 같은 대각선 여부 판단 : True False 리턴
    for i in col:
        if a==i:
            return False
    return True

def queen(level):
    global cnt
    if level > N:
        return
    if promissing(level)==False:
        return
    #재귀호출로 각 행에 체스를 놓기
    col[level] = i

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    col = [0]*(N+1)
    cnt = 0
    queen(1)
    print(cnt)