
from controller.admin.member_controller import MemberController
from controller.admin.sport_controller import SportController
from model.database import DatabaseEngine
from vue.admin.admin_vue import AdminVue


#from vue.user.user_vue import UserVue


def main():
    print("Welcome of BDS Association")

    # Init db
    database_engine = DatabaseEngine(url='sqlite:///bds.db')
    database_engine.create_database()

    #Authentification


    #Si Admin
    admin_controller = MemberController(database_engine)
    admin_controller_sport = SportController(database_engine)
    #AdminVue(admin_controller).admin_shell()
    AdminVue(admin_controller, admin_controller_sport).admin_shell()

    #Si (User)



if __name__ == "__main__":
    main()
