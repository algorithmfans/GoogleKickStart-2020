# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Kick Start 2020 Round F - Problem D. Yeehtzee
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff48/00000000003f4dea
#
# Time:  O(M * states), number of states with sum <= N and length <= K, which is at most sum(partition(i) for i in [0..N])
# Space: O(M * states)
#
# if N = 50, number of states is at most 1,295,971
# see https://oeis.org/A000041/list, 
# p[0..50] = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56, 77, 101, 135, 176, 231, 297, 385, 490, 627, 792, 1002, 1255, 1575, 1958, 2436, 3010, 3718, 4565, 5604, 6842, 8349, 10143, 12310, 14883, 17977, 21637, 26015, 31185, 37338, 44583, 53174, 63261, 75175, 89134, 105558, 124754, 147273, 173525, 204226]
#

def memoization(A, curr, lookup):
    if tuple(curr) not in lookup:
        count, total = float(len(curr)), 0
        left = 0
        while left < len(curr):
            right = left
            while right+1 < len(curr) and curr[right+1] == curr[left]:
                right += 1
            if curr[right]+1 <= A[right]:
                curr[right] += 1
                count += memoization(A, curr, lookup)*(right-left+1)
                curr[right] -= 1
                total += right-left+1
            left = right+1
        lookup[tuple(curr)] = count/total
    return lookup[tuple(curr)]

def yeehtzee():
    N, M, K = map(int, raw_input().strip().split())
    A = [0]*(M-K)
    for _ in xrange(K):
        A.append(input())
    return memoization(A, [0]*M, {tuple(A):0.0})

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, yeehtzee())
