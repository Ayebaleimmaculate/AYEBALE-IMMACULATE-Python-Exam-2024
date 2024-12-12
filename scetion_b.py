# Ask the user for their age
age = int(input("Please enter your age: "))

# Checking  if the age is greater than or equal to 18
if age >= 18:
    print("You are eligible.")
else:
    print("You are not eligible.")




def grade_students(mark):
    # Determine the grade based on the mark
    if mark >= 90:
        return 'A'
    elif 80 <= mark < 90:
        return 'B'
    elif 70 <= mark < 80:
        return 'C'
    elif 60 <= mark < 70:
        return 'D'
    else:
        return 'F'

# Testing for mark 85
test_mark = 85
grade = grade_students(test_mark)
grade




# Modified unction to handle invalid input
def grade_students(mark):
    try:
        # Convert mark to a float
        mark = float(mark)
        # Determine the grade based on the mark
        if mark >= 90:
            return 'A'
        elif 80 <= mark < 90:
            return 'B'
        elif 70 <= mark < 80:
            return 'C'
        elif 60 <= mark < 70:
            return 'D'
        else:
            return 'F'
    except ValueError:
        return "invalid input"

# Testing with valid input
valid_mark = 85
valid_grade = grade_students(valid_mark)

# Testing with invalid input
invalid_mark = "abc"
invalid_grade = grade_students(invalid_mark)

(valid_grade, invalid_grade)



def grade_students(mark):
    if mark >= 90:
        grade = 'A'
        message = 'Excellent'
    elif mark >= 80:
        grade = 'B'
        message = 'Excellent'
    elif mark >= 70:
        grade = 'C'
        message = 'Good'
    elif mark >= 60:
        grade = 'D'
        message = 'Satisfactory'
    else:
        grade = 'F'
        message = 'Needs improvement'
    
    return grade, message

# Testing the function with a mark of 78
mark = 78
grade, message = grade_students(mark)
print(f"Grade: {grade}, Message: {message}")
