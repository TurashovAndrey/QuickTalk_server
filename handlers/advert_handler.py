from base_handler import BaseHandler
from helpers.helper_functions import *
from models.advert_model import AdvertModel


class AdvertHandler(BaseHandler):
    def get(self):
        advert_id = self.get_argument('advert_id', None)
        advert_id = 'd801d00f-0ca6-4069-a0fb-73277a449b57'
        advert = AdvertModel().get_advert(advert_id)

        response = dict()
        #response['advert_id'] = advert.advert_id
        response['description'] = advert.description
        response['title'] = advert.title

        self.write(response)

    def post(self):
        title = get_json_argument(self.request.body, 'title', None)
        description = get_json_argument(self.request.body, 'description', None)
        type_id = get_json_argument(self.request.body, 'type_id', None)
        group_id = get_json_argument(self.request.body, 'group_id', None)

        AdvertModel().create_advert(title = title,
                                    description = description,
                                    type_id = type_id,
                                    group_id = group_id)


class AdvertCategoriesHandler(BaseHandler):
    def get(self):
        categories = AdvertModel().get_advert_categories()
        response = []

        for category in categories:
            cat = dict()
            cat['id'] = category.id
            cat['name'] = category.category_name

            response.append(cat)

        self.write({"categories":response})


