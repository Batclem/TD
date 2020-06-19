import bcrypt

from controller.admin.member_controller import MemberController
from controller.admin.sport_controller import SportController
from model.database import DatabaseEngine
from vue.admin.admin_vue import AdminVue
from vue.user.user_vue import UserVue
from vue.auth.auth_vue import AuthVue



#from vue.user.user_vue import UserVue


def main():
    print("Welcome of BDS Association")

    # Init db
    database_engine = DatabaseEngine(url='sqlite:///bds.db')
    database_engine.create_database()

    #Authentification
    print('Connnection : ')
    auth_controller = MemberController(database_engine)
    member = AuthVue(auth_controller).auth_shell()
    
    password = AuthVue(auth_controller).ask_password()

    if bcrypt.checkpw(bytes(password, encoding='utf-8'), member['password']):
        admin_controller = MemberController(database_engine)
        admin_controller_sport = SportController(database_engine)
        if member['isAdmin'] == 1:
            #Si Admin
            AdminVue(admin_controller, admin_controller_sport).admin_shell()
        else:
            #Si User
            UserVue(member ,admin_controller, admin_controller_sport).user_shell()
    
    else:
        print('Wrong password')



if __name__ == "__main__":
    main()
