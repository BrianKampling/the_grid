import sys
from utils.print_color import printGreen

from character import Character
def starting_location():
    pc = Character()
    name = raw_input('Welcome to the land of mystery what is your name: ')
    pc.start_pc(name)
    print 'Welcome ' + pc.name
    command = raw_input('What do you want to do? ')
    while 'quit' not in command:
        pc.process_command(command)
        command = raw_input('=: ')
    raw_input('Thanks for playing, press enter to exit.')

test_string = """     \n
              |
              |
            --#--
              |
              |
                 """

printGreen(test_string)
starting_location()