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
        response['sub_category_id'] = advert.sub_category_id
        response['price'] = advert.price

        self.write(response)

    @is_authenticated
    def post(self):
        title = get_json_argument(self.request.body, 'title', None)
        description = get_json_argument(self.request.body, 'description', None)
        type_id = get_json_argument(self.request.body, 'type_id', None)
        group_id = get_json_argument(self.request.body, 'group_id', None)
        sub_category_id = get_json_argument(self.request.body, 'sub_category_id', None)
        price = get_json_argument(self.request.body, 'price', None)

        AdvertModel().create_advert(title = title,
                                    description = description,
                                    type_id = type_id,
                                    group_id = group_id,
                                    sub_category_id = sub_category_id,
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

class AdvertSubCategoriesHandler(BaseHandler):
    def get(self):
        category_id = self.get_argument('category_id', None)
        sub_categories = AdvertModel().get_advert_sub_categories(category_id)
        response = []

        for sub_category in sub_categories:
            sub_cat = dict()
            sub_cat['id'] = sub_category.id
            sub_cat['category_id'] = sub_category.category_id
            sub_cat['name'] = sub_category.sub_category_name

            response.append(sub_cat)

        self.write({"sub_categories":response})


