import sys

sys.stdin = open('sample_input.txt')

T = int(sys.stdin.readline())
memo = [[0 for _ in range(3)] for _ in range(T)]
for i in range(T):
    RGB = list(map(int,sys.stdin.readline().split()))
    if i == 0:
        memo[i][0] = RGB[0]
        memo[i][1] = RGB[1]
        memo[i][2] = RGB[2]
    else:
        memo[i][0] = min(memo[i-1][1],memo[i-1][2]) + RGB[0]
        memo[i][1] = min(memo[i-1][0],memo[i-1][2]) + RGB[1]
        memo[i][2] = min(memo[i-1][0],memo[i-1][1]) + RGB[2]
print(min(memo[T-1]))