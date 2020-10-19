# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round G - Problem D. Merge Cards
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000415054#problem
#
# Time:  O(K^(1/2))
# Space: O(1)
#

def merge_cards():
    N = input()
    A = map(int, raw_input().strip().split())
    return sum(a*dp[N][i] for i, a in enumerate(A))

MAX_N = 5000
dp = [[0.0]*MAX_N for _ in xrange(MAX_N+1)]  # dp[i][j]: expected count of (j+1)-th cards with total i cards 
for i in xrange(2, MAX_N+1):
    for j in xrange(i):
        if j > 0:
            dp[i][j] += ((j-1)-1+1)*dp[i-1][j-1]    # pick (0,1)~(j-2,j-1)
            dp[i][j] += 1.0 + dp[i-1][j-1]          # pick (j-1,j)
        if j < i-1:
            dp[i][j] += 1.0 + dp[i-1][j]            # pick (j,j+1)
            dp[i][j] += ((i-1)-(j+2)+1)*dp[i-1][j]  # pick (j+1,j+2)~(i-2,i-1)
        dp[i][j] /= (i-1)  # (i-1) choices in i cards

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, merge_cards())
