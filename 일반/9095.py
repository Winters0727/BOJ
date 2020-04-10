import sys

sys.stdin = open('sample_input.txt')

memo = [0,1,2,4]

def solve(N):
    global memo
    if N < len(memo):
        pass
    else:
        for _ in range(len(memo),N+1):
            memo.append(sum(memo[-3:]))
    print(memo[N])
    return None

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    solve(N)