user_input_day = input("What Is Your Birthday Day? ")
user_input_month = input("What Is Your Birthday Month? ")
user_input_year = input("What Is Your Birthday Year? ")
print(user_input_day + user_input_month + user_input_year)
user_name = input("What is your name? ")
print("Hello" + user_name)
print("4 is greater than 3")
if 4 < 3:
        print("Wow math dont work like that")
if 4 > 3:
        print("See, 4 is greater than 3")
number = input("Give Me a Number ")
number = int(number)
if number < 10:
    number = str(number)
    print(number + " is Less Than Ten")
    number = int(number)
if number == 10:
    number = str(number)
    print(number + " Equals Ten")
    number = int(number)
if number > 10:
    number = str(number)
    print(number + " Is greater than Ten")
    number = int(number)
first_name = input("What Is Yor First Name ")
if len(first_name) > 5:
    print("your name is greater than 5 letters")
if len(first_name) < 5:
    print("your name is less than 5 letters")
mark_1 = input("First Mark ")
mark_1 = int(mark_1)
mark_2 = input("Second Mark ")
mark_2 = int(mark_2)
mark_3 = input("Third Mark ")
mark_3 = int(mark_3)
mark_4 = input("Fourth Mark ")
mark_4 = int(mark_4)
average = (mark_1 + mark_2 + mark_3 + mark_4)/4
average = int(average)
if average < 50:
    average = str(average)
    print("Your average is less than 50 at" + average)
    average = int(average)
if average > 80:
    average = str(average)
    print("your average is greater than 80 at " + average)
    average = int(average)
area = 50
area = int(area)
length = input("What is the desired Length?")
length = int(length)
width = input("What is the desired width?")
width = int(width)
if (width*length) > area:
    print("your Garden Would be Too Big")
if (width*length) < area:
    print("Your Garden Would Fit")
if (width*length) == area:
    print("Your Garden Perfectly Fits")
thing = input("Give me something")
thing = int(thing)
if 0 < thing < 10:
    print(yay)w