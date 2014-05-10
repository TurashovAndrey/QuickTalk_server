from database_structure import *
import uuid
from db import Database


class AdvertModel(Database):
    def get_advert(self, advert_id):
        advert = self.store.find(Advert, Advert.advert_id == uuid.UUID(advert_id)).one()
        return advert

    def create_advert(self, **kw):
        advert = Advert()
        advert.advert_id = uuid.uuid4()
        advert.title = kw['title']
        advert.description = kw['description']
        advert.type_id = int(kw['type_id'])
        advert.group_id = int(kw['group_id'])
        advert.created_by = uuid.UUID('6e12f572-ed56-43b8-9aaf-a7f08f4ff1af')
        advert.status_id = 1

        self.store.add(advert)
        self.store.commit()

    def update_advert(self, **kw):
        advert = self.store.find(Advert, Advert.advert_id == kw['advert_id']).one()
        advert.title = kw['title']
        advert.description = kw['description']
        self.store.commit()

    def delete_advert(self, advert_id):
        advert = self.store.find(Advert, Advert.advert_id == advert_id).remove()
