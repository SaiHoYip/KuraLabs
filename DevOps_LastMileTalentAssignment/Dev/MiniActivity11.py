phoneNum = input("PhoneNum: ")
digits = {
    "1": "One", #dictionaries
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}
Number = ""
for char in phoneNum:
    #Number += digits[char]
    #or use the .get(char) method
    Number+= digits.get(char, "!")
print(Number)