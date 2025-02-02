
from model.database import DatabaseEngine
from controller.member_controller import MemberController
from controller.sport_controller import SportController
from vue.admin_vue import AdminVue
from exceptions import Error


def main():
    print("Welcome of BDS Association")

    # Init db
    database_engine = DatabaseEngine(url='sqlite:///bds.db')
    database_engine.create_database()
    member_controller = MemberController(database_engine)
    member_controller_sport = SportController(database_engine)
    admin_vue = AdminVue(member_controller, member_controller_sport)

    try:
        member = admin_vue.add_member()
        admin_vue.show_member(member)
    except Error as e:
        admin_vue.error_message(str(e))


if __name__ == "__main__":
    main()
