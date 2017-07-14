from config.DBConfig import mongoDB
from schema.AuthUser import AuthUser


class AppUserService:
    @staticmethod
    def getOneByName(name):
        q = mongoDB.db.AuthUser.find_one({'username': name})
        if q is None:
            return {}
        data, errors = AuthUser().load(q)
        return data

    @staticmethod
    def create(authUser):
        app_user_id = mongoDB.db.AuthUser.insert(authUser)
        q = mongoDB.db.AuthUser.find_one_or_404({'_id': app_user_id})
        data, errors = AuthUser().load(q)
        return data
