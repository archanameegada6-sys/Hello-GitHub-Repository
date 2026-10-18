
# Problem 17: Finding the Percentage
# https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        data = input().split()
        name = data[0]
        marks = list(map(float, data[1:]))
        student_marks[name] = marks

    query_name = input()
    scores = student_marks[query_name]

    average = sum(scores) / len(scores)
    print(f"{average:.2f}")
