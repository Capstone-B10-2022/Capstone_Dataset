def rotateArray(array):
    
    array[:] = array[-1:]+array[:-1]
 
 
# create array
array = [1, 2, 3, 4, 5]
# send array to rotateArray function
rotateArray(array)
 
print(*array)  # 5 1 2 3 4