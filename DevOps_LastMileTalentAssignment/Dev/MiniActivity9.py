#write a program to find the largest number in the list
numbers = [5,9,20,34,35,4,2]
largestNum = numbers[0]
for items in numbers:
    if items > largestNum:
        largestNum = items

print(largestNum)