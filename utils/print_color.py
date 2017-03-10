ansi_reset = '\033[0m'
ansi_black = '\033[30m'
ansi_red = '\033[31m'
ansi_green = '\033[1;32m'
ansi_yellow = '\033[33m'
ansi_blue = '\033[34m'
ansi_purple = '\033[35m'
ansi_cyan = '\033[36m'
ansi_white = '\033[37m'

def print_color(string, color):
    if 'black' in color:
        print ansi_black + string + ansi_reset,
    elif 'red' in color:
        print ansi_red + string + ansi_reset,
    elif 'green' in color:
        print ansi_green + string + ansi_reset,
    elif 'yellow' in color:
        print ansi_yellow + string + ansi_reset,
    elif 'blue' in color:
        print ansi_blue + string + ansi_reset,
    elif 'purple' in color:
        print ansi_purple + string + ansi_reset,
    elif 'cyan' in color:
        print ansi_cyan + string + ansi_reset,
    elif 'white' in color:
        print ansi_white + string + ansi_reset,
