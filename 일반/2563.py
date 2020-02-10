import sys

sys.stdin = open('sample_input.txt')

N = int(input())
white = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(N):
    R, C = map(int,input().split())
    for row in range(R, R+10):
        for col in range(C, C+10):
            white[row][col] = 1
answer = 0
for row in white:
    answer += sum(row)
print(answer)