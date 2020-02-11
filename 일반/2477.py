import sys

sys.stdin = open('sample_input.txt')

N = int(input())
val = []
H, W = [], []
for _ in range(6):
    temp = list(map(int,input().split()))
    if temp[0] == 1 or temp[0] == 2:
        val.append(temp[1])
        H.append(temp[1])
    elif temp[0] == 3 or temp[0] == 4:
        val.append(temp[1])
        W.append(temp[1])
max_H, max_W = max(H), max(W)
min_val = []
for idx in range(len(val)):
    if idx == 0:
        temp = val[1] + val[-1]
    elif idx == len(val)-1:
        temp = val[len(val)-2] + val[0]
    else:
        temp = val[idx-1] + val[idx+1]
    if temp == max_H:
        min_val.append(idx)
    if temp == max_W:
        min_val.append(idx)
area = max_H*max_W - val[min_val[0]]*val[min_val[1]]
answer = N*area
print(answer)