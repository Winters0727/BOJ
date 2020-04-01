import sys

sys.stdin = open('sample_input.txt')

dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,1,-1]

while True:
    cnt = 0
    C, R = list(map(int,sys.stdin.readline().split()))
    if C == 0 and R ==0:
        break
    else:
        map_list = []
        for _ in range(R):
            map_list.append(list(map(int,sys.stdin.readline().split())))
        visited = [[0 for _ in range(C)] for _ in range(R)]
        stack = []
        for row in range(R):
            for col in range(C):
                if visited[row][col]:
                    continue
                else:
                    if map_list[row][col]:
                        cnt += 1
                        visited[row][col] = 1
                        stack.append((row,col))
                        while stack:
                            o_r, o_c = stack.pop()
                            for k in range(8):
                                n_r, n_c = o_r + dy[k], o_c + dx[k]
                                if 0 <= n_r <= R-1 and 0 <= n_c <= C-1 and not visited[n_r][n_c] and map_list[n_r][n_c]:
                                    visited[n_r][n_c] = 1
                                    stack.append((n_r,n_c))
                    else:
                        visited[row][col] = 1
    print(cnt)