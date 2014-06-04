from database_structure import *
import uuid
from db import Database
from helpers.helper_functions import *


class RequestModel(Database):
    def get_requests(self, advert_id):
        requests = self.store.find(Request, Request.advert_id == verify_uuid(advert_id))
        return requests

    def get_request(self, request_id):
        request = self.store.find(Request, Request.id == verify_uuid(request_id)).one()
        return request

    def create_request(self, **kw):
        request = Request()
        request.advert_id = verify_uuid(kw['advert_id'])
        request.request_user_id = verify_uuid(kw['request_user_id'])

        self.store.add(request)
        self.store.commit()

    def update_request(self, **kw):
        request = self.store.find(Request, Request.id == kw['request_id']).one()
        request.advert_id = kw['advert_id']
        request.user_id = kw['user_id']
        self.store.commit()

    def delete_request(self, request_id):
        self.store.find(Request, Request.id == request_id).remove()
