cases = int(input())

for case in range(cases):
    P,Q,R,S,W = map(int, input().split())
    A_rate = P * W
    if W <= R:
        B_rate = Q
    else:
        B_rate = Q + (W-R)*S
    
    if A_rate <= B_rate:
        print(f'#{case+1} {A_rate}')
    else:
        print(f'#{case+1} {B_rate}')