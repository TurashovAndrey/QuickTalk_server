from base_handler import BaseHandler
from helpers.helper_functions import *
from models.advert_model import AdvertModel
from base_handler import is_authenticated


class AdvertHandler(BaseHandler):
    def get(self):
        advert_id = self.get_argument('advert_id', None)
        advert,user = AdvertModel().get_advert(advert_id)

        response = dict()
        response['advert_id'] = str(advert.advert_id)
        response['description'] = advert.description
        response['title'] = advert.title
        response['created_by'] = str(user.username)
        response['status_id'] = advert.status_id
        response['price'] = advert.price

        self.write(response)

    @is_authenticated
    def post(self):
        title = get_json_argument(self.request.body, 'title', None)
        description = get_json_argument(self.request.body, 'description', None)
        type_id = get_json_argument(self.request.body, 'type_id', None)
        group_id = get_json_argument(self.request.body, 'group_id', None)
        price = get_json_argument(self.request.body, 'price', None)

        AdvertModel().create_advert(title = title,
                                    description = description,
                                    type_id = type_id,
                                    group_id = group_id,
                                    user_id = self.session['user_id'],
                                    price = price)

        response = dict()
        response.update(success={'code': 1})
        self.write(response)


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

class AdvertTypesHandler(BaseHandler):
    def get(self):
        category_id = self.get_argument('category_id', None)
        advert_types = AdvertModel().get_advert_types(category_id)
        response = []

        for advert_type in advert_types:
            advert_type_dict = dict()
            advert_type_dict['id'] = advert_type.id
            advert_type_dict['category_id'] = advert_type.category_id
            advert_type_dict['name'] = advert_type.type_name

            response.append(advert_type_dict)

        self.write({"types":response})

class AdvertsHandler(BaseHandler):
    def get(self):
        type_id = self.get_argument('type_id', None)
        user_id = self.get_argument('user_id', None)
        if type_id:
            adverts = AdvertModel().get_adverts_by_type(type_id)
        elif user_id:
            adverts = AdvertModel().get_adverts_by_user_id(user_id)
        else:
            adverts = AdvertModel().get_adverts()

        response = []
        for advert,user in adverts:
            advert_dict = dict()
            advert_dict['advert_id'] = str(advert.advert_id)
            advert_dict['description'] = advert.description
            advert_dict['title'] = advert.title
            advert_dict['created_by'] = str(user.username)
            advert_dict['status_id'] = advert.status_id
            advert_dict['price'] = advert.price

            response.append(advert_dict)

        self.write({"adverts": response})

