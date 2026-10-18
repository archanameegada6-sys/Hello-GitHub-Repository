# Problem 3: Mutations
# https://www.hackerrank.com/challenges/python-mutations/problem

if __name__ == '__main__':
    s = input()
    i, c = input().split()

    s = s[:int(i)] + c + s[int(i) + 1:]
    print(s)
