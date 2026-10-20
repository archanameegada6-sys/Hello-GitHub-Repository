
# Problem 16: Caesar Cipher
# https://www.hackerrank.com/challenges/caesar-cipher-1/problem

n = int(input())
s = input().strip()
k = int(input()) % 26

result = []

for c in s:
    if 'a' <= c <= 'z':
        result.append(chr((ord(c) - ord('a') + k) % 26 + ord('a')))
    elif 'A' <= c <= 'Z':
        result.append(chr((ord(c) - ord('A') + k) % 26 + ord('A')))
    else:
        result.append(c)

print("".join(result))
