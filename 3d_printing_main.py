import time
import os

main_list = [
    "FDM (Regular printer)", [
        [230, 250, 350],
        ["PLA", 0.5, 0.02, 1.25],
        ["ABS", 0.6, 0.03, 1.04],
        ["PETG", 0.7, 0.025, 1.27],
        ["TPU", 1.0, 0.035, 1.20]
    ],
    "SLA (Resin Printer)", [
        [150, 90, 175],
        ["Standard Resin", 1.2, 0.08, 1.10],
        ["Tough Resin", 1.5, 0.12, 1.15],
        ["Flexible Resin", 1.8, 0.15, 1.05]
    ],
    "SLS (Metal Printer)", [
        [400, 400, 400],
        ["Nylon 12", 1.0, 0.06, 1.01],
        ["TPU Powder", 1.3, 0.09, 1.12]
    ]
]

"""
This list holds three 3d printers and their usable filaments.
The structure is [build volume], [Name, time per mm cube, cost per mm cube, weight per mm cube]"
"""

colours = [
    "Red", "Blue",
    "Black", "White",
    "Green", "Yellow",
    "Purple", "Orange"
]

# This list describes the colours of the available filament

users_list = []

# this line will hold the users choices, it is formatted: [name, color, [volume], filament].


def input_validation(isnumeric, error_message, input_message, end_number):
    """Return a validated input."""
    while True:
        # This while True statment is for the max number check
        while True:
            # This while true statment is for the check of int / float
            user_untested = input(f"{input_message}\n> ")
            # This line takes the input of the user witht the supplied message. 
            if isnumeric is True:
                try:
                    user_tested = int(user_untested)
                    break
                except ValueError:
                    input(f"{error_message}\n(press enter to continue)\n")
                    os.system('cls')
            else:
                try:
                    user_tested = float(user_untested)
                    break
                except ValueError:
                    input(f"{error_message}\n(press enter to continue)\n")
                    os.system('cls')
            """
            This if/else set first checks which data type I want to check for (int/float) then checks the users input against it.
            If they do not pass that test, the code loops back to the users input, where they are prompted to try again. 
            If they pass the test, they are allowed to continue onto the max number check with the break statment.
            """

        if user_tested > end_number:
            input(f"your number is larger than {end_number}\n(press enter to continue)\n")
            os.system('cls')
            continue
        elif user_tested <= 0:
            input("your number is equal to or less than 0, thats too small\n(press enter to continue)")
            os.system('cls')
            continue
        else:
            return user_tested
        """
        Easy enough, This is an if else statment that checks if the users inputted number is larger than a number set by me, If it is, it tells the user and loops. It also checks if the input is equal to or less than 0. If true, tells the user and loops. 
        """


def veiw_stats():
    """This define statment allows the user to view the printers and the stats of the printers."""
    counter = 1

    message_string = """ __      __  _                       _       _                  _        _        
 \ \    / / (_)                     (_)     | |                | |      | |       
  \ \  / /__ ___      __  _ __  _ __ _ _ __ | |_ ___ _ __   ___| |_ __ _| |_ ___  
   \ \/ / _ \ \ \ /\ / / | '_ \| '__| | '_ \| __/ _ \ '__| / __| __/ _` | __/ __| 
    \  /  __/ |\ V  V /  | |_) | |  | | | | | ||  __/ |    \__ \ || (_| | |_\__ \ 
     \/ \___|_| \_/\_/   | .__/|_|  |_|_| |_|\__\___|_|    |___/\__\__,_|\__|___/ 
                         | |                                                      
                         |_|                                                     \n\nWelcome to the 3d printing company, We have three types of printers here:\n\n"""
    #these lines define the counter and the start of the print string. 

    for i in range(0, len(main_list), 2):
        message_string += f"{str(counter)}) {main_list[i]}\n"
        counter += 1
    # Prints out all the printers. 

    message_string += "\nYou can look at one of these printers and their filaments indavidually or you can press 4 to exit back to the menu. (1 to 4)"
    # Adds to the message string, post for i in range.

    input_index = input_validation(True, "That wasn't a number on the range of 1 to 4", message_string, 4)
    # Pulls the input validation for the users input on each certain printer. 


    filament_index, info_index = printer_stats(input_index)
    # Sends off the data to printer stats (getting filamet index), this takes the user with it too.  

    if filament_index == "True":
        print("returning")
        return
    # Checking the returning data to see if the code should return the user to the menu or keep them going.

    filament_stats(filament_index, info_index)
    # The final print statment, takes the user to the data for their chosen filament. 


def filament_stats(filament_index, info_index):
    input(f"{main_list[info_index][filament_index][0]} has a cost of {main_list[info_index][filament_index][1]} dollars per mm cubed, a time taken of {main_list[info_index][filament_index][2]} minutes per mm cubes and a weight of {main_list[info_index][filament_index][3]} grams per mm cubed.\n(press enter to continue)")
    # Prints out data on the chosen filament. In a define statment because I thought I would have been using it again, I did not. 
    

def printer_stats(input_index):
    """Is used by my new print code to find a filament """
    counter = 1
    # Used by the code for the numbers beside each loop number, EG: 1) 2) 3).

    name_index = input_index * 2 - 2
    info_index = input_index * 2 - 1
    # A little algorithem I cooked up to allow me to find the index of the printers name and the info for that printer.

    message_string = f"\n{main_list[name_index]} has {len(main_list[info_index]) - 1} types of filament and a build volume of {main_list[info_index][0][0]}mm X {main_list[info_index][0][1]}mm X {main_list[info_index][0][2]}mm.\nThe {len(main_list[info_index]) - 1} filament types are:\n"
    """
    My dumb ass decided I would be deleting EVREYTHING when someone tiggered the input validaitons bad side. Because of that I needed evrey single line of text that was printed to be added to a message string.
    """

    for i in range(1, len(main_list[info_index])):
        message_string += F"\n{counter}) {main_list[info_index][i][0]}"
        counter += 1
    # Runs throuhgh the users prints, lets them see the names of each one they have.

    message_string += f"\n\nWould you like to look into anyone of these filaments?\nPress the number correlating to the filament or press {len(main_list[info_index])} to exit this menu."
    # Adding a little bit more to the print string before input validation.

    filament_index = input_validation(True, f"That was not a number on a range of one to {len(main_list[info_index])}", message_string, len(main_list[info_index]) + 1)
    # Input validation

    if filament_index == len(main_list[info_index]):
        return "True", info_index
    else:
        return filament_index, info_index
    """
    The other end of that cool little check in the main define statment, returns the string true if I want to return the user to the menu and
    returns the value of the filament's indes if not. really sweet.
    """


def veiw_prints():
    """Lets the user veiw the prints they have chosen.
    Only veiw though, They had a choice if they got it wrong at the end of new print."""

    if users_list == []:
        print("\nYou don't have any prints, make one then come back here to look at some stats!")
        time.sleep(3)
        os.system('cls')
        return
    # A little validaiton for if the user didn't have any prints.

    count = 1

    print_string = f"You have {len(users_list)} prints, Which one would you like to veiw?"
    # Resets the count and adds a little to the print string to start.

    for i in users_list:
        print_string += f"\n{count}) {i[0]}"
        count += 1
    # loops through the names of the users planned prints and adds them to the print list.

    print_choice = input_validation(True, f"That wasnt a number in the range of one to {len(users_list)}", print_string, len(users_list))
    print_choice -= 1
    # Validates their input and minusis one so it can be used as an index. 

    cubed_size = users_list[print_choice][2][0] * users_list[print_choice][2][1] * users_list[print_choice][2][2]
    print_cost = cubed_size * users_list[print_choice][3][2]
    print_time = cubed_size * users_list[print_choice][3][1]
    print_weight = cubed_size * users_list[print_choice][3][3]
    # Pulling the data from the print job of their choice and assigning it to varibles, ready to print, also does a little maths. 

    print_cost = int(print_cost + 1)
    print_time = int(print_time + 1)
    print_weight = int(print_weight)
    # Rounding the result of the maths via integers (I had it print out 10.0000000006 once...)

    input(f"Your print is called {users_list[print_choice][0]} and is the colour {users_list[print_choice][1]}. It's dimentions are {users_list[print_choice][2][0]} x {users_list[print_choice][2][1]} x {users_list[print_choice][2][2]}, making a total volume of {cubed_size}mm cubed.\nWith the filament you chose ({users_list[print_choice][3][0]}), this print will cost you {print_cost} dollars, take {print_time} minutes to print and weigh {print_weight} grams. ")
    # Printing the data in a formatted format (haha)


def new_print():
    """Allows the user to add a new print"""
    count = 1
    print_string = """  _   _                 _____      _       _   
 | \ | |               |  __ \    (_)     | |  
 |  \| | _____      __ | |__) | __ _ _ __ | |_ 
 | . ` |/ _ \ \ /\ / / |  ___/ '__| | '_ \| __|
 | |\  |  __/\ V  V /  | |   | |  | | | | | |_ 
 |_| \_|\___| \_/\_/   |_|   |_|  |_|_| |_|\__|
                                               
                                               \
    \nWelcome to new print, what is the name of your print?\n> """
    # Defining count and print string. 

    print_name = str(input(print_string))
    # Gets user to input their prints name, no validation needed because it's a string.

    print_string += f"{print_name} \n\nWhat colour would you like to use? (1 to {len(colours)})\n"
    # Adds the users input to the print string and asks the next question.

    for i in range(0,len(colours)):
        print_string += f"\n{i + 1}) {colours[i]}"
    # Gets the users a list of colours.

    os.system("cls")
    print_colour = input_validation(True, f"That isn't a number on a range of one to {len(colours)}", print_string, len(colours))\
    # Clearing the system and starting input validation

    print_string += f"\n> {print_colour}\n\nNow, enter the printer you want to use\n"
    # Adds the users input to the print string and asks the next question.

    for i in range(0, len(main_list), 2):
        print_string += f"\n{count}) {main_list[i]}, a print volume of ({main_list[i + 1][0][0]}, {main_list[i + 1][0][1]}, {main_list[i + 1][0][2]})mm"
        count += 1
    # Prints out the printer choices. 

    os.system('cls')
    printer_type = input_validation(True, f"That isnt a number on a range of 1 to {int(len(main_list) / 2)}", print_string, int(len(main_list) / 2))
    # Clears screen and validats input

    info_index = printer_type * 2 - 1
    # Finds the index of the info for that printer

    print_string += f">{printer_type}\n\nNow, choose the filament, enter a number on a range of one to {len(main_list[info_index])- 1} to choose" 
    # Adds the users input to the print string and asks the next question.

    for i in range(1, len(main_list[info_index])):
        print_string += f"\n\n{i}) {main_list[info_index][i][0]}:\n   It has a cost of {main_list[info_index][i][1]} dollars per mm cubed, a time taken of {main_list[info_index][i][2]} minutes per mm cubed and weighs {main_list[info_index][i][3]} grams per mm cubed."
    # loops through the filaments and prints them out for the user.     

    os.system('cls')
    filament_temp = input_validation(True, f"That wasnt a number on the range of 1 to {len(main_list[info_index]) - 1}", print_string, len(main_list[info_index]) - 1)
    # Clears screen and goes for input of the filament. 
    
    print_string += f"\n> {filament_temp}\n\nNow it's time to choose the size of the print, the 3d printer you chose has a build size of {main_list[info_index][0][0]} deep, {main_list[info_index][0][1]} wide and {main_list[info_index][0][2]} tall:\n\nEnter the depth"
        # Adds the users input to the print string and asks the next question.

    os.system("cls")
    depth = input_validation(True, "that wasnt a number or your number was too large, try again", print_string, main_list[info_index][0][0])

    print_string += f"\n> {depth}\nEnter the width"

    os.system("cls")
    width = input_validation(True, "that wasnt a number or your number was too large, try again", print_string, main_list[info_index][0][1])

    print_string += f"\n> {width}\nEnter the Height"

    os.system("cls")
    height = input_validation(True, "that wasnt a number or your number was too large, try again", print_string, main_list[info_index][0][2])
    # Gets input for depth, width and height of the print and adds to the print string accordignly. 

    print_string += f"\n> {height}"
    # Adds to the print string.

    filament = main_list[info_index][filament_temp]
    user_dimentions = [depth, width, height]
    user_colour = colours[print_colour - 1]
    users_list.append([print_name, user_colour, user_dimentions, filament])
    # Prepears some varibles for the final print. 

    os.system('cls')
    while True:
        user_input = input(f"\nYour print is called {users_list[len(users_list) - 1][0]}, is the colour {users_list[len(users_list) - 1][1]} and is the dimentions ({users_list[len(users_list) - 1][2][0]}, {users_list[len(users_list) - 1][2][1]}, {users_list[len(users_list) - 1][2][2]})\nAditionally, you chose {users_list[len(users_list) - 1][3][0]} for your filament.\n\nIs this all correct? (y / n)\n> ")
        # Takes input on weather the data is correct or not. 

        if user_input == "y" or user_input == "Y":
            print("perfect, saving the data and returning to the home screen now")
            time.sleep(3)
            os.system('cls')
            break
        elif user_input == "n" or user_input == "N":
            print("Ok, deleting data and retuning to menu now")
            time.sleep(3)
            users_list.pop(len(users_list) - 1)
            break
        else:
            input("That wasn't y or n, please try again\n(press enter to continue)")
            os.system('cls')
        # Checks the data, if correct, exits the program, if not, pops the data and exits.


function_list = [
    new_print, veiw_prints, veiw_stats
 ]

"""
This line above is a list that holds a couple of functions for my menu.
 I chose to put the list below all of the defining functions because I 
 wanted to be able to call those functions from this list. 
"""

while True:
    os.system('cls')
    validated_input = input_validation( True, "That isn't a number on the range of 1 to 4.", """  ____      _               _       _   _                                                            
 |___ \    | |             (_)     | | (_)                                                           
   __) | __| |   _ __  _ __ _ _ __ | |_ _ _ __   __ _     ___ ___  _ __ ___  _ __   __ _ _ __  _   _  
  |__ < / _` |  | '_ \| '__| | '_ \| __| | '_ \ / _` |   / __/ _ \| '_ ` _ \| '_ \ / _` | '_ \| | | | 
  ___) | (_| |  | |_) | |  | | | | | |_| | | | | (_| |  | (_| (_) | | | | | | |_) | (_| | | | | |_| | 
 |____/ \__,_|  | .__/|_|  |_|_| |_|\__|_|_| |_|\__, |   \___\___/|_| |_| |_| .__/ \__,_|_| |_|\__, | 
                | |                              __/ |                      | |                 __/ | 
                |_|                             |___/                       |_|                |___/ \n\nWhat would you like to do?    (1 to 4)\n1) Start a new print job\n2) Veiw your print jobs\n3) Veiw printers and their filaments\n4) Exit the program""", 4)
    # Takes input and validates it

    validated_input -= 1
    # Minuses 1 from the input to make it useful for index.

    if validated_input in range(len(function_list)):
        os.system('cls')
        function_list[validated_input]()
    else:
        break   
    """
    Chooses which function to send the user to in accordance to the input, The max input is set to four so if it's not 1, 2 or 3 itll be four and break
    """
    