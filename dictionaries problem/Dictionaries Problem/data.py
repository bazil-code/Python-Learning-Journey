#numbers = {1:1, 2:4, 3:9, 4:16, 5:25}
#for key, value in numbers.items():
    #print(f"The square of {key} is {value}")

data = {
    "a": 1,
    "b": 2,
    "c": 3
}

reverse = {}
for key, value in data.items():
    reverse[value] = key
print(reverse)
