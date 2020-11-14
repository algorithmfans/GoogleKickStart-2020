# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2020 Round D - Problem C. Beauty of Truee
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000386edd
#
# Time:  O(N)
# Space: O(N)
#

from itertools import izip
from functools import partial

def iter_dfs(children, A, B):
    def divide(curr, d):
        stk.append(partial(postprocess, curr, d))
        for child in reversed(children[curr]):
            stk.append(partial(divide, child, d+1))
        stk.append(partial(preprocess, curr, d))

    def preprocess(curr, d):
        A_cnt[curr] -= A_prefix[d%A]
        B_cnt[curr] -= B_prefix[d%B]
        A_prefix[d%A] += 1
        B_prefix[d%B] += 1

    def postprocess(curr, d):
        A_cnt[curr] += A_prefix[d%A]
        B_cnt[curr] += B_prefix[d%B]

    A_prefix, B_prefix, A_cnt, B_cnt = [0]*len(children), [0]*len(children), [0]*len(children), [0]*len(children)
    stk = []
    stk.append(partial(divide, 0, 0))
    while stk:
        stk.pop()()
    return A_cnt, B_cnt

def beauty_of_tree():
    N, A, B = map(int, raw_input().strip().split())
    children = [[] for _ in xrange(N)]
    for i, p in enumerate(map(int, raw_input().strip().split()), 1):
        children[p-1].append(i)
    return float(sum((a+b)*N - a*b for a, b in izip(*iter_dfs(children, A, B))))/N/N

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, beauty_of_tree())
