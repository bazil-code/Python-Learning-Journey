num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
num3 = float(input("enter third number: "))
if num1 > num2 and num1 > num3:
    print (f'{num1} is the largest num')
elif num2 > num1 and num2 > num3:
    print (f'{num2} is the largest num')
elif num3 > num1 and num3 > num2:
    print (f'{num3} is the largest num')
else:
    print("All numbers are equal")