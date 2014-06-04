from base_handler import BaseHandler
from models.request_model import RequestModel
from helpers.helper_functions import *


class RequestHandler(BaseHandler):
    def get(self):
        try:
            advert_id = self.get_argument('advert_id', None)
            adverts = RequestModel().get_requests(advert_id)
            response = []

            for advert in adverts:
                adv = dict()
                adv['id'] = advert.id
                adv['request_user_id'] = str(advert.request_user_id)
                adv['advert_id'] = str(advert.advert_id)

                response.append(adv)

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