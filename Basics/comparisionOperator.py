#COMPARISION OPERATORS 
a=1
b=4
print(a==b)

#LOGICAL OPERATORS AND OR
print(a>b and a!=b)
print(a>b or a!=b)

#IDENTITY OPERATOR IS , IS NOT
print(a<b is a!=b)
print(a<b is not a!=b)

a=[1,2,3]
b=[1,2,3]  # IN LIST ID IS DIFF
print(id(a))
print(id(b))


#membership operators in, not in
x = 3
y = [1, 2, 3, 4, 5]

print(x in y)

numbers = [1, 2, 3, 4, 5]                #Example with a list
data = {"name": "Ali", "age": 20}        #Example with a dictionary
text = "hello world"                     #Example with a string

print("helo" in text)     #false
print("bye" not in text)   #True

print(6 in numbers)      #False
print(6 not in numbers)  #True

print("name" in data)      #True (checks keys)
print("Ali" in data)       #False (values not checked)