import array
import random

from help import help_command


DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

LOWERCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']

UPPERCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

COMBINED_LIST = DIGITS + LOWERCASE_CHARACTERS + UPPERCASE_CHARACTERS + SYMBOLS

command_list = ["generate", "help", "exit"]
command_requirements = {
    "generate": 2,
    "help": 1
}


def generate(symbols):
    """Generates password from user symbols and added random symbols"""
    temp_pass = random.choice(DIGITS) + random.choice(UPPERCASE_CHARACTERS) + random.choice(LOWERCASE_CHARACTERS) + random.choice(SYMBOLS)
    temp_pass += symbols
    while len(temp_pass) < 8:
        temp_pass += random.choice(COMBINED_LIST)
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
    password = ""
    for x in temp_pass_list:
        password += x
    print(password)


def execute(command):
    """Executes commands from list"""
    if len(command) > 0 and command[0] in command_list:
        if len(command) < command_requirements[command[0]]:
            print("More information required to execute the given command")
            print(f"Type help or help {command[0]} for more information")
        else:
            match command[0]:
                case "generate":
                    generate(command[1])
                case "help":
                    try:
                        help_command(command[1])
                    except IndexError:
                        help_command()
    else:
        print("Invalid command")


def main():
    while True:
        command_input = input("--> ").strip().split()
        if command_input[0] == "exit":
            verify = input("Are you sure you want to leave (Y|N) :")
            if verify[0].strip().lower() == 'y':
                break
        execute(command_input)


if __name__ == '__main__':
    print('Write "help" to show a list of commands')
    main()
