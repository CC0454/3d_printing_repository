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

#this line will hold the users choices.     


def input_validation(isnumeric, error_message, input_message, end_number):
    """Return a validated input."""
    while True:
        while True:
            user_untested = input(f"{input_message}\n> ")
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
        if user_tested > end_number:
            input(f"{error_message}\n(press enter to continue)\n")
            os.system('cls')
            continue
        else:
            return user_tested


"""
This frightfully complicated function above this comment acts as input
validation for the whole code. It works by taking boolean that acts as
float or integer, the error message that needs to be printed and the
input message. It works by first off, starting a loop that will
only be broken from the return function
(when the user has inputted something valid)
It proceeds to check the boolean to see if I want to test for Floats
or Integers. After the choice is made, it tries to turn the users input into
that choice. If that dosent work, It tells the user what they did
wrong and to try again.
I understand that it isn't perfect as I test the boolean each and every
loop but the substatute for that is a different function or
Two user inputs inside of two while true loops, So im happy with it.
"""


def veiw_stats():
    counter = 1
    message_string = f""" __      __  _                       _       _                  _        _        
 \ \    / / (_)                     (_)     | |                | |      | |       
  \ \  / /__ ___      __  _ __  _ __ _ _ __ | |_ ___ _ __   ___| |_ __ _| |_ ___  
   \ \/ / _ \ \ \ /\ / / | '_ \| '__| | '_ \| __/ _ \ '__| / __| __/ _` | __/ __| 
    \  /  __/ |\ V  V /  | |_) | |  | | | | | ||  __/ |    \__ \ || (_| | |_\__ \ 
     \/ \___|_| \_/\_/   | .__/|_|  |_|_| |_|\__\___|_|    |___/\__\__,_|\__|___/ 
                         | |                                                      
                         |_|                                                     \n\nWelcome to the 3d printing company, We have three types of printers here:\n\n"""
    for i in range(0,len(main_list),2):
        message_string += f"{str(counter)}) {main_list[i]}\n"
        counter += 1

    message_string += f"\nYou can look at one of these printers and their filaments indavidually or you can press 4 to exit back to the menu. (1 to 4)"
    
    input_index = input_validation(True, "That wasn't a number on the range of 1 to 4", message_string, 4)


    filament_index, info_index = printer_stats(input_index)

    if filament_index == "True":
        print("returning")
        return
    
    filament_stats(filament_index, info_index)
    
    
def filament_stats(filament_index, info_index):
    input(f"{main_list[info_index][filament_index][0]} has a cost of {main_list[info_index][filament_index][1]} dollars per mm cubed, a time taken of {main_list[info_index][filament_index][2]} s per mm cubes and a weight of {main_list[info_index][filament_index][3]} grams per mm cubed.")
    

def printer_stats(input_index):

    counter = 1

    name_index = input_index * 2 - 2
    info_index = input_index * 2 - 1

    

    message_string = f"\n{main_list[name_index]} has {len(main_list[info_index]) - 1} types of filament and a build volume of {main_list[info_index][0][0]}mm X {main_list[info_index][0][1]}mm X {main_list[info_index][0][2]}mm.\nThe {len(main_list[info_index]) - 1} filament types are:\n"

    for i in range(1, len(main_list[info_index])):
        message_string += F"\n{counter}) {main_list[info_index][i][0]}"
        counter += 1

    message_string += f"\n\nWould you like to look into anyone of these filaments?\nPress the number correlating to the filament or press {len(main_list[info_index])} to exit this menu."

    filament_index = input_validation(True, f"That was not a number on a range of one to {len(main_list[info_index])}", message_string, len(main_list[info_index]) + 1)

    if filament_index == len(main_list[info_index]):
        return "True", info_index
    else:
        return filament_index, info_index


def veiw_prints():
    print("number 2")


def new_print():
    """I need a print name, colour and size before I move on"""
    print_string = """  _   _                 _____      _       _   
 | \ | |               |  __ \    (_)     | |  
 |  \| | _____      __ | |__) | __ _ _ __ | |_ 
 | . ` |/ _ \ \ /\ / / |  ___/ '__| | '_ \| __|
 | |\  |  __/\ V  V /  | |   | |  | | | | | |_ 
 |_| \_|\___| \_/\_/   |_|   |_|  |_|_| |_|\__|
                                               
                                               \
    \n\nWelcome to new print, what is the name of your print?\n> """

    print_name = str(input(print_string))

    print_string += f"{print_name} \nWhat colour would you like to use? (1 to {len(colours)})\n"

    for i in range(0,len(colours)):
        print_string += f"\n{i + 1}) {colours[i]}"
    
    os.system("cls")
    print(len(colours))
    input_validation(True, f"That isn't a number on a range of one to {len(colours)}", print_string, len(colours))


function_list = [
    new_print, veiw_prints, veiw_stats
 ]

"""
This line above is a list that holds a couple of functions for my menu.
 I chose to put the list below all of the defining functions because I 
 wanted to be able to call those functions from this list. 
"""

while True:

    validated_input = input_validation( True, "That isn't a number on the range of 1 to 4.", """  ____      _               _       _   _                                                            
 |___ \    | |             (_)     | | (_)                                                           
   __) | __| |   _ __  _ __ _ _ __ | |_ _ _ __   __ _     ___ ___  _ __ ___  _ __   __ _ _ __  _   _  
  |__ < / _` |  | '_ \| '__| | '_ \| __| | '_ \ / _` |   / __/ _ \| '_ ` _ \| '_ \ / _` | '_ \| | | | 
  ___) | (_| |  | |_) | |  | | | | | |_| | | | | (_| |  | (_| (_) | | | | | | |_) | (_| | | | | |_| | 
 |____/ \__,_|  | .__/|_|  |_|_| |_|\__|_|_| |_|\__, |   \___\___/|_| |_| |_| .__/ \__,_|_| |_|\__, | 
                | |                              __/ |                      | |                 __/ | 
                |_|                             |___/                       |_|                |___/ \n\nWhat would you like to do?    (1 to 4)\n1) Start a new print job\n2) Veiw your print jobs\n3) Veiw printers and their filaments\n4) Exit the program""", 4)

    validated_input -= 1

    if validated_input in range(len(function_list)):
        os.system('cls')
        function_list[validated_input]()
    else:
        break   



