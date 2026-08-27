T = int(input())
import math

for tc in range(1,T+1):
    N, L = map(int, input().split())
    S = []
    L = []
    for n in range(N):
        S[n], L[n] = map(int, input().split())
    combi = []
    max_score=0
    # 재료 개수 조합으로 모든 case에 대해서 점수와 칼로리 계산
    for i in range(N):
        # M = math.combi(5,i)
        for j in range(N-i+1,0,-1):
        # combi[i][n] = 

        # L이 1000을 넘지 않는 것 중에서 점수(T)가 최대인것
        
    print(f'#{tc} {max_score}')