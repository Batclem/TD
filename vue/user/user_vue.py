
import sys
from vue.admin.member_vue import MemberVue
from vue.admin.sport_vue import SportVue
from exceptions import ResourceNotFound, Error, InvalidData


class UserVue(MemberVue, SportVue):
    """
    User Vue
    User specific interfaces
    """

    def __init__(self, member, member_controller, sport_controller):
        SportVue.__init__(self, sport_controller)
        MemberVue.__init__(self, member_controller)
        self.member = member

    def help(self, commands):
        print()
        for command, description in commands.items():
            print("  * %s: '%s'" % (command, description))
        print()

    def ask_command(self, commands):

        command = input('command > ').lower().strip()
        while command not in commands.keys():
            print("Unknown command")
            command = input('command >').lower().strip()

        return command

    def user_shell(self):

        commands = {
            "exit": "Quit the Shell",
            "update_sport": "change practiced sport",
            "show_sport": "show practiced sport",
            "show_profil": "show profil information",
            "update_profil": "change profil information",
            "help": "Show this help"
        }

        self.help(commands)

        while True:
            try:
                command = self.ask_command(commands)
                if command == 'exit':
                    # Exit loop
                    break
                elif command == 'update_sport':
                    self.member = self.update_my_sport(self.member)
                elif command == 'show_sport':
                    self.member = self.show_sports(self.member)
                elif command == 'update_profil':
                    self.member = self.update_profile(self.member)
                elif command == 'show_profil':
                    self.show_member(self.member)
                elif command == 'help':
                    self.help(commands)
                else:
                    print("Unknown command")
            except ResourceNotFound:
                self.error_message("Member not found")
            except InvalidData as e:
                self.error_message(str(e))
            except Error as e:
                self.error_message("An error occurred (%s)" % str(e))
