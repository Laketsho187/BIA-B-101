# Creation of array
array1 = [1,2,3, "thimphu", 2.5]
print(array1)

# retreiving
element1 = array1[0]
element2 = array1[4]
last_elements= array1[-1]

print(last_elements)

#modifying elements
array1[0] = 10
print(array1)

# getting number of elements in an array
no_of_elements = len(array1)
print(no_of_elements)

# slicing 
elements = array1[0:2]
print(elements)

arr1 = [1, 10]
arr2 = ['thimphu', 'wangdue']

number_to_check = 2
result = number_to_check in arr1
print('result is', result)

arr3 = arr2 + arr1
print(arr3)

arrVariable = [1,3,2]
arrVariable.append(4) # [1,3,2,4]
print(arrVariable)

#insert at a specific index
arrVariable.insert(1,10) # [1,10,3,2,4]
print(arrVariable)

stackVar = []
# adding an elements to the stack
stackVar.append(4)
stackVar.append(2)
stackVar.append(9)
stackVar.append(1) # [9,2,9,1]
print('After appending', stackVar)

element = stackVar.pop()
print('After popping', stackVar)
print('Remove element', element)