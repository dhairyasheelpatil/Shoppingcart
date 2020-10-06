import User
import uuid

class Session:
    _user = None
    _token = None
    def __init__(self, user: User):
        self._user = user
        self._token =  uuid.uuid1()

    def get_session_token(self):
        return self._token

    def get_user(self):
        return self._user

    def __str__(self):
        return "%s" % self._token