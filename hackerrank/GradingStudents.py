for i in range(int(input())):
    marks = int(input())
    if marks >= 38:
        lastDigit = marks % 10
        if lastDigit == 9 or lastDigit == 4:
            marks = marks + 1
        if lastDigit == 8 or lastDigit == 3:
            marks = marks + 2
    print(marks)