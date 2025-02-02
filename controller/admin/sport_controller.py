import re

from model.dao.admin.sport_dao import SportDAO
from exceptions import Error, InvalidData


class SportController:
    """
    Sport actions
    """

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frames = []

    def list_sports(self):


        with self._database_engine.new_session() as session:
            sports = SportDAO(session).get_all()
            sports_data = [sport.to_dict() for sport in sports]
            
        ## ou
        session = self._database_engine.new_session()
        with session :
            sports = SportDAO(session).get_all()
            sports_data = [sport.to_dict() for sport in sports]

        ## ou alors
        session = self._database_engine.new_session()
        sports = SportDAO(session).get_all()
        sports_data = [sport.to_dict() for sport in sports]

        session.commit()
        session.close()

        return sports_data

    def get_sport(self, sport_id):
        with self._database_engine.new_session() as session:
            sport = SportDAO(session).get(sport_id)
            sport_data = sport.to_dict()
        return sport_data

    def create_sport(self, data):

        self._check_profile_data(data)
        try:
            with self._database_engine.new_session() as session:
                # Save sport in database
                sport = SportDAO(session).create(data)
                sport_data = sport.to_dict()
                return sport_data
        except Error as e:
            # log error
            raise e

    def update_sport(self, sport_id, sport_data):

        self._check_profile_data(sport_data, update=True)
        with self._database_engine.new_session() as session:
            sport_dao = SportDAO(session)
            sport = sport_dao.get(sport_id)
            sport = sport_dao.update(sport, sport_data)
            return sport.to_dict()

    def delete_sport(self, sport_id):

        with self._database_engine.new_session() as session:
            sport_dao = SportDAO(session)
            sport = sport_dao.get(sport_id)
            sport_dao.delete(sport)

    def search_sport(self, name):

        # Query database
        with self._database_engine.new_session() as session:
            sport_dao = SportDAO(session)
            sport = sport_dao.get_by_name(name)
            return sport.to_dict()

    def _check_profile_data(self, data, update=False):
        name_pattern = re.compile("^[\S-]{2,50}$")
        mandatories = {
            'name': {"type": str, "regex": name_pattern},
        }
        for mandatory, specs in mandatories.items():
            if not update:
                if mandatory not in data or data[mandatory] is None:
                    raise InvalidData("Missing value %s" % mandatory)
            else:
                if mandatory not in data:
                    continue
            value = data[mandatory]
            if "type" in specs and not isinstance(value, specs["type"]):
                raise InvalidData("Invalid type %s" % mandatory)
            if "regex" in specs and isinstance(value, str) and not re.match(specs["regex"], value):
                raise InvalidData("Invalid value %s" % mandatory)
