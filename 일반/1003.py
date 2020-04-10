import sys

sys.stdin = open('sample_input.txt')

memo = [(1,0),(0,1)]

def fibo(N):
    global memo
    if N < len(memo):
        pass
    else:
        for i in range(len(memo),N+1):
            memo.append((memo[i-2][0]+memo[i-1][0],memo[i-2][1]+memo[i-1][1]))
    print(*memo[N])
    return None

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    fibo(N)