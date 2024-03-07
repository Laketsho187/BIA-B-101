# objective
# Create a program that takes in user input
# determine if the number is positive or negative
# print 'ur number id positive' or 'ur number is negative'

# If else
# print()
# input()

# 3 minutes

# break down the problem
# Take in user input
        # Check the Type of the input
        # if the type is string, how  do you convert it to an int?
2. # check if the number is positive or negative or zero
        #need to use if else statement
        # ! a == b (is it equal to)
        # ! a != b (Not equal to)
        # ypu will be comparing numbers and not string
# Print the result

# Solution
# Get user input
userinput = input()

userInputType = type(userinput)
print('The type of user input is:', userinput)

userInputNumber = float(userinput)
print('The type of userInputNumber is:', type(userInputNumber))

#2,3    If else statement and print
if userInputNumber >0:
    print('The number is positive')
elif userInputNumber <0:
    print('The number is Negative')
elif userInputNumber ==0:
    print('The number is zero')