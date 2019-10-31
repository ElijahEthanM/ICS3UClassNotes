import math
speed = input("how fast is the car going")  # a simple input to determine the speed of the car
running = 0  # used multiple times, this variable is used to create a while loop mostly to check if the value
# given is incorrect
while running == 0:  # This is the while loop that makes sure the speed of the care is a readable and usable number
    if not speed.isdigit():
        print("Please give the speed of the car in a number")
        speed = (input("how fast is the car going"))
    elif int(speed) < 0:
        print("the car cannot go negative speeds")
        speed = (input("how fast is the car going"))
    else:
        running = 1
if int(speed) <= 50:  # each of these is used to determine the fine received for going to fast and reading
    # the speed back out to you
    print("you are going at a safe speed")
elif 50 <= int(speed) <= 71:
    speed = int(int(speed) - 50)
    print("you are going over the speed limit by")
    print(speed)
    print("Khm and have been fined 45 dollars")
elif 71 <= int(speed) <= 80:
    speed = int(int(speed) - 50)
    print("you are going over the speed limit by")
    print(speed)
    print("Khm and have been fined a total of 75 dollars")
elif 81 <= int(speed):
    print("you are well over the speeding limit at")
    speed = int(int(speed) - 50)
    print(speed)
    print("Khm and have been fined 150 dollars")
running = 0
group = 0
for x in range(0, 6):  # Repeating 6 times, asking for a w or an l, and
    # updating the database for which group to be put in each time a w is read
    game = input("Win or Loss (W or L)")
    while running == 0:
        if game.isdigit():  # Again, this will show up multiple times, it is to make sure the input is
            # readable by the code
            print("Please give the value in capital W or L")
            game = input("Win or Loss (W or L)")
        else:
            running = 1
    if game == "W":
        group = group + 1
    if game == "w":
        group = group + 1
if group >= 5:  # The group definitions, being the number of wins required
    print("you are placed into group one")
elif 2 < group < 5:
    print("you are placed into group two")
elif 0 < group < 3:
    print("you are placed into group three")
else:
    print("you were knocked out with zero wins")

average = 0
running = 0
subjects = (input("How many classes do you take?"))  # determines the number of subjects , which then determines
# how many times a command will repeat
while running == 0:  # defensive coding again
    if int(subjects) > 8:
        print("That is just false, you take 5-8")
        subjects = (input("How many Classes do you take"))
    elif int(subjects) < 5:
        print("That is just false, you take 5-8")
        subjects = (input("How many Classes do you take"))
    elif not subjects.isdigit():
        print("That is just false, you take a number of courses from 5-8")
        subjects = (input("How many Classes do you take"))
    else:
        running = 1
running = 0
for i in range(0, int(subjects)):  # the number of times the the statement asking for the marks in classes will be
    marks = (input("What was your mark in a class"))  # asks for the marks
    running = 0
    while running == 0:  # again, the programming to try and prevent the toddler to
        # slam the keyboard and miss input a value
        if not subjects.isdigit:
            print("Please give the mark in a value from 1-100 and not a number")
            marks = (input("What was your mark in a class"))
        elif int(marks) > 100:
            print("Please give a number between 1-100")
            marks = (input("What was your mark in a class"))
        elif int(marks) < 0:
            print("Please give a number between 1-100")
            marks = (input("What was your mark in a class"))
        else:
            running = 1
    average = int(average + int(marks))  # the calculations demeriting the average of the marks imputed
    average = int(average / int(subjects))
    if int(average) > 79.5:  # code checking to see if the average is the min to receive the award
        print("You have received the Principal's Award!")
    else:
        print("so close, next year you will get it")
cookies = (input("How many cookies over 200 are being made?"))  # cookies command, determining
# how many over 200 being made
running = 0
while running == 0:  # again, the programming to try and prevent the toddler to slam the keyboard and miss input a value
    if not cookies.isdigit():
        print("You cant have lettered cookies")
        cookies = (input("How many cookies over 200 are being made?"))
    else:
        running = 1
if int(cookies) < 0:  # again, the programming to try and prevent the toddler to slam the
    # keyboard and miss input a value
    print("No Cookies below zero")
    cookies = (input("How many cookies over 200 are being made?"))
cookies = int(int(cookies) + 200)  # all of these are the mathematical equation to update cookies and
# determine how many crates and boxes and cookies you will have.
crates = int(cookies % (20 * 12))
cookies = int(cookies / (20 * 12))
boxes = int(cookies / 12)
cookies = int(cookies % 12)
if crates > 0:  # if commands to determine and print how many items you have in total, if they are above zero
    print("you have this many crates")
    print(crates)
else:
    print("you made no crates")
if boxes > 0:
    print("you have these many boxes")
    print(boxes)
else:
    print("you made no boxes")
if cookies > 0:
    print("You have this many cookies")
    print(cookies)
else:
    print("you have no more cookies")
money = (crates * 80) + (boxes * 12) + (cookies * 0.5)  # checks the money you will make and prints it
print("your total money is")
print(money)
running = 0
while running == 0:
    mode = (input(  # the command to determine which mode of the menu you want, as well as being looped
        # to keep the menu open
        "if you want hypotenuse press H, if you want Tip calculator press T, if you want temperature changer press C"))
    running1 = 0
    while running1 == 0:  # again, the programming to try and prevent the toddler to
        # slam the keyboard and miss input a value
        if mode.isdigit():
            print("Please input the proper indicators")
            mode = str(input(
                "if you want hypotenuse press H, if you want Tip calculator press T, if you want temperature changer "
                "press C"))
        if mode == "H" or mode == "h":  # checks the mode, and determines the command needed
            running1 = 0
            a = (input("Give me a"))  # asks for the values of a and b, and then.....
            while running1 == 0:
                if not a.isdigit():  # more defensive coding
                    a = input("please give a valid number")
                else:
                    running1 = 1
            b = (input("Give me b"))
            running1 = 0
            while running1 == 0:  # even more defensive coding
                if not b.isdigit():
                    b = input("please give a valid number")
                else:
                    running1 = 1
            c = int((a * int(a))) + int((b * int(b)))  # the mathematical formula to create the
            # value of c to the power of 2, the reason is for the ints to to try and prevent the children
            # from miss imputing
            c = math.sqrt(c)  # square roots to find the true value of c, and then prints the value
            print("The hypotenuse is")
            print(round(c), 2)  # rounds the decimal places to the nearest 2nd
            running = input("If you want to continue press 0 if not, press any number")  # the command to either stop
            # or to continue
        elif mode == "T" or mode == "t":  # checks the mode, and determines the command needed
            money = input("Give me the value of the bill")  # asks for the value of the bill
            tip = (input("What is the tip percentage"))  # asks for the value of the tip
            tip = int(int(money) * int(tip)/100)  # mathematically calculates the tip value and then prints that value
            print("The value of the tip is")
            print(tip)
            running = input("If you want to continue press 0 if not, press any number")  # stop command
        elif mode == "C" or mode == "c":  # checks the mode, and determines the command needed
            mode2 = (input("Type 1 of Celsius to Fahrenheit, 2 for Fahrenheit to Celsius"))
            # checks the mode, and determines the command needed
            running1 = 0
            while running1 == 0:
                if not mode2 == 1 or mode2 == 2:
                    mode2 = input("Please give 1 for c to f, to for f to c")
                elif not mode2.isdigit:
                    mode2 = input("Please give 1 for c to f, to for f to c")
                else:
                    running1 = 1
            if mode2 == 1:  # option one
                tempC = (input("Give me the temperature in C"))  # asks for temp in c, and then converts it into F
                running = 0
                while running1 == 0:
                    if not tempC.isdigit:  # defensive coding
                        tempC = (input("Please give the temperature in Celsius"))
                    else:
                        running1 = 1
                tempF = int((1.8 * int(tempC)) + 32)  # math equation to determine, then prints the value
                print("the temperature in Fahrenheit is")
                print(tempF)
                running = input("If you want to continue press 0 if not, press any number")
            if mode == 2:  # option 2
                tempF = (input('Give me the temperature in Fahrenheit')) # F to C
                while running1 == 0:
                    if not tempF.isdigit:  # defensive coding
                        tempC = (input("Please give the temperature in a number"))
                    else:
                        running1 = 1
                tempC = int((int(tempF) + 32) * 1.8)  # math equation to determine the value in C, then prints it
                print("The temperature in Celsius is")
                print(tempC)
