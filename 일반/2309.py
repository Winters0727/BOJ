from itertools import combinations
import sys

sys.stdin = open('sample_input.txt')

real = [True for _ in range(9)]
small = [int(input()) for _ in range(9)]
all_sum = sum(small)
comb = list(combinations([N for N in range(9)],2))
bad_guys = []
for c in comb:
    if all_sum-(small[c[0]]+small[c[1]]) == 100:
        bad_guys.append(c)
real[bad_guys[0][0]], real[bad_guys[0][1]] = False, False
answer = sorted([small[idx] for idx in range(9) if real[idx] == True])
for ans in answer:
    print(ans)