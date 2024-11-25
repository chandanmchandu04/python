score = 90

if score >= 101:
    print("please verify your marks to check the grade")
    exit()

if score >= 90:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "F"

print("grade: ", grade)