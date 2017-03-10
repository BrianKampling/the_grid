import sys
from utils.print_color import print_color

from character import Character
def starting_location():
    pc = Character()
    print_color('\nWelcome to the land of mystery what is your name: ', 'green')
    name = raw_input()
    pc.start_pc(name)
    print_color('\nWelcome ' + pc.name, 'green')
    command = raw_input('\nWhat do you want to do? ')
    while 'quit' not in command:
        pc.process_command(command)
        print_color('\n' + pc.name, 'cyan')
        print_color('=: ', 'green')
        command = raw_input()
    raw_input('Thanks for playing, press enter to exit.')

starting_location()