T = int(input())

for tc in range(1,T+1):
    N, L = map(int, input().split())
    for n in range(N):
        T[n], L[n] = map(int, input().split())

    max_score=0
    for i in range(N):
        

    print(f'#{tc} {max_score}')