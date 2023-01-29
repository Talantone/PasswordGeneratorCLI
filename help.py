from colorama import Fore, Style
help_str = """
Commands:
    generate <symbols>
    exit
    You can also type help <command> to get a little more info"""

generate_str = """Command:
    generate <symbols>
    """ + Fore.RED + """NOTE: Symbols must be written in one word""" + Style.RESET_ALL

exit_str = """This will stop the program."""


help_strings = {
    "generate": generate_str,
    "exit": exit_str,
    "help": help_str
}


def help_command(command=None):
    if command is None:
        command = "help"

    try:
        print(help_strings[command])
    except KeyError:
        print("This command doesn't exist")
