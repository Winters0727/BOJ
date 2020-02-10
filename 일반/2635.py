N = int(input())
answer = []
for i in range(N,0,-1):
    ans_list = [N,i]
    temp_N = N
    while True:
        if ans_list[-2] - ans_list[-1] > 0:
            ans_list.append(ans_list[-2] - ans_list[-1])
        elif ans_list[-2] - ans_list[-1] < 0:
            break
        else:
            ans_list.append(0)
    if len(ans_list) > len(answer):
        answer = ans_list
print(len(answer))
print(*answer) 