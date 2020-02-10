import sys

sys.stdin = open('sample_input.txt')

map_list = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(4):
    r1, c1, r2, c2 = map(int,input().split())
    for row in range(r1,r2):
        for col in range(c1,c2):
            map_list[row][col] = 1
answer = 0
for k in map_list:
    answer += sum(k)
print(answer)
