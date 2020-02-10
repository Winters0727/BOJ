import sys

sys.stdin = open('sample_input.txt')

col, row = map(int,input().split())
paper = [[1 for _ in range(col)] for _ in range(row)]
row_point, col_point = [0], [0]
N = int(input())
for _ in range(N):
    way, point = map(int,input().split())
    if way == 0:
        row_point.append(point)
    elif way == 1:
        col_point.append(point)
row_point.append(row)
col_point.append(col)
row_point = sorted(row_point)
col_point = sorted(col_point)
area_list = []
if row_point and col_point:
    for r in range(1,len(row_point)):
        for c in range(1,len(col_point)):
            area_list.append((row_point[r]-row_point[r-1])*(col_point[c]-col_point[c-1]))
    answer = max(area_list)
elif not col_point and row_point:
    for idx in range(1,len(row_point)):
        area_list.append((row_point[idx]-row_point[idx-1])*col)
    answer = max(area_list)
elif not row_point and col_point:
    for idx in range(1, len(col_point)):
        area_list.append((col_point[idx]-col_point[idx-1])*row)
    answer = max(area_list)
else:
    answer = col*row
print(answer)