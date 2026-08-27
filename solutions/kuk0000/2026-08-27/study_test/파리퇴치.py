# test case 입력 받기
T = int(input())

for tc in range(1,T+1):
    # 배열 크기, 파리채 크기 입력 받기
    N, M = map(int, input().split())
    # 배열 초기화
    fly_arr = []
    # 배열 안의 숫자(파리의 개수) 입력 받기
    for n in range(N):
        fly_arr.append(list(map(int,input().split())))
    # 최대 kill 수 계산을 위한 초기화
    max_kill = 0

    # 최대한 많은 차리 죽이는 경우를 sliding으로 구하기
    for i in range(N-M+1): # => N-M+1인 이유 : 최대로 죽이는것이므로 파리채가 파리영역을 넘어가지 않도록(N-M), range(n)은 n-1까지만 case돌리므로 +1
            for j in range(N-M+1):
                # 파리채 한 번 내려칠 때 죽이는 파리개수
                sum_kill = 0
                for m in range(M):
                    for k in range(M):
                        sum_kill += fly_arr[i+m][j+k]
                # 기존에 최대로 죽인 파리개수보다 더 많은 수라면 해당 값이 max_kill이 되도록
                if max_kill < sum_kill:
                    max_kill = sum_kill

    print(f'#{tc} {max_kill}')