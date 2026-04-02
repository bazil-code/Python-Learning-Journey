available_exit = ['east', 'west', 'south', 'north']
chosen_exit = " "
while chosen_exit not in available_exit:
    chosen_exit = input("Please choose a direction to exit: ")
    if chosen_exit == "east":
        print("You have escaped the maze!")
        print("Congratulations!")
        break
    else:
        print("You cannot exit that way. Please choose another direction.")