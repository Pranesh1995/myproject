# Student Performance Analyzer

print("================================")
print("   STUDENT PERFORMANCE ANALYZER")
print("================================")

# Collect student information
name = input("Enter student name: ")

# Collect subject marks
python = float(input("Enter Python marks: "))
java = float(input("Enter Java marks: "))
statistics = float(input("Enter Statistics marks: "))
machine_learning = float(input("Enter ML marks: "))

# Calculate performance
total = python + java + statistics + machine_learning
average = total / 4
percentage = (total / 400) * 100

# Grade calculation
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "Needs Improvement"

# Display report
print("\n========== STUDENT REPORT ==========")
print("Student Name:", name)
print("Total Marks:", total, "/ 400")
print("Average:", average)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("====================================")
