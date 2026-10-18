# Problem 17: Check Strict Superset
# HackerRank: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

A = set(map(int, input().split()))
n = int(input())

is_strict_superset = True

for _ in range(n):
    B = set(map(int, input().split()))
    if not A > B:
        is_strict_superset = False
        break

print(is_strict_superset)
