
# Problem 6: Pangrams
# https://www.hackerrank.com/challenges/pangrams/problem

s = input().lower()
letters = set(c for c in s if c.isalpha())

print("pangram" if len(letters) == 26 else "not pangram")
