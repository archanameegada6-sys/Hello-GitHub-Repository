
# Problem 16: Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    records = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    unique_scores = sorted(set(score for name, score in records))
    second_lowest = unique_scores[1]

    names = sorted(
        name for name, score in records
        if score == second_lowest
    )

    for name in names:
        print(name)
