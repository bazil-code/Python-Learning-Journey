# enclosing function
def washingmachine():
    clothes =  'clean first then'
    def spin():
        # to modify the clothes variable in the enclosing function,  we need to use the nonlocal keyword
        #nested function
        nonlocal clothes
        clothes = 'spin the clothes'
        print(clothes)
    spin()
    print(clothes)
washingmachine()
