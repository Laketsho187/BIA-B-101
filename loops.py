# loop over an array
fruits = ['a', 'b', 'c']

# lopp through each element 
# at each stage, if the elemnt is 'c'
# print true
for e in fruits: #1.e = 'a', 2,e = 'b' , 3.e = 'c'
    if e == 'c':
        print('True from c')
    if e == 'b':
        print('True from b')

## Iterate over a string
greeting = "Hello"
for char in greeting:
    print(char)

# iterate over a range
for i in range(9):
    #print(i)  # Output :  5 6 7 8 9 10 11 12 13 
    val = i + 5
    print(val)

for i in range(5, 14, 2):
    print(i)


#! While Loops 
# Basic while loop
    
count = 0
while count < 5:
    print(count)
    count = count + 1 # Output: 0 1 2 3 4 

# user input string is unknown
# print every char of the string
s = 'helloabc'
counter = 0
length_s = len(s)
print('counter:', counter)
print('len s ', length_s)
# output 0, 1, 2, 3, 

print('going in loop')
while counter < length_s:
    print('counter:', counter)
    char = s[1]
    print(char)
    counter = counter + 1
    print('------')