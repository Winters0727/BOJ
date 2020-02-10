import sys

sys.stdin = open('sample_input.txt')

N, K = map(int,input().split())
stu_list = [[0,0] for _ in range(6)]
for _ in range(N):
    sex, grade = map(int,input().split())
    if sex == 0:
        stu_list[grade-1][0] += 1
    elif sex == 1:
        stu_list[grade-1][1] += 1
answer = 0
for idx in range(6):
    if stu_list[idx][0]%K:
        answer += (stu_list[idx][0]//K)+1
    else:
        answer += stu_list[idx][0]//K
    if stu_list[idx][1]%K:
        answer += (stu_list[idx][1]//K)+1
    else:
        answer += stu_list[idx][1]//K
print(answer)