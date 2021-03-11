#write a program to remove duplicates in a list
numbers = [10,9,6,6,5,4,4,9]
uniqueNums = []
for i in numbers:
    if i not in uniqueNums:
        uniqueNums.append(i)
print(uniqueNums)
