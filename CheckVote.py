# ! check if user can vote
# Check if the user can vote
# get user age from input
#convert if userinput(str) to int() to number
#check if user can vote
        # if else statement
        # if above 18 print ('You can Vote')
        # if below 18 print ('You cant Vote')

# Get user input
userinput = input('Please enter your Name: ')
Your_Name = str(userinput)
print('Your Name is',(Your_Name))


userinput = input('Please type your age: ')
Your_age = int(userinput)

if Your_age > 18:
    print('You Can Vote')
elif Your_age < 18:
    print('You Cant Vote')

