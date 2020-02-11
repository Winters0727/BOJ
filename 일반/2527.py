import sys

sys.stdin = open('sample_input.txt')

def check(r_set, c_set):
    if len(r_set) > 1 and len(c_set) > 1:
        return 'a'
    elif (len(r_set) > 1 and len(c_set) == 1) or (len(c_set) > 1 and len(r_set) == 1):
        return 'b'
    elif len(r_set) == 1 and len(c_set) == 1:
        return 'c'
    else:
        return 'd'

for _ in range(4):
    ar1, ac1, ar2, ac2, br1, bc1, br2, bc2 = map(int,input().split())
    ar_set = set([num for num in range(ar1,ar2+1)])
    ac_set = set([num for num in range(ac1,ac2+1)])
    br_set = set([num for num in range(br1,br2+1)])
    bc_set = set([num for num in range(bc1,bc2+1)])
    r_set = ar_set.intersection(br_set)
    c_set = ac_set.intersection(bc_set)
    answer = check(r_set, c_set)
    print(answer)