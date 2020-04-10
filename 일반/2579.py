import sys

sys.stdin = open('sample_input.txt')

T = int(sys.stdin.readline())
stair = [0]
for i in range(T):
    s = int(sys.stdin.readline())
    stair.append(s)
if T > 2:
    memo = [0,stair[1],stair[1]+stair[2]]
    for i in range(3, T+1):
        val1 = memo[i-2] + stair[i]
        val2 = memo[i-3] + stair[i-1] + stair[i]
        memo.append(max(val1,val2))
    print(memo[T])
else:
    print(sum(stair))