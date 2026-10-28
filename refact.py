"""
Refactoring code means improving the structure of a program
without changing its behavior.

In simple words:
- the code still does the same task
- but it becomes easier to read, maintain, and update

Why refactor code?
- cleaner logic
- less repetition
- easier debugging
- easier teamwork
- easier future changes

Example from this project:
- default form values were grouped in one dictionary
- repeated assignments were removed
- status logic was moved into a helper function
- the app route became shorter and easier to understand

This makes the code more professional and easier to extend later.
"""

# Example of a refactored version
DEFAULT_FORM_VALUES = {
    "college_name": "Green Valley College",
    "class_start": "09:00",
    "class_end": "10:30",
    "break_start": "10:30",
    "break_end": "10:45",
    "student_text": "No message entered yet",
}


def get_status(student_text):
    if student_text and student_text.strip():
        return "Attendance sent successfully"
    return "Please enter student message"


# Example of a simple non-refactored version
# This works, but it is harder to read.
def old_way():
    college_name = "Green Valley College"
    class_start = "09:00"
    class_end = "10:30"
    break_start = "10:30"
    break_end = "10:45"
    student_text = "No message entered yet"
    status = "Waiting for attendance"

    if student_text and student_text.strip():
        status = "Attendance sent successfully"
    else:
        status = "Please enter student message"

    return college_name, class_start, class_end, break_start, break_end, student_text, status


if __name__ == "__main__":
    print("Refactoring example loaded successfully.")
    print(DEFAULT_FORM_VALUES)
    print(get_status("Student present for Java class"))
