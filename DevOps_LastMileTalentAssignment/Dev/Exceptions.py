try:
    age = int(input("Enter your age: "))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print("Age can't be zero")
except ValueError:
    print("Invalid! value must be an integar")

