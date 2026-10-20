
# Problem 20: Super Reduced String
# https://www.hackerrank.com/challenges/reduced-string/problem

def superReducedString(s):
    stack = []

    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return "".join(stack) if stack else "Empty String"


s = input().strip()
print(superReducedString(s))
