from config.DBConfig import mongoDB


class TokenBlackListService:
    @staticmethod
    def isBlackListed(token):
        q = mongoDB.db.TokenBlackList.find_one({'token': token})
        if q is None:
            return False
        else:
            return True

    @staticmethod
    def addToTokenBlackList(token):
        mongoDB.db.TokenBlackList.insert({"token": token})
