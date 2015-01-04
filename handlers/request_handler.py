from base_handler import BaseHandler
from models.request_model import RequestModel
from helpers.helper_functions import *


class RequestHandler(BaseHandler):
    def get(self):
        try:
            user_id = self.get_argument('user_id', None)
            users = RequestModel().get_requests(user_id)
            response = []

            for user in users:
                user = dict()
                user['id'] = user.id
                user['request_user_id'] = str(user.request_user_id)
                user['advert_id'] = str(user.advert_id)

                response.append(user)

            self.write({"requests":response})

        except Exception,e:
            self.write_exception(e)

    def post(self):
        try:
            request_user_id = get_json_argument(self.request.body, 'request_user_id', None)
            advert_id = get_json_argument(self.request.body, 'advert_id', None)

            RequestModel().create_request(request_user_id=request_user_id,
                                          advert_id=advert_id)

            response = dict()
            response.update(success={'code': 1})
            self.write(response)
        except Exception,e:
            self.write_exception(e)