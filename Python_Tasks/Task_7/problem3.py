
# Problem 3: Mars Exploration
# https://www.hackerrank.com/challenges/mars-exploration/problem

s = input().strip()
expected = "SOS" * (len(s) // 3)

count = sum(a != b for a, b in zip(s, expected))
print(count)
