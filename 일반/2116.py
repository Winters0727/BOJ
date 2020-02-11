import sys
import copy

sys.stdin = open('sample_input.txt')

N = int(input()) # 답은 맞았지만 시간이 오래걸린다. 다른 방법은 없을까?
max_list = []
dice_list = [list(map(int,input().split())) for _ in range(N)]
for idx in range(6):
    cp_list = copy.deepcopy(dice_list)
    start_dice = cp_list.pop(0)
    idx_list = []
    if idx == 0:
        idx_list.append((0,5))
    elif idx == 1:
        idx_list.append((1,3))
    elif idx == 2:
        idx_list.append((2,4))
    elif idx == 3:
        idx_list.append((3,1))
    elif idx == 4:
        idx_list.append((4,2))
    elif idx == 5:
        idx_list.append((5,0))
    rear_val = start_dice[idx]
    while cp_list:
        temp_dice = cp_list.pop(0)
        temp_idx = temp_dice.index(rear_val)
        if temp_idx == 0:
            idx_list.append((0,5))
            rear_val = temp_dice[5]
        elif temp_idx == 1:
            idx_list.append((1,3))
            rear_val = temp_dice[3]
        elif temp_idx == 2:
            idx_list.append((2,4))
            rear_val = temp_dice[4]
        elif temp_idx == 3:
            idx_list.append((3,1))
            rear_val = temp_dice[1]
        elif temp_idx == 4:
            idx_list.append((4,2))
            rear_val = temp_dice[2]
        elif temp_idx == 5:
            idx_list.append((5,0))
            rear_val = temp_dice[0]
    cp2_list = copy.deepcopy(dice_list)
    for i in range(N):
        cp2_list[i][idx_list[i][0]], cp2_list[i][idx_list[i][1]] = 0, 0
    max_value = 0
    for dice in cp2_list:
        max_value += max(dice)
    max_list.append(max_value)
print(max(max_list))