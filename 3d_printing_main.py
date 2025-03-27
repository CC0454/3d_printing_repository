import time
import os

main_dictionary = {
    "FDM (Regular printer)": [
        [230, 250, 350],
        ["PLA", 0.5, 0.02, 1.25],
        ["ABS", 0.6, 0.03, 1.04],
        ["PETG", 0.7, 0.025, 1.27],
        ["TPU", 1.0, 0.035, 1.20]
    ],
    "SLA (Resin Printer)": [
        [150, 90, 175],
        ["Standard Resin", 1.2, 0.08, 1.10],
        ["Tough Resin", 1.5, 0.12, 1.15],
        ["Flexible Resin", 1.8, 0.15, 1.05]
    ],
    "SLS (Metal Printer)": [
        [400, 400, 400],
        ["Nylon 12", 1.0, 0.06, 1.01],
        ["TPU Powder", 1.3, 0.09, 1.12]
    ]
}

"""
This dictionary holds three 3d printers and their usable filaments.
The structure is [build volume], [Name, cost per mm, ]"
"""

colours = [
    "Red", "Blue",
    "Black", "White",
    "Green", "Yellow",
    "Purple", "Orange"
]

# This list describes the colours of the available filament


def veiw_stats():
    print("veiwing my thick dick")


def veiw_prints():
    print("looking at my fat ass")



def new_print():
    print("new homie")





def input_validation(isnumeric, error_message, input_message):
    """Return a validated input."""
    while True:
        user_untested = input(f"{input_message}\n> ")
        if isnumeric is True:
            try:
                user_tested = int(user_untested)
                return user_tested
            except ValueError:
                input(f"{error_message}\n(press enter to continue)\n")
                os.system('cls')
        else:
            try:
                user_tested = float(user_untested)
                return user_tested
            except ValueError:
                input(f"{error_message}\n(press enter to continue)\n")
                os.system('cls')


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


function_list = [new_print(), veiw_prints(), veiw_stats()]

while True:
    print("""  ____      _               _       _   _                                                            
 |___ \    | |             (_)     | | (_)                                                           
   __) | __| |   _ __  _ __ _ _ __ | |_ _ _ __   __ _     ___ ___  _ __ ___  _ __   __ _ _ __  _   _  
  |__ < / _` |  | '_ \| '__| | '_ \| __| | '_ \ / _` |   / __/ _ \| '_ ` _ \| '_ \ / _` | '_ \| | | | 
  ___) | (_| |  | |_) | |  | | | | | |_| | | | | (_| |  | (_| (_) | | | | | | |_) | (_| | | | | |_| | 
 |____/ \__,_|  | .__/|_|  |_|_| |_|\__|_|_| |_|\__, |   \___\___/|_| |_| |_| .__/ \__,_|_| |_|\__, | 
                | |                              __/ |                      | |                 __/ | 
                |_|                             |___/                       |_|                |___/ """)
    validated_input = input_validation( True, "That isn't a number on the range of 1 to 4.", "What would you like to do?    (1 to 4)\n1) Start a new print job\n2) Veiw your print jobs\n3) Veiw printers and their filaments\n4) Exit the program")
    if validated_input in len(function_list):
        function_list[validated_input]
    else:
        break
