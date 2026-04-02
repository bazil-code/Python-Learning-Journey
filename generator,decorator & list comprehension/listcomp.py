# 1. expression 2. for loop 3. if condition

#sqr_num = [i**2 for i in range(10)]
#print(sqr_num)

#even_num = [i for i in range(int(input("Enter a number: "))) if i%2==0 ]
#print(even_num)

# nested loop
#multiply_num = [x*y for x in [1,2,3] for y in [4,5,6]]
#print(multiply_num)

#else
list = ['a', 'b', 'c', 'd']
list_comprehension = [i if i != 'b' else 'x' for i in list]
print(list_comprehension)