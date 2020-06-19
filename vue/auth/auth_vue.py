

import sys

from vue.admin.member_vue import MemberVue
from vue.common import Common

from exceptions import ResourceNotFound, Error, InvalidData


class AuthVue(MemberVue):
    """
    Auth Vue
    Auth specific interfaces
    """

    def __init__(self, member_controller):
        MemberVue.__init__(self, member_controller)
        

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

    def auth_shell(self):
        return self.search_member() 

    def ask_password(self):
        return self._common.ask_password()
        
        