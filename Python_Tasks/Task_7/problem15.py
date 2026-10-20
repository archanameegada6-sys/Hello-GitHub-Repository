
# Problem 15: Game of Thrones - I
# https://www.hackerrank.com/challenges/game-of-thrones/problem

from collections import Counter

s = input().strip()
odd_counts = sum(count % 2 for count in Counter(s).values())

print("YES" if odd_counts <= 1 else "NO")
