import locations
import commands
from utils.print_color import print_color


class Character:
    def __init__(self):
        pass

    name = ''

    def start_pc(self, name):
        self.name = name
        self.current_location = locations.get_location('The Silvery Moon Tavern')

    def print_name(self):
        print self.name

    def process_command(self, command):
        if 'look' in command:
            print_color('\n' + self.current_location.description, 'green')
        elif 'help' in command:
            print commands.help()
        elif 'north' or 'n' in command:
            if 'n' in command:
                command = 'north'
            self.move(command)
        elif 'south' in command:
            self.move(command)
        elif 'east' in command:
            self.move(command)
        elif 'west' in command:
            self.move(command)
        elif 'up' in command:
            self.move(command)
        elif 'down' in command:
            self.move(command)
        elif 'forward' in command:
            self.move(command)
        elif 'back' in command:
            self.move(command)
        else:
            print_color('\nInvalid Command', 'red')

    def move(self, command):
        try:
            self.current_location = locations.get_location(self.current_location.exits[command])
        except:
            print_color('\nYou cannot go that way', 'red')
        print_color('\n' + self.current_location.description, 'green')
