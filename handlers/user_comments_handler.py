from base_handler import BaseHandler
from helpers.helper_functions import *
from models.user_comments_model import UserCommentsModel


class UserCommentsHandler(BaseHandler):
    def get(self):
        user_id = self.get_argument('user_id', None)
        comments = UserCommentsModel().get_comments(user_id)
        response = []

        for comment in comments:
            user_comment = dict()
            user_comment['id'] = comment.id
            user_comment['user_id'] = str(comment.user_id)
            user_comment['from_user_id'] = str(comment.from_user_id)
            user_comment['description'] = comment.description

            response.append(user_comment)

        self.write({"user_comments":response})

    def post(self):
        try:
            from_user_id = get_json_argument(self.request.body, 'from_user_id', None)
            user_id = get_json_argument(self.request.body, 'user_id', None)
            description = get_json_argument(self.request.body, 'description', None)

            UserCommentsModel().create_comment(from_user_id = from_user_id,
                                        user_id = user_id,
                                        description = description)

            response = dict()
            response.update(success={'code': 1})
            self.write(response)
        except Exception,e:
            self.write_exception(e)