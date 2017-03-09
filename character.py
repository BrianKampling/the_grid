import locations
import commands


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
            print self.current_location.description
        elif 'help' in command:
            print commands.help()
        if 'north' in command:
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
            print 'Invalid Command'

    def move(self, command):
        try:
            self.current_location = locations.get_location(self.current_location.exits[command])
        except:
            print 'You cannot go that way'
        print self.current_location.description
