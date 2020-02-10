import sys

sys.stdin = open('sample_input.txt')

N = int(input())
paper = [[0 for _ in range(101)] for _ in range(101)]
next_paper = 1
for _ in range(N):
    r1, c1, r2, c2 = map(int,input().split())
    for row in range(r1, r1+r2):
        for col in range(c1, c1+c2):
            paper[row][col] = next_paper
    next_paper += 1

answer_list = []
for num in range(1, N+1):
    num_total = 0
    for p in paper:
        num_total += p.count(num)
    answer_list.append(num_total)
for answer in answer_list:
    print(answer)