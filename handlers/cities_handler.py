from base_handler import BaseHandler
from models.city_model import CityModel

class CitiesHandler(BaseHandler):
    def get(self):
        cities = CityModel().get_cities()

        response = []
        for city in cities:
            city_dict = dict()
            city_dict['city_id'] = str(city.id)
            city_dict['city_name'] = city.city_name
            city_dict['country_id'] = city.country_id

            response.append(city_dict)

        self.write({"cities": response})
