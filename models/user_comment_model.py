from database_structure import *
import uuid
from db import Database


class CommentUserModel(Database):
    def get_comments(self, user_id):
        user_comments = self.store.find(UserComment, UserComment.user_id == uuid.UUID(user_id))
        return user_comments

    def create_comment(self, **kw):
        user_comment = UserComment()
        user_comment.user_id = kw['user_id']
        user_comment.from_user_id = kw['from_user_id']
        user_comment.description = kw['description']

        self.store.add(user_comment)
        self.store.commit()

    def delete_comment(self, comment_id):
        self.store.find(UserComment, UserComment.id == comment_id).remove()


