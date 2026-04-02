marks= int(input("Enter the marks: "))
if marks >= 0 and marks <= 100:
    if marks >= 80:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 65:
        print("Grade C")
    elif marks >= 55:
        print("Grade D")
    else:
        print("Grade F")
else:
    print("Invalid input. Please enter a valid mark between 0 and 100.")