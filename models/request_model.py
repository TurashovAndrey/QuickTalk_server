from database_structure import *
import uuid
from db import Database


class RequestModel(Database):
    def get_request(self, request_id):
        request = self.store.find(Request, Request.id == uuid.UUID(request_id)).one()
        return request

    def create_request(self, **kw):
        request = Request()
        request.advert_id = kw['advert_id']
        request.user_id = kw['user_id']

        self.store.add(request)
        self.store.commit()

    def update_advert(self, **kw):
        request = self.store.find(Request, Request.id == kw['request_id']).one()
        request.advert_id = kw['advert_id']
        request.user_id = kw['user_id']
        self.store.commit()

    def delete_advert(self, request_id):
        self.store.find(Request, Request.id == request_id).remove()
