import sys
from copy import deepcopy

sys.stdin = open('input.txt')

def my_combinations(iterations, N):
    result = []
    length = len(iterations)
    for i in range(1 << length):
        temp = []
        for j in range(i+1):
            if i & (1 << j):
                temp.append(iterations[j])
        if len(temp) == N:
            result.append(tuple(temp))
    return result

def archer_attack(game_map, archer_position,D):
    result = 0
    cp_map = deepcopy(game_map)
    M = len(cp_map[0])
    while cp_map:
        rg = -1
        dead_enemy = []
        enemy_rush = cp_map[-D:]
        for archer in archer_position:
            kill_enemy = False
            while not kill_enemy:
                if (archer-(D+rg)) < 0:
                    start_num = 0
                else:
                    start_num = (archer-(D+rg))
                if (archer+(D+rg)+1) > M:
                    end_num = M
                else:
                    end_num = (archer+(D+rg)+1)

                for ene_idx in range(start_num, end_num):
                    try:
                        if enemy_rush[rg][ene_idx] == '1':
                            if (rg,ene_idx) not in dead_enemy:
                                kill_enemy = True
                                dead_enemy.append((rg,ene_idx))
                                cp_map[rg][ene_idx] = '0'
                                break
                            else:
                                continue
                    except:
                        continue
                if kill_enemy:
                    break
                rg -= 1
                if rg < -D:
                    break
        result += len(dead_enemy)
        cp_map.pop(-1)
    return result
            
                    


N,M,D = map(int,input().split())
game_map = []
for _ in range(N):
    game_map.append(input().split())

enemy_per_line = []
for j in range(M):
    enemies = 0
    for i in range(N):
        if game_map[i][j] == '1':
            enemies += 1
    enemy_per_line.append(enemies)

if D == 1:
    answer = sum(sorted(enemy_per_line, reverse = True)[:3])
    print(answer)
else:
    answer = 0
    archer_positions = my_combinations([i for i in range(M)], 3)
    for position in archer_positions:
        temp_answer = archer_attack(game_map,position, D)
        if temp_answer > answer:
            answer = temp_answer
    print(answer)
    