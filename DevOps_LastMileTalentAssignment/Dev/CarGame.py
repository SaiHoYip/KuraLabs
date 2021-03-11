Car = True
while Car == True:
    action = input("What would you like to do? (type help for commands): ")
    if action == 'help':
        print("start: start the car")
        print("stop: stop the car")
        print("quit: quit the program")
    elif action == 'start':
        print("Car started...")
    elif action == 'stop':
        print("Car stopped...")
    elif action == 'quit':
        Car = False
    else:
        print("I don't understand")