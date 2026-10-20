
# Problem 19: Weighted Uniform Strings
# https://www.hackerrank.com/challenges/weighted-uniform-string/problem

s = input().strip()
n = int(input())
queries = [int(input()) for _ in range(n)]

weights = set()
previous = ""
current_weight = 0

for c in s:
    if c == previous:
        current_weight += ord(c) - ord('a') + 1
    else:
        current_weight = ord(c) - ord('a') + 1

    weights.add(current_weight)
    previous = c

for q in queries:
    print("Yes" if q in weights else "No")
