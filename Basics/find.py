even=range(0,20,2)
odd=range(1,20,2)
print(list(even))
print(list(odd))

list_find= list(range(2,20,2))
num= int(input('enter the number:'))
if num in list_find:
    print(f'{num} is divisible by 2: {num in list_find}')
else:
    print(f'{num} is not divisible by 2: {num in list_find}')
