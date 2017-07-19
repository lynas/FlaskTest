from schema.AuthUser import AuthUser


class AppUserService:
    @staticmethod
    def getOneByName(name):
        from main import dbCon
        q = dbCon.db.AuthUser.find_one({'username': name})
        if q is None:
            return {}
        data, errors = AuthUser().load(q)
        return data

    @staticmethod
    def create(authUser):
        from main import dbCon
        app_user_id = dbCon.db.AuthUser.insert(authUser)
        q = dbCon.db.AuthUser.find_one_or_404({'_id': app_user_id})
        data, errors = AuthUser().load(q)
        return data
