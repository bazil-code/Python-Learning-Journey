marks ={
    "physics": 85,
    "chemistry": 90,
    "math": 96
}
total_marks= 0
for subject, mark in marks.items():
    total_marks += mark
print("Total marks:", total_marks)