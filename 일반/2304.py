import sys

sys.stdin = open('sample_input.txt')

N = int(input())
columns = [list(map(int,input().split())) for _ in range(N)] # [point, height]
col_list = sorted(columns, key=lambda x:x[0])
val_list = [col[1] for col in col_list]
max_height = max(val_list)
max_idx = val_list.index(max_height)
answer = 0
if max_idx == 0: # 최고 높이를 갖는 기둥이 제일 왼쪽에 있는 케이스
    for idx in range(len(col_list)):
        if idx == 0:
            answer += max_height
            p_val, h_val = col_list[idx]
        else:
            temp_max = max(val_list[idx:])
            if col_list[idx][1] == temp_max:
                answer += (col_list[idx][0]-p_val)*col_list[idx][1]
                p_val, h_val = col_list[idx]
elif max_idx == len(col_list)-1: # 최고 높이를 갖는 기둥이 제일 오른쪽에 있는 케이스
    for idx in range(len(col_list)):
        if idx == 0:
            p_val, h_val = col_list[idx]
        else:
            if col_list[idx][1] > h_val:
                    answer += (col_list[idx][0]-p_val)*h_val
                    p_val, h_val = col_list[idx]
    answer += max_height
else: # 일반 케이스
    for idx in range(len(col_list)):
        if idx == 0:
            p_val, h_val = col_list[idx]
        elif idx < max_idx:
            if col_list[idx][1] > h_val:
                answer += (col_list[idx][0]-p_val)*h_val
                p_val, h_val = col_list[idx]
        elif idx == max_idx:
            answer += (col_list[idx][0]-p_val)*h_val+col_list[idx][1]
            p_val, h_val = col_list[idx]
        elif idx > max_idx:
            temp_max = max(val_list[idx:])
            if col_list[idx][1] == temp_max:
                answer += (col_list[idx][0]-p_val)*col_list[idx][1]
                p_val, h_val = col_list[idx]
print(answer)