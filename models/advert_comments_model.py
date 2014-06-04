from database_structure import *
from db import Database
from helpers.helper_functions import *


class AdvertCommentsModel(Database):
    def get_comments(self, advert_id):
        advert_comments = self.store.find(AdvertComment, AdvertComment.advert_id == verify_uuid(advert_id))
        return advert_comments

    def create_comment(self, **kw):
        advert_comment = AdvertComment()
        advert_comment.advert_id = verify_uuid(kw['advert_id'])
        advert_comment.from_user_id = verify_uuid(kw['from_user_id'])
        advert_comment.description = kw['description']

        self.store.add(advert_comment)
        self.store.commit()

    def delete_comment(self, comment_id):
        self.store.find(AdvertComment, AdvertComment.id == comment_id).remove()


