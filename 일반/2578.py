import sys

sys.stdin = open('sample_input.txt')

def bingo_checker(bingo):
    cnt = 0
    for row in bingo: # 가로 체크
        if row == [0,0,0,0,0]:
            cnt += 1
    for col in range(5): # 세로 체크
        temp = []
        for row in range(5):
            temp += [bingo[row][col]]
        if temp == [0,0,0,0,0]:
            cnt += 1
    temp1, temp2 = [], []
    for idx in range(5): # 대각  체크
        temp1 += [bingo[idx][idx]]
        temp2 += [bingo[4-idx][idx]]
    if temp1 == [0,0,0,0,0]:
        cnt += 1
    if temp2 == [0,0,0,0,0]:
        cnt += 1
    return cnt

bingo = [list(map(int,input().split())) for _ in range(5)]
del_list = []
for _ in range(5):
    del_list += list(map(int,input().split()))
counter = 0
for del_element in del_list:
    counter += 1
    for row in bingo:
        if del_element in row:
            row[row.index(del_element)] = 0
            break
    cnt = bingo_checker(bingo)
    if cnt >= 3:
        break
print(counter)