# Problem 9: Word Order
# https://www.hackerrank.com/challenges/word-order/problem

if __name__ == '__main__':
    n = int(input())
    word_count = {}

    for _ in range(n):
        word = input()
        word_count[word] = word_count.get(word, 0) + 1

    print(len(word_count))
    print(*word_count.values())
