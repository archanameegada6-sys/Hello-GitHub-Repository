
# Problem 17: Separate the Numbers
# https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separateNumbers(s):
    for i in range(1, len(s) // 2 + 1):
        first = s[:i]

        if first.startswith("0"):
            continue

        expected = first
        built = ""

        while len(built) < len(s):
            built += expected
            expected = str(int(expected) + 1)

        if built == s:
            print("YES", first)
            return

    print("NO")


q = int(input())
for _ in range(q):
    separateNumbers(input().strip())
