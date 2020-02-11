import sys

sys.stdin = open('sample_input.txt')

N, D = map(int,input().split())
temp_list = list(map(int,input().split()))
temp_val = sum(temp_list[:D])
max_val = temp_val
for i in range(N-D):
    temp_val += (temp_list[i+D]-temp_list[i])
    if temp_val > max_val:
        max_val = temp_val
print(max_val)