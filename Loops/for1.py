#a= {1,2,3,4}
#for var_a in a:
    #print(var_a)

barca= ['messi','neymar','suarez']
arsenal= ['saka','rice', 'kai']
for x,y in zip(barca,arsenal):
    print(f'{x} vs {y}')

  # second method but a bit different  
for i in barca:
    for j in arsenal:
        print(f'{i} vs {j}')
