
import sys
from vue.admin.member_vue import MemberVue
from vue.admin.sport_vue import SportVue
from exceptions import ResourceNotFound, Error, InvalidData


class AdminVue(MemberVue, SportVue):
    """
    Admin Vue
    Admin specific interfaces
    """

    def __init__(self, member_controller, sport_controller):
        super().__init__(member_controller)
        super().__init__(sport_controller)

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

    def admin_shell(self):

        commands = {
            "exit": "Quit the Shell",
            "add": "Add association member",
            "list": "List association members",
            "search": "Show member profile",
            "delete": "Delete a member",
            "update": "Update a member",

            "addSP": "Add association sport",
            "listSP": "List association sport",
            "searchSP": "Show sport profile",
            "deleteSP": "Delete a sport",
            "updateSP": "Update a sport",

            "help": "Show this help"
        }

        self.help(commands)

        while True:
            try:
                command = self.ask_command(commands)
                if command == 'exit':
                    # Exit loop
                    break
                elif command == 'add':
                    member = self.add_member()
                    self.show_member(member)
                elif command == 'list':
                    self.show_members()
                elif command == 'search':
                    member = self.search_member()
                    self.show_member(member)
                elif command == 'delete':
                    self.delete_member()
                elif command == 'update':
                    member = self.update_member()
                    self.show_member(member)
                elif command == 'help':
                    self.help(commands)

                elif command == 'addSP':
                    sport = self.add_sport()
                    self.show_sport(sport)


                else:
                    print("Unknown command")
            except ResourceNotFound:
                self.error_message("Member not found")
            except InvalidData as e:
                self.error_message(str(e))
            except Error as e:
                self.error_message("An error occurred (%s)" % str(e))
