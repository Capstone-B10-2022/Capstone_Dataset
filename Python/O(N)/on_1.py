'''
Source: https://www.geeksforgeeks.org/time-complexity-and-space-complexity/#:~:text=Time%20Complexity%3A%20The%20time%20complexity,the%20algorithm%20is%20running%20on.

'''

count = 0
n = 2
i = n
while(i > 0):
  for j in range(i):
    count+=1
  i = i / 2
  i = int(i)
