import sys

sys.stdin = open('sample_input.txt')

def check(A,B):
    for idx in range(4):
        if A[idx] > B[idx]:
            return 'A'
        elif A[idx] < B[idx]:
            return 'B'
        else:
            continue
    else:
        return 'D'

N = int(input())
for _ in range(N):
    A = list(map(int,input().split()))[1:]
    B = list(map(int,input().split()))[1:]
    A_power = [A.count(mark) for mark in range(4,0,-1)]
    B_power = [B.count(mark) for mark in range(4,0,-1)]
    answer = check(A_power, B_power)
    print(answer)