command=""
is_car_started = False
while True:
    command=input('>').lower()
    if command=='start':
        if is_car_started == True:
            print("Car started already")
        else:
            is_car_started = True
            print("Car started")
    elif command=='stop':
         is_car_started = False
         print("Car stopped")
    elif command=="help":
        print('''
start-to start the car
stop-to stop the car
quit-to exit
        ''')
    elif command=='quit':
        break
    else:
        print("I don't understand that")

