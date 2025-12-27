def calculate_grade(percentage):
    if percentage >= 75:
        return "Distinction"
    elif percentage >= 60:
        return "First Class"
    elif percentage >= 50:
        return "Second Class"
    elif percentage >= 40:
        return "Pass"
    else:
        return "Fail"


# Input student details
print("----- Student Result System -----")

name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))

# Input marks
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

# Calculate total and percentage
total = sub1 + sub2 + sub3
percentage = (total / 300) * 100

# Get grade
grade = calculate_grade(percentage)

# Display result
print("\n----- Result -----")
print("Name:", name)
print("Roll No:", roll_no)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)

# Check pass or fail using loop
subjects = [sub1, sub2, sub3]
failed = False

for marks in subjects:
    if marks < 40:
        failed = True

if failed:
    print("Status: Fail (One or more subjects below 40)")
else:
    print("Status: Pass")



print("\nProgram End")

