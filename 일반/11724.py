import sys
from collections import deque

sys.stdin = open('sample_input.txt')

def DFS(edge_list, S):
    global N, stack, visited, count
    stack.append(S)
    visited[S] = 1
    while stack:
        for j in range(N):
            if edge_list[stack[-1]][j] == 1 and visited[j] == 0:
                visited[j] = 1
                stack.append(j)
                break
        else:
            stack.pop()
    count += 1

N, M = map(int,sys.stdin.readline().split())
if M == 0:
    print(N)
else:
    edge_list = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        i,j = map(int,sys.stdin.readline().split())
        edge_list[i-1][j-1] = 1
        edge_list[j-1][i-1] = 1
    visited = [0 for _ in range(N)]
    stack = deque()
    count = 0
    for i in range(N):
        if visited[i] == 1:
            continue
        DFS(edge_list, i)
    print(count)