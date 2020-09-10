listOfFive = [11,2,3,4,-111]
min = listOfFive[0] 
for i in range(len(listOfFive)):
    if min > listOfFive[i]:
        min = listOfFive[i]

print ("The minimum number is:",min)
