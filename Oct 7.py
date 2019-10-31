guess = input("Give me a number")
guess = int(guess)
if guess == 6:
    print("you guessed the correct number")
else:
    print("Wrong Number!")
print("You arrive at a fork in the road with 3 paths, left forward and right, which way do you go")
direction = str(input("which way do you go?"))
if direction == "go left":
    print("you fall into a river and die")
if direction == "go right":
    print("You stumble into a dragons cave. leave or go deeper")
    question = str(input("Which way to go"))
    if question == "deeper":
        print("you stumble into the dragon and are turned into a crispy snack")
    if question == "go back":
        print("you trip on a rock and smash your head and are stolen by goblins")
if direction == "go forward":
    print("you forgot you were a wanted fugitive and are arrested and hanged for burning down an orphange")
if direction == "go back":
    print("you go home to where you know it is safe")

count = 0
count = int(count)
while count <= 20:
    print(count)
    count = count+1

count = 0
count = int(count)
while count <= 20:
    print(count)
    count = count+2

xyear = int(input("give me a year"))
if xyear < 1967:
    print("to long ago")
yyear = int(input("give me another year greater than the last"))
if yyear == xyear:
    print("Thats not possilbe")
if yyear > xyear:
    print("the leafs did not win in " + str(xyear) + "but will win in" + str(yyear))
if yyear < xyear:
    print("you didnt listen")

num = int(input("Give me a number"))
while num != 0:
    print(str(num))
    num = num-1

word = str(input("Give me a word"))
repeat = int(len(word))
while repeat > 0:
    print(word)
    repeat = repeat-1