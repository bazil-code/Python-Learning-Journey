marks = {
    "Ali": 62,
    "Sara": 88,
    "Ahmed": 55,
    "Zain": 60
}
#highest = 0
#top_student = ""

for name, score in marks.items():
    
    #if score > highest:
     #   highest = score
      #  top_student = name
      
    if score >60:
        print(f'{name} has scored above 60 with a score of= {score}')
    elif score<=60:
        print(f'{name} has scored below or equal to 60 with a score of= {score}')