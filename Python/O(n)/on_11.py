def rotateArray(array):
    '''
    array[-1:] taking last element
    array[:-1] taking elements from start to last second element
    array[:] changing array from starting to end
    '''
    array[:] = array[-1:]+array[:-1]
 
 
# create array
array = [1, 2, 3, 4, 5]
# send array to rotateArray function
rotateArray(array)
 
print(*array)  # 5 1 2 3 4