import sys

sys.stdin = open('sample_input.txt')

def male_process(switch,switch_list): # 성별이 남자일 경우
    start_idx = switch-1 # 시작 인덱스를 맞춰줌
    for idx in range(start_idx,len(switch_list),switch): # 시작 인덱스부터 주어진 스위치 번호의 배수만큼 for문을 돌려 변경사항 적용
        if switch_list[idx] == 1:
            switch_list[idx] = 0
        elif switch_list[idx] == 0:
            switch_list[idx] = 1
    return switch_list

def female_process(switch,switch_list): # 성별이 여자일 경우
    start_idx = switch-1 # 시작 인덱스를 맞춰줌
    recur_num = min(len(switch_list[:start_idx]),len(switch_list[start_idx+1:])) # 주어진 스위치 번호를 기준으로 좌우 스위치 길이 중 짧은 방향을 찾음.
    len_cnt = 0 # 양 옆으로 상태가 같은 스위치의 개수 / 2
    for idx in range(1,recur_num+1): # 주어진 스위치 번호를 기준으로 양 옆의 스위치 상태가 같은지 확인
        if switch_list[start_idx+idx] == switch_list[start_idx-idx]:
            len_cnt += 1
            pass
        else: # 다를 경우 탈출
            break

    for idx in range(start_idx-len_cnt,start_idx+len_cnt+1): # 위에서 구한 스위치 범위에 따라 변경사항 적용
        if switch_list[idx] == 1:
            switch_list[idx] = 0
        elif switch_list[idx] == 0:
            switch_list[idx] = 1
    return switch_list

switch_num = int(input())
switch_list = list(map(int,input().split()))
stu_num = int(input())
for _ in range(stu_num):
    sex, switch = map(int,input().split())
    if sex == 1:
        switch_list = male_process(switch,switch_list)
    elif sex == 2:
        switch_list = female_process(switch,switch_list)
for num in range((len(switch_list)//20)+1): # 스위치 리스트에서 20개씩 뽑아내서 출력
    print(*switch_list[0+20*num:20*(num+1)])