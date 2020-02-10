import sys

sys.stdin = open('sample_input.txt')

C, R = map(int,input().split())
N = int(input())
market_list = [list(map(int,input().split())) for _ in range(N)]
donggun = list(map(int,input().split()))
answer_list = []
for idx in range(N):
    if donggun[0] == 1:
        if market_list[idx][0] == 1:
            answer_list.append(abs(donggun[1]-market_list[idx][1]))
        elif market_list[idx][0] == 2:
            if donggun[1] + market_list[idx][1] < C:
                answer_list.append(donggun[1] + market_list[idx][1] + R)
            else:
                answer_list.append(2*C-(donggun[1] + market_list[idx][1]) + R)
        elif market_list[idx][0] == 3:
            answer_list.append(donggun[1] + market_list[idx][1])
        elif market_list[idx][0] == 4:
            answer_list.append((C-donggun[1]) + market_list[idx][1])
    elif donggun[0] == 2:
        if market_list[idx][0] == 1:
            if donggun[1] + market_list[idx][1] < C:
                answer_list.append(donggun[1] + market_list[idx][1] + R)
            else:
                answer_list.append(2*C-(donggun[1] + market_list[idx][1]) + R)
        elif market_list[idx][0] == 2:
            answer_list.append(abs(donggun[1]-market_list[idx][1]))
        elif market_list[idx][0] == 3:
            answer_list.append(donggun[1] + (R-market_list[idx][1]))
        elif market_list[idx][0] == 4:
            answer_list.append((C-donggun[1]) + (R-market_list[idx][1]))
    elif donggun[0] == 3:
        if market_list[idx][0] == 1:
            answer_list.append(donggun[1] + market_list[idx][1])
        elif market_list[idx][0] == 2:
            answer_list.append((R-donggun[1]) + market_list[idx][1])
        elif market_list[idx][0] == 3:
            answer_list.append(abs(donggun[1]-market_list[idx][1]))
        elif market_list[idx][0] == 4:
            if donggun[1] + market_list[idx][1] < R:
                answer_list.append(donggun[1] + market_list[idx][1] + C)
            else:
                answer_list.append(2*R-(donggun[1] + market_list[idx][1]) + C)
    elif donggun[0] == 4:
        if market_list[idx][0] == 1:
            answer_list.append(donggun[1] + (C-market_list[idx][1]))
        elif market_list[idx][0] == 2:
            answer_list.append((R-donggun[1]) + (C-market_list[idx][1]))
        elif market_list[idx][0] == 3:
            if donggun[1] + market_list[idx][1] < R:
                answer_list.append(donggun[1] + market_list[idx][1] + C)
            else:
                answer_list.append(2*R-(donggun[1] + market_list[idx][1]) + C)
        elif market_list[idx][0] == 4:
            answer_list.append(abs(donggun[1]-market_list[idx][1]))
print(answer_list)
print(sum(answer_list))