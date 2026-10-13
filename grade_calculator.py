
def calculate_total(marks):
    if not marks:
        raise ValueError("Marks cannot be empty")

    for mark in marks:
        if not isinstance(mark, (int, float)) or isinstance(mark, bool):
            raise ValueError("Marks must be numbers")
        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100")

    return sum(marks)


def calculate_percentage(marks):
    total = calculate_total(marks)
    return round(total / len(marks), 2)


def calculate_grade(percentage):
    if not isinstance(percentage, (int, float)) or isinstance(percentage, bool):
        raise ValueError("Percentage must be a number")
    if percentage < 0 or percentage > 100:
        raise ValueError("Percentage must be between 0 and 100")

    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    return "F"


if __name__ == "__main__":
    marks = [85, 90, 78, 88, 92]
    total = calculate_total(marks)
    percentage = calculate_percentage(marks)
    grade = calculate_grade(percentage)

    print("Total Marks:", total)
    print("Percentage:", percentage, "%")
    print("Grade:", grade)