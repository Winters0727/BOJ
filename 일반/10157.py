import sys

sys.stdin = open('sample_input.txt')

C, R = map(int,input().split()) # python3 시간초과, pypy3 통과
N = int(input())
way = 'up'
start_point = [1,1]
turn = 0
if N > C*R:
    print(0)
else:
    for _ in range(N-1):
        if way == 'up':
            if start_point[1] + 1 > R - turn:
                start_point[0] += 1
                way = 'right'
            else:
                start_point[1] += 1
        elif way == 'down':
            if start_point[1] - 1 < 1 + turn:
                start_point[0] -= 1
                turn += 1
                way = 'left'
            else:
                start_point[1] -= 1
        elif way == 'right':
            if start_point[0] + 1 > C - turn:
                start_point[1] -= 1
                way = 'down'
            else:
                start_point[0] += 1
        elif way == 'left':
            if start_point[0] - 1 < 1 + turn:
                start_point[1] += 1
                way = 'up'
            else:
                start_point[0] -= 1
    print(*start_point)