from vue.common import Common

class SportVue:
    """
    Sport Vue
    Sports interface features
    """

    def __init__(self, sport_controller):
        self._common = Common()
        self._sport_controller = sport_controller

    def add_sport(self):
        # Show subscription formular
        data = {}
        print("BDS Subscription")
        print()
        data['name'] = self._common.ask_name(key_name="name")
        print()
        return self._sport_controller.create_sport(data)

    def show_sport(self, sport: dict):
        print("Sport profile: ")
        print(sport['name'].capitalize())

    def error_message(self, message: str):
        print("/!\\ %s" % message.upper())

    def succes_message(self, message: str = ""):
        print("Operation succeeded: %s" % message)

    def show_sports(self):

        sports = self._sport_controller.list_sports()

        print("Sports: ")
        for sport in sports:
            print("* %s " % (sport['name'].capitalize()))

    def search_sport(self):
        name = self._common.ask_name('name')
        sport = self._sport_controller.search_sport(name)
        return sport

    def update_sport(self):
        sport = self.search_sport()
        data = {}
        print("Update Sport")
        print()
        data['name'] = self._common.ask_name(key_name="name", default=sport['name'])
        print()
        return self._sport_controller.update_sport(sport['id'], data)

    def delete_sport(self):
        sport = self.search_sport()
        self._sport_controller.delete_sport(sport['id'])
        self.succes_message()

    def set_coach_sport(self, sport, member_id):
        data = {}
        data['name']= sport['name']
        data['id_coach'] = member_id
        return self._sport_controller.update_sport(sport['id'], data)
  

    