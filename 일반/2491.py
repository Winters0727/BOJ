import sys

sys.stdin = open('sample_input.txt')

N = int(input())
numbers = list(map(int,input().split()))
if N == 1: # 개수개 1개 일때의 예외처리를 해줘야한다!
    answer = 1
else:
    cnt_list = []
    cnt = 1
    for idx in range(1,len(numbers)):
        if numbers[idx] - numbers[idx-1] >= 0:
            cnt += 1
        else:
            if cnt == 1:
                continue
            else:
                cnt_list.append(cnt)
                cnt = 1
    if cnt > 1:
        cnt_list.append(cnt)
    cnt = 1
    for idx in range(1,len(numbers)):
        if numbers[idx] - numbers[idx-1] <= 0:
            cnt += 1
        else:
            if cnt == 1:
                continue
            else:
                cnt_list.append(cnt)
                cnt = 1
    if cnt > 1:
        cnt_list.append(cnt)
    if max(cnt_list) > 2:
        answer = max(cnt_list)
    else:
        answer = 2
print(answer)