# searching 
#sorting

# pro 1
# input
user_input = [1,2,3,4,5,6,7,8,9,11]

# check to see if a certain number exist in the user input array
n = 2

# linnear search
result = False # a variable to keep track of your answer
for e in user_input:
    if e == n:
        result = True

if result == True:
    print('exist')
else:
    print('Not exist')
#  if else. for loops, print, calculations (+,-)

# time = 0(n)
input = [1,2,3,4,5,6,7,8,9]
for i in input:
    if i == 1: 
        continue# 0(8)
    print('hi')

    
input = [1,2,3,1,1,1]
# 0(n^2)
for i in input:
    print('hey')
for k in input:
    print('hello')

    # o(N) != n^2
    