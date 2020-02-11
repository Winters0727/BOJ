import sys

sys.stdin = open('boj2.txt')

W, H = map(int,input().split())
start_point = list(map(int,input().split()))
t = int(input())
if t <= (W-start_point[0]):
    start_point[0] += t
else:
    d, m = divmod(t-(W-start_point[0]),W)
    if d%2:
        start_point[0] = m
    else:
        start_point[0] = W-m
        
if t <= (H-start_point[1]):
    start_point[1] += t
else:
    d, m = divmod(t-(H-start_point[1]),H)
    if d%2:
        start_point[1] = m
    else:
        start_point[1] = H-m

print(*start_point)