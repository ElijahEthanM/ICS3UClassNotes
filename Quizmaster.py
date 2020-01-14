import time, random # imports required to use certain features
hispoint = 0 # different variables to be used in the program
geopoint = 0
quit_input = 0
tracker = 0
try: # creating files to be used in the program, if already made it does not create them again and tests for the error
    high_g = open("geo_score", "x")
    high_h = open("history_score", "x")
    f = open("geo_questions.txt", "x")
    r = open("geo_ans.txt", "x")
    h = open("History_ans.txt", "x")
    g = open("History_questions.txt", "x")
    f.close()
    r.close()
    h.close()
    g.close()
    high_g.close()
    high_h.close()
except FileExistsError:
    print("files already created!")
# f = open("geo_questions.txt", "w")
# r = open("geo_ans.txt", "w")
# h = open("History_ans.txt", "w")
# g = open("History_questions.txt", "w")
# r.write("port moresby\n5\n7\nitaly\nseoul\n54\n50\n10\nhargeisa\n44\n7")
# f.write("What is the Capital of Papua New Guinea?\nHow many oceans are there?\nWhat country is mount vesuvius in?"
#         "\nWhat is the Capitol of South Korea?\nHow many counties are in Africa?\nHow many states are in the USA?\n"
#         "How many provinces are in Canada\nWhat is the capital of Somaliland?\nHow many counties are in europe?"
#         "\nHow many continents are there?")
# g.write("What year was the declaration of Independence signed?\nWhat year was the start of the American Civil War?\n"
#         "What was the name of the Roman emperor who was assassinated in his courtroom by his subjects?\n"
#         "What year did George Washington die?\nWhen did the Qing dynasty end?\nWhat year did the war of 1812 end in?"
#         "\n"
#         "What was George Washington’s role in the American Revolution?\nwhat year did mount Saint Helens erupt?\n"
#         "What year did genghis khan die in?\nwhen did the babylonian empire end?")
# h.write("1776\n1861\njulius caesar\n1799\n1912\n1812\ngeneral\n2008\n1227\n539bce")
# f.close()
# r.close()
# h.close()
# g.close()
user_input = str(input("Would You like to play trivia?"))
user_mode = 0
x = 0
while x == 0:
    if user_input == "yes":
        geopoint = 0
        hispoint = 0
        user_mode = str(input("Would you like to play history or geography trivia?")).lower()
        if user_mode == "geography":
            tracker = 0
            time.sleep(0.3)
            print("     ▄█    ▄████████  ▄██████▄      ▄███████▄     ▄████████  ████████▄   ▄██   ▄   ")
            time.sleep(0.3)
            print("    ███   ███    ███ ███    ███    ███    ███    ███    ███  ███   ▀███  ███   ██▄ ")
            time.sleep(0.3)
            print("    ███   ███    █▀  ███    ███    ███    ███    ███    ███  ███    ███  ███▄▄▄███ ")
            time.sleep(0.3)
            print("    ███  ▄███▄▄▄     ███    ███    ███    ███   ▄███▄▄▄▄██▀  ███    ███  ▀▀▀▀▀▀███ ")
            time.sleep(0.3)
            print("    ███ ▀▀███▀▀▀     ███    ███   ▀████████▀   ▀▀███▀▀▀▀▀    ███    ███  ▄██   ███ ")
            time.sleep(0.3)
            print("    ███   ███    █▄  ███    ███    ███         ▀███████████  ███    ███  ███   ███ ")
            time.sleep(0.3)
            print("    ███   ███    ███ ███    ███    ███           ███    ███  ███   ▄███  ███   ███ ")
            time.sleep(0.3)
            print("█▄ ▄███   ██████████  ▀██████▀    ▄████▀         ███    ███  ████████▀    ▀█████▀  ")
            time.sleep(0.3)
            print("▀▀▀▀▀▀")
            time.sleep(0.3)
            try:
                f = open("geo_questions.txt", "r")
                r = open("geo_ans.txt", "r")
                h = open("History_ans.txt", "r")
                g = open("History_questions.txt", "r")
                question_geography = open("geo_questions.txt", "r")
                answers_geography = open('geo_ans.txt', "r")
                gqs = question_geography.readlines()
                gans = answers_geography.readlines()
                geo_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                random.shuffle(geo_list)
                for i in geo_list:
                    gq = input(gqs[i])
                    gq = gq.lower()
                    tracker = tracker + 1
                    if gq == gans[i].strip():
                        time.sleep(0.3)
                        print("\nThat is Correct!\n")
                        geopoint = geopoint + 1
                        print("\nyou have " + str(geopoint) + " point\n")
                    else:
                        time.sleep(0.5)
                        print("\nThat is incorrect\n")
                    if tracker == 10:
                        high_g = open("history_score", "r")
                        temp = str(high_g.readlines(1))
                        if temp >= str(geopoint):
                            print("You have not broken your highscore! So close though!")
                        elif temp <= str(geopoint):
                            high_h.write(geopoint)
            except IOError:
                print("File for Questions and answers were not found")
        if user_mode == "history":
            tracker = 0
            time.sleep(0.3)
            print("     ▄█    ▄████████  ▄██████▄      ▄███████▄     ▄████████  ████████▄   ▄██   ▄   ")
            time.sleep(0.3)
            print("    ███   ███    ███ ███    ███    ███    ███    ███    ███  ███   ▀███  ███   ██▄ ")
            time.sleep(0.3)
            print("    ███   ███    █▀  ███    ███    ███    ███    ███    ███  ███    ███  ███▄▄▄███ ")
            time.sleep(0.3)
            print("    ███  ▄███▄▄▄     ███    ███    ███    ███   ▄███▄▄▄▄██▀  ███    ███  ▀▀▀▀▀▀███ ")
            time.sleep(0.3)
            print("    ███ ▀▀███▀▀▀     ███    ███   ▀████████▀   ▀▀███▀▀▀▀▀    ███    ███  ▄██   ███ ")
            time.sleep(0.3)
            print("    ███   ███    █▄  ███    ███    ███         ▀███████████  ███    ███  ███   ███ ")
            time.sleep(0.3)
            print("    ███   ███    ███ ███    ███    ███           ███    ███  ███   ▄███  ███   ███ ")
            time.sleep(0.3)
            print("█▄ ▄███   ██████████  ▀██████▀    ▄████▀         ███    ███  ████████▀    ▀█████▀  ")
            time.sleep(0.3)
            print("▀▀▀▀▀▀")
            time.sleep(0.3)
            try:
                f = open("geo_questions.txt", "r")
                r = open("geo_ans.txt", "r")
                h = open("History_ans.txt", "r")
                g = open("History_questions.txt", "r")
                question_history = open("History_questions.txt", "r")
                answers_history = open('History_ans.txt', "r")
                hqs = question_history.readlines()
                hans = answers_history.readlines()
                his_list = [0,1,2,3,4,5,6,7,8,9]
                random.shuffle(his_list)
                for i in his_list:
                    hq = input(hqs[i])
                    hq = hq.lower()
                    if hq == hans[i].strip():
                        time.sleep(0.3)
                        print("\nThat is Correct!\n")
                        hispoint = hispoint + 1
                        print("\nyou have " + str(hispoint) + " point\n")
                        if tracker == 10:
                                high_h = open("history_score", "r")
                                temp = str(high_h.readlines(1))
                                if temp >= str(hispoint):
                                    print("You have not broken your highscore! So close though!")
                                elif temp <= str(hispoint):
                                    high_h.write(hispoint)
                    else:
                        time.sleep(0.5)
                        print("\nThat is incorrect\n")
            except IOError:
                print("File for Questions and answers were not found")
        else:
            print("That is not a valid input")
            user_input = str(input("Would you like to play trivia?"))
    elif user_input == "no":
        quit_input = str(input("Are you sure you want to quit?")).lower()
        if quit_input == "yes":
            x = 1
            print("See you around!")
        elif quit_input == "no":
            user_input = "yes"
        else:
            print("\n That is not a valid input")
    else:
        print("That is not a valid answer")
        user_input = str(input("Would You like to play trivia?"))
