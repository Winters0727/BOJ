import sys

sys.stdin = open('sample_input.txt')

N = int(input())
ticket_list = list(map(int,input().split()))
answer_list = []
for num in range(N):
    answer_list.insert(ticket_list[num],num+1)
answer_list = answer_list[::-1]
print(*answer_list)