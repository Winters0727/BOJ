import sys

sys.stdin = open('sample_input.txt')

dx = [0,0,1,-1]
dy = [1,-1,0,0]

N = int(sys.stdin.readline())
map_list = []
for _ in range(N):
    map_list.append(list(map(int,list(input()))))
visited = [[0 for _ in range(N)] for _ in range(N)]
stack = []
answer = []
for row in range(N):
    for col in range(N):
        if visited[row][col]:
            continue
        else:
            if map_list[row][col]:
                cnt = 1
                visited[row][col] = 1
                stack.append((row,col))
                while stack:
                    o_r, o_c = stack.pop()
                    for k in range(4):
                        n_r, n_c = o_r + dy[k], o_c + dx[k]
                        if 0 <= n_r <= N-1 and 0 <= n_c <= N-1 and not visited[n_r][n_c] and map_list[n_r][n_c]:
                            visited[n_r][n_c] = 1
                            cnt += 1
                            stack.append((n_r,n_c))
                answer.append(cnt)
answer.sort()
print(len(answer))
for ans in answer:
    print(ans)