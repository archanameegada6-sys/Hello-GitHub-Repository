
# Problem 13: Sherlock and the Valid String
# https://www.hackerrank.com/challenges/sherlock-and-the-valid-string/problem

from collections import Counter

s = input().strip()
freq = Counter(Counter(s).values())

if len(freq) == 1:
    print("YES")
elif len(freq) == 2:
    items = list(freq.items())

    if (items[0][0] == 1 and items[0][1] == 1) or (
        items[1][0] == 1 and items[1][1] == 1
    ):
        print("YES")
    elif abs(items[0][0] - items[1][0]) == 1 and (
        items[0][1] == 1 or items[1][1] == 1
    ):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
