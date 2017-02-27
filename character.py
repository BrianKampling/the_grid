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
        elif 'move' in command:
            print 'Here are your exits: '
            for exits in self.current_location.exits:
                print exits
            dir = raw_input("where do you want to move to: ")
            try:
                self.current_location = locations.get_location(self.current_location.exits[dir])
            except:
                print 'You cannot go that way'
            print self.current_location.description
        else:
            print 'Invalid Command'
