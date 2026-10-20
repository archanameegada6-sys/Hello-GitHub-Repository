
# Problem 7: Alphabet Rangoli
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    import string

    alphabet = string.ascii_lowercase
    width = 4 * size - 3

    for i in range(size - 1, -size, -1):
        row = list(range(size - 1, abs(i) - 1, -1))
        letters = [alphabet[size - 1 - j] for j in row]
        line = "-".join(letters + letters[-2::-1])
        print(line.center(width, "-"))


n = int(input())
print_rangoli(n)
