#Group 4 Solution to CCC  2014 J5
# The problem is made easy because the input lines
# are guaranteed to have N DIFFERENT names, so no checks
# for duplicates or missing names need occur and the second
# line has the SAME names as the first, so no checks needed
# for 'not found' conditions.
# for each position i, it must be the case that
# first [i] = second[position in first of second[i]]
# (ie. a to b is also b to a)
# and that position in first of second[i] not = i
# (ie. a to a is not the case)

#while loop to loop program
x=1
while x==1:
    #Next two lines define empty lists
    first1=[]
    second1=[]
    #first input statment which sets the value for variable 'n'
    n= int(input("Please enter the number of children in your class between 1 and 30: "))
    #troubleshooting statement to ensure only a number greater than 1 and less than or equal to 30. If the parameters are not met, the input statment is reprinted.
    if n<1 and n>30:
        n= int(input("Invalid Entry. Please enter the number of children in your class between 1 and 30: "))
    #lets user input list of names to enter in to 'first' list
    first= input("Please enter the names of the children in your class in a random order. Seperate your entries by commas. Make sure to enter the same number of children: ")
    #appends the input from previous line to the empty list 'first'
    first1.append(first)
    #lets user input list of names to enter in to 'second' list
    second= input("Please enter the names of the children in your class in another random order. Seperate your entries by commas.  Make sure to enter the same number of children: ")
    #appends the input from previous line to the empty list 'second'
    second1.append(second)
    #sets variable 'state' to string 'good'
    state = "good"
    #sets variable 'i' to string 0
    i=0
    while i < n and state == "good":
    #bottom line: takes the index value of 'i' from the second list, then inputs it into the '.index(obj)' method. The resulting value is set as the value for the variable position
        position = first.index(second[i])
        # this 'if' statement compares the index position (set by variable 'i') to the index postion of the second list (set by variable 'position'). If the two values
        #do not equal each other or if the value of 'position' equals the value of 'i'
        if first[i] != second[position] or position == i:
        #if the above statements are 'true' the variable 'state' is overwritten with the string 'bad'
            state = "bad"
        #this next line of code is very important because this line allows the if statement to cycle through all the index numbers until the parameters
            #defined in the 'if' statements are 'true'
        i = i + 1

    #This print statment provides the final output and tells the user whether or not the pairs they have inputted are 'good' or 'bad'
        
    print ("Your student pairs are: "+ str(state))

    
    
