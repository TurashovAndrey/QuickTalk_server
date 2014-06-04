from base_handler import BaseHandler
from helpers.helper_functions import *
from models.advert_comments_model import AdvertCommentsModel


class AdvertCommentsHandler(BaseHandler):
    def get(self):
        try:
            advert_id = self.get_argument('advert_id', None)
            comments = AdvertCommentsModel().get_comments(advert_id)
            response = []

            for comment in comments:
                advert_comment = dict()
                advert_comment['id'] = comment.id
                advert_comment['from_user_id'] = str(comment.from_user_id)
                advert_comment['advert_id'] = str(comment.advert_id)
                advert_comment['description'] = comment.description

                response.append(advert_comment)

            self.write({"advert_comments":response})

        except Exception,e:
            self.write_exception(e)

    def post(self):
        try:
            advert_id = get_json_argument(self.request.body, 'advert_id', None)
            user_id = get_json_argument(self.request.body, 'from_user_id', None)
            description = get_json_argument(self.request.body, 'description', None)

            AdvertCommentsModel().create_comment(advert_id = advert_id,
                                        from_user_id = user_id,
                                        description = description)

            response = dict()
            response.update(success={'code': 1})
            self.write(response)
        except Exception,e:
            self.write_exception(e)