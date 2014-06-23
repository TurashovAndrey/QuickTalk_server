from database_structure import *
import uuid
from db import Database
from helpers.helper_functions import verify_uuid

class CityModel(Database):
    def get_cities(self):
        cities = self.store.find(City)
        return cities
